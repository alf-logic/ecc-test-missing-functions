"""Text processing utilities for tokenization, normalization, and truncation."""

from __future__ import annotations

import re


def tokenize(text: str, delimiters: list[str] | None = None) -> list[str]:
    """Split text into tokens using the given delimiters, or whitespace by default."""
    if not text:
        return []

    if delimiters is None:
        return text.split()

    pattern: str = "|".join(re.escape(d) for d in delimiters)
    tokens: list[str] = re.split(pattern, text)
    return [token for token in tokens if token]


def normalize_whitespace(text: str) -> str:
    """Collapse consecutive whitespace characters into a single space and strip leading/trailing whitespace."""
    return re.sub(r"\s+", " ", text).strip()


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length characters, appending suffix if truncated.

    If the text is shorter than or equal to max_length, return it unchanged.
    Otherwise, truncate so that the result including the suffix is at most
    max_length characters.
    """
    if len(text) <= max_length:
        return text

    truncated_length: int = max_length - len(suffix)
    if truncated_length <= 0:
        return suffix[:max_length]

    return text[:truncated_length] + suffix


def count_words(text: str) -> int:
    """Count the number of whitespace-separated words in the text.

    Returns 0 for empty or whitespace-only strings.
    """
    stripped: str = text.strip()
    if not stripped:
        return 0
    return len(stripped.split())
