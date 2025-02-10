"""Unit tests for the singleton solution.
"""

__author__ = "Ram Basnet"
__date__ = "2025/02/10"
__license__ = "MIT"
__version__ = "0.1.0"


from io import StringIO
from cold_singleton import Solution


def test_singleton() -> None:
    """Test if the solution is a singleton.
    """
    a = Solution()
    b = Solution()
    assert a is b


def test_find_answer() -> None:
    """Test find_answer method
    """
    a = Solution()
    a.read_data(StringIO("3\n5 -10 15\n"))
    expected = a.find_answer()
    assert expected == 1


def test_read_data() -> None:
    """ Test read_data method
    """
    a = Solution()
    a.read_data(StringIO("3\n5 -10 15\n"))
    assert a.get_n() == 3


def test_get_data() -> None:
    """Test get_data method
    """
    a = Solution()
    a.read_data(StringIO("3\n5 -10 15\n"))
    assert a.get_data() == "5 -10 15"


def test_solve() -> None:
    """Test solve method
    """
    a = Solution()
    a.solve(StringIO("3\n5 -10 15\n"))
    # we'll learn how to patch the stdout later
    # for now we'll just check the answer
    assert a.find_answer() == 1
