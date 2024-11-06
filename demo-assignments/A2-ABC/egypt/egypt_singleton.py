"""Egyp problem solution using ABC and Singleton pattern.
"""

from __future__ import annotations
import sys
from typing import Any, List
from triangle import Triangle
from kattis import Kattis


class Solution(Kattis):
    """Solution class to solve the problem
       Uses Singleton pattern and Kattis ABC class
    """
    _instance = None

    def __init__(self, input_source: Any = sys.stdin) -> None:
        """Constructor
        """
        if Solution._instance:
            raise NameError(
                "Cannot create multiple instances of \
                a singleton class Solution")

        super().__init__(input_source)
        self._instance = self
        # self._input_source: Any = input_source
        self._data: List[List[int]] = []
        self._triangles: List[Triangle] = []
        self._answer: List[str] = []
        self.read_input()

    @classmethod
    def get_instance(cls) -> Solution:
        """Returns the instance of the class

        Returns:
            Solution: class instance
        """
        if cls._instance is None:
            cls._instance = Solution()
        return cls._instance

    def read_input(self) -> None:
        """Reads the data from the given source.

        Args:
            input_source (Any): input source
        """
        data = self._input_source.readlines()
        # ignore the last line: 0, 0, 0
        self._data = [list(map(int, data[i].split()))
                      for i in range(len(data) - 1)]
        for a, b, c in self._data:
            self._triangles.append(Triangle(a, b, c))

    @property
    def data(self) -> List[List[int]]:
        """Data property

        Returns:
            List[List[int]]: data
        """
        return self._data

    @property
    def answer(self) -> str:
        """Creates the answer string

        Returns:
            str: answer
        """
        return '\n'.join([str(t) for t in self._answer])

    def solve(self) -> None:
        """
        Solves the problem
        """
        for t in self._triangles:
            self._answer.append(
                'right' if t.is_right_angled() else 'wrong')

        self._answer.append('')

    def print_answer(self) -> None:
        """
        Prints the answer
        """
        sys.stdout.write(self.answer)

    @staticmethod
    def main() -> None:
        """Main function to run the solution
        """
        solution = Solution(sys.stdin)
        solution.solve()
        solution.print_answer()


if __name__ == '__main__':
    Solution.main()  # pragma: no cover
