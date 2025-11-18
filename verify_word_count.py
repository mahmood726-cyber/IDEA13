#!/usr/bin/env python3
"""
Word count verification for BMJ manuscript
Requirement: 3,000-4,000 words for research articles
"""

import re
from pathlib import Path

def count_words(file_path):
    """Count words in a markdown file, excluding front matter and metadata."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)

    # Remove metadata lines (lines starting with ** or containing only formatting)
    content = re.sub(r'^\*\*.*?\*\*\s*$', '', content, flags=re.MULTILINE)

    # Remove markdown headers
    content = re.sub(r'^#+\s+', '', content, flags=re.MULTILINE)

    # Remove URLs
    content = re.sub(r'http[s]?://\S+', '', content)

    # Remove reference placeholders like [1-3] or [8,9]
    content = re.sub(r'\[\d+[-,\d]*\]', '', content)

    # Remove table separators and formatting
    content = re.sub(r'\|[-:]+\|', '', content)
    content = re.sub(r'^\|.*\|$', '', content, flags=re.MULTILINE)

    # Remove special markdown characters
    content = re.sub(r'[*_#`\[\]()]', '', content)

    # Split into words and count
    words = content.split()
    return len(words)

def main():
    # Define files and their sections
    sections = {
        'Abstract': 'manuscript_abstract.md',
        'Introduction': 'manuscript_introduction.md',
        'Methods': 'manuscript_methods.md',
        'Results': 'manuscript_results.md',
        'Discussion': 'manuscript_discussion.md'
    }

    print("=" * 70)
    print("BMJ MANUSCRIPT WORD COUNT VERIFICATION")
    print("=" * 70)
    print(f"\nBMJ Requirement: 3,000-4,000 words for research articles")
    print(f"(Abstract typically 400 words, not counted toward main text limit)\n")
    print("-" * 70)

    total_words = 0
    total_words_with_abstract = 0

    for section, filename in sections.items():
        file_path = Path(filename)
        if file_path.exists():
            word_count = count_words(file_path)
            total_words_with_abstract += word_count

            if section != 'Abstract':
                total_words += word_count

            # Determine status
            if section == 'Abstract':
                target = "~400 words"
                status = "✓" if 350 <= word_count <= 450 else "⚠"
            elif section == 'Introduction':
                target = "~750 words"
                status = "✓" if word_count <= 800 else "⚠"
            elif section == 'Methods':
                target = "~1,300 words"
                status = "✓" if word_count <= 1400 else "⚠"
            elif section == 'Results':
                target = "~1,850 words"
                status = "✓" if word_count <= 1900 else "⚠"
            elif section == 'Discussion':
                target = "~1,700 words"
                status = "✓" if word_count <= 1800 else "⚠"
            else:
                target = ""
                status = ""

            print(f"{section:20s}: {word_count:5d} words  {status}  (target: {target})")
        else:
            print(f"{section:20s}: FILE NOT FOUND")

    print("-" * 70)
    print(f"\nMAIN TEXT (excluding Abstract): {total_words:5d} words")
    print(f"TOTAL (including Abstract):      {total_words_with_abstract:5d} words")
    print()

    # Determine compliance
    if 3000 <= total_words <= 4000:
        print("✓ COMPLIANT: Word count meets BMJ requirements (3,000-4,000 words)")
        print(f"  Margin: {total_words - 3000} words above minimum")
        print(f"          {4000 - total_words} words below maximum")
    elif total_words < 3000:
        print(f"⚠ BELOW TARGET: {3000 - total_words} words short of minimum")
    else:
        print(f"✗ EXCEEDS LIMIT: {total_words - 4000} words over maximum")
        print(f"  Reduction needed: ~{((total_words - 3500) / total_words * 100):.1f}%")

    print("\n" + "=" * 70)

    # Summary
    print("\nSUMMARY:")
    print(f"  Original word count: ~10,524 words")
    print(f"  Current word count:  ~{total_words} words")
    print(f"  Reduction achieved:  ~{10524 - total_words} words ({(10524 - total_words) / 10524 * 100:.1f}%)")
    print("=" * 70)

if __name__ == "__main__":
    main()
