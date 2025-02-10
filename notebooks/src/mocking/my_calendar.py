""" A module for dealing with calendars.
"""

from datetime import datetime
from typing import Any
import requests


def is_weekday() -> bool:
    """Return True if today is a weekday, False otherwise.

    Returns:
        bool: True if today is a weekday, False otherwise
    """
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    # print('today = ', today)
    return 0 <= today.weekday() < 5


def get_holidays() -> Any:
    """Get the upcoming holidays.

    Returns:
        Any: The upcoming holidays
    """
    r = requests.get('http://localhost/api/holidays', timeout=2)
    if r.status_code == 200:
        return r.json()
    return None
