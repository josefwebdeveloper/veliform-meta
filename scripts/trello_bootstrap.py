#!/usr/bin/env python3
"""Create Veliform Trello boards/lists and seed cards. Writes IDs to meta/ceo/trello.yaml."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from trello_client import card_names, create_board, create_card, create_list, trello_request  # noqa: E402

TRELLO_YAML = ROOT / "ceo" / "trello.yaml"
SEED_YAML = ROOT / "ceo" / "trello_seed.yaml"
LANDING = ROOT.parent / "veliform-landing"
VOICE = ROOT.parent / "voice"


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def save_yaml(path: Path, data: dict) -> None:
    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")


def ensure_board(board_cfg: dict) -> dict:
    if board_cfg.get("id"):
        return board_cfg
    created = create_board(board_cfg["name"], desc="Veliform task board")
    board_cfg["id"] = created["id"]
    board_cfg["url"] = created.get("url") or f"https://trello.com/b/{created.get('shortLink', created['id'])}"
    return board_cfg


def ensure_list(board_id: str, list_cfg: dict) -> dict:
    if list_cfg.get("id"):
        return list_cfg
    created = create_list(board_id, list_cfg["name"])
    list_cfg["id"] = created["id"]
    return list_cfg


def seed_cards(list_id: str, cards: list[dict]) -> int:
    existing = card_names(list_id)
    created = 0
    for item in cards:
        name = str(item.get("name") or "").strip()
        if not name or name in existing:
            continue
        create_card(list_id, name=name, desc=str(item.get("desc") or ""))
        created += 1
        existing.add(name)
    return created


def patch_agent_configs(registry: dict) -> None:
    company_lists = registry["boards"]["company"]["lists"]
    marketing_path = LANDING / "config" / "marketing-agent.json"
    finance_path = LANDING / "config" / "finance-agent.json"
    if marketing_path.is_file():
        data = json.loads(marketing_path.read_text(encoding="utf-8"))
        data.pop("clickup", None)
        data["trello"] = {
            "list_id": company_lists["seo_marketing"]["id"],
            "max_weekly_tasks": 3,
        }
        marketing_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    if finance_path.is_file():
        data = json.loads(finance_path.read_text(encoding="utf-8"))
        data.pop("clickup", None)
        data["trello"] = {
            "list_id": company_lists["company_hq"]["id"],
            "max_pulse_tasks": 1,
        }
        finance_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    registry = load_yaml(TRELLO_YAML)
    seed = load_yaml(SEED_YAML)
    total_cards = 0

    for board_key in ("company", "voice"):
        board_cfg = registry["boards"][board_key]
        ensure_board(board_cfg)
        for list_key, list_cfg in board_cfg["lists"].items():
            ensure_list(board_cfg["id"], list_cfg)
            cards = ((seed.get(board_key) or {}).get(list_key)) or []
            total_cards += seed_cards(list_cfg["id"], cards)

    save_yaml(TRELLO_YAML, registry)
    patch_agent_configs(registry)

    # Pin quick links on voice board description
    voice_board_id = registry["boards"]["voice"]["id"]
    trello_request(
        "PUT",
        f"/boards/{voice_board_id}",
        params={
            "desc": "\n".join(
                [
                    "Repo: https://github.com/josefwebdeveloper/voice-agent",
                    "Personal admin: https://personal-server-production-3d89.up.railway.app/admin",
                    "Business admin: https://voice-server-production-f958.up.railway.app/admin",
                    "Docs: voice/docs/TRELLO_PROJECT.md",
                ]
            )
        },
    )

    print(f"OK — boards ready, {total_cards} new cards seeded")
    print(f"Registry: {TRELLO_YAML}")
    print(f"Company board: {registry['boards']['company'].get('url')}")
    print(f"Voice board: {registry['boards']['voice'].get('url')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
