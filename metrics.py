"""Numeric metrics utilities for statistical calculations."""

from __future__ import annotations


def moving_average(values: list[float], window_size: int) -> list[float]:
    """Compute the simple moving average with the given window size.

    For each position i where i >= window_size - 1, the average is computed
    over values[i - window_size + 1 : i + 1]. Positions before the first
    full window are excluded from the result.

    Raises ValueError if window_size is less than 1 or greater than the
    number of values.
    """
    ...


def clamp(value: float, minimum: float, maximum: float) -> float:
    """Restrict value to the range [minimum, maximum].

    Raises ValueError if minimum is greater than maximum.
    """
    ...


def percentage_change(old_value: float, new_value: float) -> float:
    """Calculate the percentage change from old_value to new_value.

    Returns ((new_value - old_value) / old_value) * 100.
    Raises ValueError if old_value is zero.
    """
    ...


def standard_deviation(values: list[float]) -> float:
    """Compute the population standard deviation of the values.

    Uses the formula: sqrt(mean of squared deviations from the mean).
    Raises ValueError if the list is empty.
    """
    ...
