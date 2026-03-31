"""Numeric metrics utilities for statistical calculations."""

from __future__ import annotations

import math


def moving_average(values: list[float], window_size: int) -> list[float]:
    """Compute the simple moving average with the given window size.

    For each position i where i >= window_size - 1, the average is computed
    over values[i - window_size + 1 : i + 1]. Positions before the first
    full window are excluded from the result.

    Raises ValueError if window_size is less than 1 or greater than the
    number of values.
    """
    if window_size < 1:
        raise ValueError("window_size must be at least 1")
    if window_size > len(values):
        raise ValueError("window_size must not exceed the number of values")

    result: list[float] = []
    for i in range(window_size - 1, len(values)):
        window: list[float] = values[i - window_size + 1 : i + 1]
        result.append(sum(window) / window_size)
    return result


def clamp(value: float, minimum: float, maximum: float) -> float:
    """Restrict value to the range [minimum, maximum].

    Raises ValueError if minimum is greater than maximum.
    """
    if minimum > maximum:
        raise ValueError("minimum must not exceed maximum")
    return max(minimum, min(maximum, value))


def percentage_change(old_value: float, new_value: float) -> float:
    """Calculate the percentage change from old_value to new_value.

    Returns ((new_value - old_value) / old_value) * 100.
    Raises ValueError if old_value is zero.
    """
    if old_value == 0:
        raise ValueError("old_value must not be zero")
    return ((new_value - old_value) / old_value) * 100


def standard_deviation(values: list[float]) -> float:
    """Compute the population standard deviation of the values.

    Uses the formula: sqrt(mean of squared deviations from the mean).
    Raises ValueError if the list is empty.
    """
    if not values:
        raise ValueError("values must not be empty")

    mean: float = sum(values) / len(values)
    squared_deviations: list[float] = [(v - mean) ** 2 for v in values]
    variance: float = sum(squared_deviations) / len(values)
    return math.sqrt(variance)
