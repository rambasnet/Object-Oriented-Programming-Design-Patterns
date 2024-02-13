import unittest
from requests.exceptions import Timeout
from unittest.mock import Mock

requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestHolidays(unittest.TestCase):
	def test_get_holidays_timeout(self) -> None:
		# test a connection timeout
		requests.get.side_effect = Timeout
		#holidays = get_holidays()
		with self.assertRaises(Timeout):
			get_holidays()

	def test_get_holidays_data(self) -> None:
		response_mock = Mock()
		response_mock.status_code = 200
		response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
		requests.get.side_effect = [response_mock]
		data = get_holidays()
		print('data', data)
		self.assertEqual(data['12/25'], 'Christmas')
		self.assertEqual(data['7/4'], 'Independence Day')

	def test_both(self) -> None:
		response_mock = Mock()
		response_mock.status_code = 200
		response_mock.json.return_value = {
						'12/25': 'Christmas',
						'7/4': 'Independence Day',
				}
		requests.get.side_effect = [Timeout, response_mock]
		with self.assertRaises(Timeout):
			get_holidays()
		data = get_holidays()
		print('data', data)
		self.assertEqual(data['12/25'], 'Christmas')
		self.assertEqual(data['7/4'], 'Independence Day')

if __name__ == '__main__':
	unittest.main(verbosity=2)
