""" Test setup and teardown methods in unittest.
"""
import unittest


class TestValues(unittest.TestCase):
    """ Test the values."""

    def setUp(self) -> None:
        """ Set up the test."""
        print("setUp")
        return super().setUp()

    def tearDown(self) -> None:
        """ Tear down the test."""
        print("tearDown")
        return super().tearDown()

    def test_int_float(self) -> None:
        """ Test int and float."""
        print("test_int_float")
        self.assertEqual(1, 1.0)

    def test_int_string(self) -> None:
        """ Test int and string."""
        print("test_int_string")
        self.assertNotEqual(1, "1")

    def test_int_bool(self) -> None:
        """ Test int and bool."""
        print("test_int_bool")
        self.assertEqual(1, True)
