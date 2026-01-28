#!/usr/bin/env python3
"""
Generate daily_log from books progress data.
Reads _data/reading.yml and updates the log section based on:
- last_date_read dates
- log entry dates
- Progress distribution across reading days
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


def parse_date(date_str: str | None) -> datetime | None:
    """Parse YYYY-MM-DD date string."""
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except (ValueError, TypeError):
        return None


def date_key(dt: datetime) -> str:
    """Convert datetime to YYYY-MM-DD string."""
    return dt.strftime("%Y-%m-%d")


def generate_log_from_items(items: list[dict]) -> dict[str, int]:
    """
    Generate daily_log from books using explicit per-day logs.

    Rules (to keep math correct and avoid "guessing" earlier dates):
    - Only count days that have a log entry with a `date`.
    - If the log entry includes `start_page` and `end_page`, pages read is
      `end_page - start_page + 1` (only if both are valid ints and end>=start).
    - If a log entry has no page range, it contributes 0 pages (ignored).
    - No distribution/backfilling based on date_started / last_date_read.
    """
    log: dict[str, int] = defaultdict(int)
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    twelve_weeks_ago = today - timedelta(days=84)
    
    for item in items:
        if item.get("status") not in ("reading", "completed"):
            continue

        for log_entry in item.get("logs", []) or []:
            log_date = parse_date(log_entry.get("date"))
            if not log_date or log_date < twelve_weeks_ago:
                continue

            sp_raw = log_entry.get("start_page")
            ep_raw = log_entry.get("end_page")
            try:
                sp = int(sp_raw) if sp_raw is not None else None
            except (TypeError, ValueError):
                sp = None
            try:
                ep = int(ep_raw) if ep_raw is not None else None
            except (TypeError, ValueError):
                ep = None

            pages = 0
            if sp is not None and ep is not None and ep >= sp:
                pages = ep - sp + 1

            if pages > 0:
                log[date_key(log_date)] += pages
    
    # Convert to regular dict with string keys, sorted by date
    result = {k: int(v) for k, v in sorted(log.items()) if v > 0}
    return result


def update_reading_yml(data_path: Path) -> bool:
    """Read reading.yml, generate logs, and update the file."""
    if not data_path.exists():
        print(f"Error: {data_path} not found", file=sys.stderr)
        return False
    
    # Read file
    with open(data_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Parse YAML
    try:
        data = yaml.safe_load(content)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}", file=sys.stderr)
        return False
    
    # Generate logs
    books = data.get("books", [])
    
    daily_log = generate_log_from_items(books)
    
    # Write back using YAML dump, but preserve structure
    # Find the log section and replace it
    lines = content.split("\n")
    new_lines = []
    i = 0
    daily_log_replaced = False
    skipping_log_entry = False
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Replace daily_log section
        if stripped == "daily_log:":
            new_lines.append("daily_log:")
            if daily_log:
                for date, pages in sorted(daily_log.items()):
                    new_lines.append(f'  "{date}": {pages}')
            else:
                new_lines.append("  {}")
            # Skip existing entries until next top-level key
            i += 1
            skipping_log_entry = True
            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()
                # Stop if we hit another top-level key or empty line followed by top-level key
                if next_stripped and not next_line.startswith("  ") and not next_stripped.startswith("#"):
                    break
                if next_stripped == "" and i + 1 < len(lines):
                    # Check if next non-empty line is a top-level key
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and lines[j].strip() and not lines[j].startswith("  ") and not lines[j].strip().startswith("#"):
                        break
                i += 1
            skipping_log_entry = False
            daily_log_replaced = True
            continue
        
        # Remove comic_log section if it exists
        if stripped == "comic_log:":
            # Skip the entire comic_log section
            i += 1
            while i < len(lines):
                next_line = lines[i]
                next_stripped = next_line.strip()
                if next_stripped and not next_line.startswith("  ") and not next_stripped.startswith("#"):
                    break
                if next_stripped == "" and i + 1 < len(lines):
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and lines[j].strip() and not lines[j].startswith("  ") and not lines[j].strip().startswith("#"):
                        break
                i += 1
            continue
        
        # Skip lines that are part of old log sections (already handled above)
        if skipping_log_entry:
            i += 1
            continue
        
        new_lines.append(line)
        i += 1
    
    # Add missing daily_log section if needed
    if not daily_log_replaced:
        # Insert before books
        insert_idx = 0
        for idx, line in enumerate(new_lines):
            if line.strip() == "books:":
                insert_idx = idx
                break
        new_lines.insert(insert_idx, "daily_log:")
        if daily_log:
            for date, pages in sorted(daily_log.items()):
                new_lines.insert(insert_idx + 1, f'  "{date}": {pages}')
        else:
            new_lines.insert(insert_idx + 1, "  {}")
        new_lines.insert(insert_idx + 2, "")
    
    # Write updated content
    with open(data_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))
        if not new_lines[-1].endswith("\n"):
            f.write("\n")
    
    print(f"Generated daily_log with {len(daily_log)} entries")
    return True


def main() -> None:
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    data_path = repo_root / "_data" / "reading.yml"
    
    if not update_reading_yml(data_path):
        sys.exit(1)


if __name__ == "__main__":
    main()
