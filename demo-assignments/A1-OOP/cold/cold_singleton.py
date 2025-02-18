#! /usr/bin/env python3

"""
Solving Kattis problem - cold using Singleton pattern
https://open.kattis.com/problems/cold
"""

from __future__ import annotations

__author__ = "Ram Basnet"
__date__ = "2022/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"


from typing import Any, List
import sys
from temperature import Temperature


class Solution():
    """ Solution class to solve the problem using Singleton pattern"""

    _instance: "Solution" | None = None

    def __new__(cls) -> "Solution":
        """Creates a new instance of the class if not already created.

        Enforces Singleton pattern.

        Returns:
            Solution: class instance
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """ Constructor
        """
        self._n: int = 0  # number of temperatures
        self._data: str = ''  # data
        self._temps: List[Temperature] = []  # list of temperatures

    def find_answer(self) -> int:
        """Counts the number of temperatures below zero

        Returns:
            int: number of temperatures below zero
        """
        count = 0
        for temp in self._temps:
            if temp.is_negative():
                count += 1
        return count

    def read_data(self, source: Any) -> None:
        """ Reads data from provided source.

        Args:
            source (Any): stdin typically for kattis problem
        """
        # ignore the first line
        data = source.readlines()
        self._n = int(data[0])
        self._data = data[1].strip()
        self._temps = [Temperature(int(i)) for i in self._data.split()]

    def get_n(self) -> int:
        """Returns the number of temperature readings

        Returns:
            int: number of temperature readings
        """
        return self._n

    def get_data(self) -> str:
        """ Returns the data

        Returns:
            str: data
        """
        return self._data

    def solve(self, source: Any) -> None:
        """ Solves the problem.
        """
        self.read_data(source)
        print(self.find_answer())
        # sys.stdout.write('1')

    @staticmethod
    def main() -> None:
        """Entry static method
        """
        sol = Solution()
        sol.solve(sys.stdin)


if __name__ == "__main__":
    Solution.main()  # pragma: no cover
