"""Text processing utilities for tokenization, normalization, and truncation."""

from __future__ import annotations


def tokenize(text: str, delimiters: list[str] | None = None) -> list[str]:
    """Split text into tokens using the given delimiters, or whitespace by default."""
    ...


def normalize_whitespace(text: str) -> str:
    """Collapse consecutive whitespace characters into a single space and strip leading/trailing whitespace."""
    ...


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length characters, appending suffix if truncated.

    If the text is shorter than or equal to max_length, return it unchanged.
    Otherwise, truncate so that the result including the suffix is at most
    max_length characters.
    """
    ...


def count_words(text: str) -> int:
    """Count the number of whitespace-separated words in the text.

    Returns 0 for empty or whitespace-only strings.
    """
    ...
