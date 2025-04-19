"""
Testing Solution class
"""

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"


import unittest
from unittest.mock import patch
from io import StringIO
from hello import Solution


class TestSolution(unittest.TestCase):
    """
    Testing Singleton Solution class
    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_solve(self, mock_stdout: StringIO) -> None:
        """
        Tests solve method
        """
        my_main: 'Solution' = Solution.get_instance()
        my_main.solve()
        self.assertEqual(mock_stdout.getvalue(), 'Hello World!\n')

    def test_get_instance(self) -> None:
        """
        Tests get_instance method
        """
        my_main: 'Solution' = Solution.get_instance()
        self.assertIs(my_main.get_instance(), my_main)

    def test_exeception(self) -> None:
        """
        Tests exception with multiple instances
        """
        _ = Solution.get_instance()
        self.assertRaises(NameError, Solution)

    def test_main_static(self) -> None:
        """
        Tests main staticmethod
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # call the static method
            Solution.main()
            self.assertEqual(mock_stdout.getvalue(), 'Hello World!\n')
