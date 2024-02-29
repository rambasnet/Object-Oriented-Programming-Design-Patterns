"""Demonstrates the use of the patch decorator and patch context manager.
"""
import unittest
from unittest.mock import patch, Mock
from requests.exceptions import Timeout
from typing import Any
from my_calendar import get_holidays


class TestHolidays(unittest.TestCase):
    """Test cases for get_holidays function.
    """

    @patch('my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests: Any) -> None:
        """
        Test get_holidays function with a connection timeout."""
        # test a connection timeout
        mock_requests.get.side_effect = Timeout
        # holidays = get_holidays()
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()
            mock_requests.get.assert_called_once_with(
                'http://localhost/api/holidays')

    # testing with a patch context manager
    def test_get_holidays_timeout1(self) -> None:
        with patch('my_calendar.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()
                mock_requests.get.assert_called_once_with(
                    'http://localhost/api/holidays')

    @patch('my_calendar.requests')
    def test_get_holidays_data(self, mock_requests) -> None:
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        mock_requests.get.side_effect = [response_mock]
        data = get_holidays()
        self.assertEqual(data['12/25'], 'Christmas')
        self.assertEqual(data['7/4'], 'Independence Day')

    def test_get_holidays_data1(self) -> None:
        with patch('my_calendar.requests') as mock_requests:
            response_mock = Mock()
            response_mock.status_code = 200
            response_mock.json.return_value = {
                '12/25': 'Christmas',
                '7/4': 'Independence Day',
            }
            mock_requests.get.side_effect = [response_mock]
            data = get_holidays()
            self.assertEqual(data['12/25'], 'Christmas')
            self.assertEqual(data['7/4'], 'Independence Day')


if __name__ == '__main__':
    unittest.main(verbosity=2)
