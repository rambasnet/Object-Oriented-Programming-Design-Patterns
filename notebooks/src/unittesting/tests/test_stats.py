"""
NOTE:
Run pytest from the command line.
Can't run this module as main module due to import of stats
from parent folder which is not a package
"""

import unittest
from .stats import StatsList


class TestValidInputs(unittest.TestCase):
    """Test the StatsList class."""

    def setUp(self) -> None:
        """Create a StatsList with valid inputs.
        """
        self.stats = StatsList([1, 2, 2, 3, 3, None, 4])

    def test_mean(self) -> None:
        """Test the mean method.
        """
        self.assertEqual(self.stats.mean(), 2.5)

    def test_median(self) -> None:
        """Test the median method.
        """
        self.assertEqual(self.stats.median(), 2.5)
        self.stats.append(4)
        self.assertEqual(self.stats.median(), 3)

    def test_mode(self) -> None:
        """Test the mode method.
        """
        self.assertEqual(self.stats.mode(), [2, 3])
        self.stats.remove(2)
        self.assertEqual(self.stats.mode(), [3])
