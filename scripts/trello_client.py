"""Trello REST API helpers for Veliform bootstrap and GitHub Actions."""

from __future__ import annotations

import os
from typing import Any

TRELLO_API = "https://api.trello.com/1"


class TrelloError(RuntimeError):
    pass


def _requests() -> Any:
    try:
        import requests
    except ImportError as exc:
        raise TrelloError("Install requests: pip install requests") from exc
    return requests


def credentials() -> tuple[str, str]:
    key = os.environ.get("TRELLO_API_KEY", "").strip()
    token = os.environ.get("TRELLO_TOKEN", "").strip()
    if not key or not token:
        raise TrelloError("TRELLO_API_KEY and TRELLO_TOKEN are required")
    return key, token


def auth_params() -> dict[str, str]:
    key, token = credentials()
    return {"key": key, "token": token}


def trello_request(
    method: str,
    path: str,
    *,
    params: dict[str, Any] | None = None,
    json_body: dict[str, Any] | None = None,
) -> Any:
    requests = _requests()
    merged = {**auth_params(), **(params or {})}
    url = f"{TRELLO_API}{path}"
    response = requests.request(method, url, params=merged, json=json_body, timeout=30)
    if not response.ok:
        raise TrelloError(f"Trello {method} {path} failed ({response.status_code}): {response.text[:500]}")
    if response.text.strip():
        return response.json()
    return None


def create_board(name: str, *, desc: str = "") -> dict[str, Any]:
    return trello_request("POST", "/boards", params={"name": name, "desc": desc, "defaultLists": "false"})


def create_list(board_id: str, name: str) -> dict[str, Any]:
    return trello_request("POST", "/lists", params={"name": name, "idBoard": board_id})


def list_cards(list_id: str) -> list[dict[str, Any]]:
    return trello_request("GET", f"/lists/{list_id}/cards", params={"fields": "name,desc,url,closed"})


def create_card(
    list_id: str,
    *,
    name: str,
    desc: str = "",
    pos: str = "bottom",
) -> dict[str, Any]:
    return trello_request(
        "POST",
        "/cards",
        params={"idList": list_id, "name": name, "desc": desc, "pos": pos},
    )


def existing_markers(list_id: str, prefix: str) -> set[str]:
    markers: set[str] = set()
    for card in list_cards(list_id):
        for line in str(card.get("desc") or "").splitlines():
            stripped = line.strip()
            if stripped.startswith(prefix) and stripped.endswith("]"):
                markers.add(stripped)
        for line in str(card.get("name") or "").splitlines():
            stripped = line.strip()
            if stripped.startswith(prefix) and stripped.endswith("]"):
                markers.add(stripped)
    return markers


def card_names(list_id: str) -> set[str]:
    return {str(card.get("name") or "").strip() for card in list_cards(list_id)}
