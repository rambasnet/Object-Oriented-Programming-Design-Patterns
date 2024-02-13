from datetime import datetime
import unittest
from unittest.mock import patch
from my_calendar import is_weekday

class TestCalendar(unittest.TestCase):
	# testing with a patch decorator
	@patch('my_calendar.datetime')
	def test_is_weekday(self, mock_datetime) -> None:
		tuesday = datetime(year=2023, month=1, day=3)
		mock_datetime.today.return_value = tuesday # Tuesday
		self.assertTrue(is_weekday())
		mock_datetime.today.assert_called_once()

	# testing with a patch context manager
	def test_is_weekday1(self) -> None:
		with patch('my_calendar.datetime') as mock_datetime:
			tuesday = datetime(year=2023, month=1, day=3)
			mock_datetime.today.return_value = tuesday
			self.assertTrue(is_weekday())
			mock_datetime.today.assert_called_once()

	# testing with a patch decorator
	@patch('my_calendar.datetime')
	def test_is_weekday_false(self, mock_datetime) -> None:
		saturday = datetime(year=2023, month=1, day=7)
		mock_datetime.today.return_value = saturday
		self.assertFalse(is_weekday())
		mock_datetime.today.assert_called_once()

	# testing with a patch context manager
	def test_is_weekday_false1(self) -> None:
		with patch('my_calendar.datetime') as mock_datetime:
			saturday = datetime(year=2023, month=1, day=7)
			mock_datetime.today.return_value = saturday
			self.assertFalse(is_weekday())
			mock_datetime.today.assert_called_once()
			self.assertEqual(mock_datetime.today().year, 2023)
			self.assertEqual(mock_datetime.today().month, 1)
			self.assertEqual(mock_datetime.today().day, 7)

if __name__ == '__main__':
	unittest.main(verbosity=2)
