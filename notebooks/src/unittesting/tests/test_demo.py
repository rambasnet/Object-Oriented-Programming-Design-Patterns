"""Unittest demo.
"""
import unittest


class TestValues(unittest.TestCase):
    """Test the values.
    """

    def test_int_float(self) -> None:
        """Test int and float.
        """
        self.assertEqual(1, 1.0)

    def test_int_string(self) -> None:
        """Test int and string."""
        self.assertEqual(1, "1")

    def test_int_bool(self) -> None:
        """Test int and bool."""
        self.assertEqual(1, True)

    def test_float_string(self) -> None:
        """Test float and string."""
        self.assertNotEqual(1.0, "1.0")

    def test_float_bool(self) -> None:
        """Test float and bool."""
        self.assertEqual(1.0, True)

    def test_int_string2(self) -> None:
        """ Test int and string2."""
        self.assertNotEqual(1, "1")

    def test_float_float(self) -> None:
        """ Test float and float."""
        self.assertEqual(1.0, 1.00001)

    def test_float_float1(self) -> None:
        """ Test float and float1."""
        self.assertAlmostEqual(2.0, 1.000001, 3)

    def test_assert_true(self) -> None:
        """Test assert true."""
        self.assertTrue(True)

    def test_assert_false(self) -> None:
        """Test assert false."""
        self.assertFalse(False)

    def test_assert_none(self) -> None:
        """Test assert none."""
        self.assertIsNone(None)

    def test_assert_is(self) -> None:
        """Test assert is."""
        self.assertIs(True, True)

    def test_assert_raises(self) -> None:
        """Test assert raises."""
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

    def test_assert_raises1(self) -> None:
        """Test assert raises1."""
        with self.assertRaises(TypeError):
            _ = 1 + "5"
