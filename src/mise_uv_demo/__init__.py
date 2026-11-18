"""A tiny word counter for the mise and uv demo."""

import os

from rich.console import Console


def count_words(text: str) -> int:
    return len(text.split())


def count_unique_words(text: str) -> int:
    """Count whitespace-separated words, ignoring case but keeping punctuation."""
    return len(set(text.casefold().split()))


def count_characters(text: str) -> int:
    """Count characters, including whitespace."""
    return len(text)


def main() -> None:
    text = "mise and uv make setup smooth"
    console = Console(markup=False, highlight=False)
    console.print(os.environ.get("APP_GREETING", "Hello!"))
    console.print(f'Text: "{text}"')
    console.print(
        f"{count_words(text)} words, {count_unique_words(text)} unique words, "
        f"{count_characters(text)} characters"
    )
