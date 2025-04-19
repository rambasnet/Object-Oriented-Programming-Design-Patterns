"""
Unittesting HelloWorld class
"""

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"


import unittest
from unittest.mock import patch
from io import StringIO
from helloworld import HelloWorld


class TestHelloWorld(unittest.TestCase):
    """
    Unittesting HelloWorld class
    """

    def setUp(self) -> None:
        """Setup method
        """
        self.hello = HelloWorld()

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_message(self, mock_stdout: StringIO) -> None:
        """Tests printMessage method
        """
        self.hello.print_message()
        self.assertEqual(mock_stdout.getvalue(), 'Hello World!\n')

    def test_message(self) -> None:
        """Test message property
        """
        self.assertEqual(self.hello.message, 'Hello World!')
