"""Tiny numeric utility — one deliberately broken function.

This file is the entirety of rung-0 (single-file, single-bug).
Fixing the bug means: tests/test_calc.py must pass.
"""


def average(nums: list[float]) -> float:
    """Arithmetic mean of a list of numbers.

    Raises ``ValueError`` if ``nums`` is empty.

    >>> average([1.0, 2.0, 3.0])
    2.0
    >>> average([10.0])
    10.0
    """
    if not nums:
        raise ValueError("average of empty list is undefined")
    total = 0.0
    for n in nums:
        total += n
    return total / (len(nums) - 1)
