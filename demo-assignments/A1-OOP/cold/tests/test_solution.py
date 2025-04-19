"""Unittesting Solution class."""

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"


import unittest
import os
from unittest.mock import patch
from io import StringIO
from cold import Solution


class TestSolution(unittest.TestCase):
    """
    Unittesting Solution class
    """

    def setUp(self) -> None:
        """ Setup method - called before each test"""
        self.sol = Solution()
        dir_name = os.path.dirname(os.path.abspath(__file__))
        file_1 = os.path.join(dir_name, '../data/1.in')
        self.input1 = open(file_1, 'r', encoding='utf-8')
        file_2 = os.path.join(dir_name, '../data/2.in')
        print(f'{file_1=}')
        self.input2 = open(file_2, 'r', encoding='utf-8')

    def tearDown(self) -> None:
        """ Tear down method - called after each test"""
        self.input1.close()
        self.input2.close()
        return super().tearDown()

    def test_read_data1(self) -> None:
        """Tests readData method"""
        self.sol.read_data(self.input1)
        self.assertEqual(self.sol.n, 3)
        self.assertEqual(self.sol.data, '5 -10 15')

    def test_read_data2(self) -> None:
        """
        Tests readData method
        :return: None
        """
        self.sol.read_data(self.input2)
        self.assertEqual(self.sol.n, 5)
        self.assertEqual(self.sol.data, '-14 -5 -39 -5 -7')

    def test_find_answer1(self) -> None:
        """Tests findAnswer method"""
        self.sol.read_data(self.input1)
        expected = self.sol.find_answer()
        self.assertEqual(expected, 1)

    def test_find_answer2(self) -> None:
        """Tests findAnswer method"""
        self.sol.read_data(self.input2)
        expected = self.sol.find_answer()
        self.assertEqual(expected, 5)

    # @patch('sys.stdout', new_callable=StringIO)
    # @patch('sys.stderr', new_callable=StringIO)
    def test_solve1(self) -> None:
        """ Tests solve method - using patch context manager
        - tests 1.in
        """
        # self.sol.solve()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.sol.solve(self.input1)
            self.assertEqual(mock_stdout.getvalue(), '1\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_solve2(self, mock_stdout: StringIO) -> None:
        """Tests solve method - using patch decorator
        - tests 2.in
        """
        self.sol.solve(self.input2)
        self.assertEqual(mock_stdout.getvalue(), '5\n')

    def test_singleton(self) -> None:
        """Tests singleton pattern"""
        a = Solution()
        b = Solution()
        self.assertIs(a, b)

    def test_read_data(self) -> None:
        """Test read_data method using StrionIO input
        """
        a = Solution()
        a.read_data(StringIO("3\n5 -10 15\n"))
        self.assertEqual(a.n, 3)

    def test_find_answer(self) -> None:
        """Test find_answer method
        """
        a = Solution()
        a.read_data(StringIO("3\n5 -10 15\n"))
        expected = a.find_answer()
        assert expected == 1

    def test_get_data3(self) -> None:
        """Test data property
        """
        a = Solution()
        a.read_data(StringIO("3\n5 -10 15\n"))
        assert a.data == "5 -10 15"

    def test_solve(self) -> None:
        """Test solve method
        """
        a = Solution()
        a.solve(StringIO("3\n5 -10 15\n"))
        # we'll learn how to patch the stdout later
        # for now we'll just check the answer
        assert a.find_answer() == 1
