"""
Python 3 Object-Oriented Programming

Chapter 13.  Testing Object-Oriented Programs.
"""

from __future__ import annotations  # for Python < 3.7
import collections
from typing import DefaultDict, List, Optional


class StatsList(List[Optional[float]]):
    """Stats with None objects rejected"""

    def mean(self) -> float:
        """Mean of values.

        Returns:
            float: Mean of values
        """
        clean = list(filter(None, self))
        return sum(clean) / len(clean)

    def median(self) -> float:
        """Median of values.

        Returns:
            float: Median of values
        """
        clean = list(filter(None, self))
        if len(clean) % 2:
            return clean[len(clean) // 2]

        idx = len(clean) // 2
        return (clean[idx] + clean[idx - 1]) / 2

    def mode(self) -> list[float]:
        """ Mode of values."""
        freqs: DefaultDict[float, int] = collections.defaultdict(int)
        for item in filter(None, self):
            freqs[item] += 1
        mode_freq = max(freqs.values())
        modes = [item for item, value in freqs.items() if value == mode_freq]
        return modes
