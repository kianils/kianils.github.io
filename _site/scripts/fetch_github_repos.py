#!/usr/bin/env python3
"""
Fetch GitHub repos (public + private when GH_PAT is set) and write _data/github_repos.json.
Uses GITHUB_USERNAME and optionally GH_PAT env vars. Safe to run without PAT (public-only).
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

API = "https://api.github.com"
USER_AGENT = "Portfolio-GitHub-Repos/1.0"


def get_env(name: str, default: str | None = None) -> str | None:
    return os.environ.get(name) or default


def fetch(
    url: str,
    *,
    token: str | None = None,
) -> list[dict] | None:
    headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": USER_AGENT}
    if token:
        headers["Authorization"] = f"token {token}"
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode())
    except (HTTPError, URLError) as e:
        print(f"fetch error {url}: {e}", file=sys.stderr)
        return None


def main() -> None:
    username = get_env("GITHUB_USERNAME") or "kianils"
    token = get_env("GH_PAT")

    if token:
        url = f"{API}/user/repos?affiliation=owner,collaborator&sort=updated&per_page=100&type=all"
        raw = fetch(url, token=token)
    else:
        url = f"{API}/users/{username}/repos?sort=updated&per_page=100"
        raw = fetch(url)

    if raw is None:
        sys.exit(1)

    repos: list[dict] = []
    for r in raw:
        repos.append({
            "name": r.get("name") or "",
            "full_name": r.get("full_name") or "",
            "description": r.get("description") or "",
            "html_url": r.get("html_url") or "",
            "private": bool(r.get("private")),
            "language": r.get("language") or "",
            "stargazers_count": int(r.get("stargazers_count") or 0),
            "forks_count": int(r.get("forks_count") or 0),
            "pushed_at": r.get("pushed_at") or "",
            "created_at": r.get("created_at") or "",
        })

    out = {
        "username": username,
        "repos": repos,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "includes_private": bool(token),
    }

    data_dir = os.path.join(os.path.dirname(__file__), "..", "_data")
    os.makedirs(data_dir, exist_ok=True)
    path = os.path.join(data_dir, "github_repos.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(repos)} repos to {path} (includes_private={out['includes_private']})")


if __name__ == "__main__":
    main()
