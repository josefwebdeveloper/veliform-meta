#!/usr/bin/env python3
"""Create or update Trello cards for a completed delivery. Requires TRELLO_API_KEY + TRELLO_TOKEN."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import yaml

from trello_client import create_card, list_cards, trello_request, TrelloError


def load_registry() -> dict:
    return yaml.safe_load((ROOT / "ceo" / "trello.yaml").read_text(encoding="utf-8"))


def find_card_by_prefix(list_id: str, prefix: str) -> dict | None:
    for card in list_cards(list_id):
        name = str(card.get("name") or "")
        if name.startswith(prefix):
            return card
    return None


def move_card_to_list(card_id: str, list_id: str) -> None:
    trello_request("PUT", f"/cards/{card_id}", params={"idList": list_id})


def main() -> int:
    parser = argparse.ArgumentParser(description="Log delivery to Veliform Trello boards")
    parser.add_argument("--voice-done", action="store_true", help="Add card to Veliform Voice ✅ Done")
    parser.add_argument("--company-seo", action="store_true", help="Add card to Company SEO & Marketing")
    parser.add_argument("--name", required=True, help="Card title")
    parser.add_argument("--desc", default="", help="Card description (markdown ok)")
    parser.add_argument("--move-prefix", default="", help="Move existing card starting with prefix to Done")
    args = parser.parse_args()

    reg = load_registry()
    voice_done = reg["boards"]["voice"]["lists"]["done"]["id"]
    seo_list = reg["boards"]["company"]["lists"]["seo_marketing"]["id"]

    if args.move_prefix:
        existing = find_card_by_prefix(reg["boards"]["voice"]["lists"]["in_progress"]["id"], args.move_prefix)
        if existing:
            move_card_to_list(existing["id"], voice_done)
            print(f"Moved: {existing.get('name')} → Done")

    if args.voice_done:
        card = create_card(voice_done, name=args.name, desc=args.desc)
        print(f"Voice Done: {card.get('url')}")

    if args.company_seo:
        card = create_card(seo_list, name=args.name, desc=args.desc)
        print(f"Company SEO: {card.get('url')}")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TrelloError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
