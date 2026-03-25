#!/usr/bin/env python3
"""
Auto-translate Korean Jekyll posts to English using Claude API.
Only translates posts that don't already have an English equivalent.

Usage:
  python scripts/translate.py

Requires:
  ANTHROPIC_API_KEY environment variable
  pip install anthropic
"""

import os
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

KO_DIR = Path("_posts/ko")
EN_DIR = Path("_posts/en")

SYSTEM_PROMPT = """You are a professional translator specializing in PM (Project Management) content.
You translate Korean Jekyll blog posts to English for a bilingual PM blog.

Rules:
- Translate the `title` and `description` front matter fields to natural English
- Change `lang: ko` to `lang: en`
- Keep ALL other front matter fields unchanged (ref, date, categories, tags, pdu_category, pdu_hours, layout, permalink)
- Translate body content to clear, professional English
- Keep all markdown formatting intact (headers, bold, italic, lists, code blocks, tables)
- Keep PM acronyms as-is: WBS, PMBOK, PMP, PDU, RACI, RAID, etc.
- Return ONLY the complete translated post with no extra commentary"""


def translate_post(ko_content: str) -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"Translate this Korean PM blog post to English:\n\n{ko_content}"
            }
        ]
    )
    return message.content[0].text.strip()


def main():
    if not KO_DIR.exists():
        print(f"Korean posts directory not found: {KO_DIR}")
        return

    EN_DIR.mkdir(parents=True, exist_ok=True)

    ko_files = sorted(KO_DIR.glob("*.md"))
    if not ko_files:
        print("No Korean posts found.")
        return

    new_count = 0
    skip_count = 0

    for ko_file in ko_files:
        en_file = EN_DIR / ko_file.name

        if en_file.exists():
            print(f"  Already exists: {ko_file.name}")
            skip_count += 1
            continue

        print(f"  Translating: {ko_file.name} ...", end="", flush=True)
        ko_content = ko_file.read_text(encoding="utf-8")

        try:
            en_content = translate_post(ko_content)
            en_file.write_text(en_content, encoding="utf-8")
            print(f" done")
            new_count += 1
        except Exception as e:
            print(f" ERROR: {e}")
            raise

    print(f"Translation complete: {new_count} translated, {skip_count} skipped.")


if __name__ == "__main__":
    main()
