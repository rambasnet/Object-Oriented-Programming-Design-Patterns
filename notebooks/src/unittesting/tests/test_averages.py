"""
Unittesting demo
"""


from __future__ import annotations  # for Python < 3.7
import unittest
from typing import Optional


def average(seq: list[Optional[float]]) -> float:
    """Average of non-None values"""
    total, count = 0.0, 0
    for v in filter(None, seq):
        total += v
        count += 1
    return total / count


class TestAverage(unittest.TestCase):
    """Test the average function.
    """

    def test_zero(self) -> None:
        """Test average of an empty list.
        """
        self.assertRaises(ZeroDivisionError, average, [])

    def test_with_zero(self) -> None:
        """Test average of a list containing a zero.
        """
        with self.assertRaises(ZeroDivisionError):
            average([])
