""" Temperature class to represent a temperature"""

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

from typing import Any


class Temperature(object):
    """
    Represents a temperature
    """

    def __init__(self, temp: int, unit: str = 'F') -> None:
        """
        initializes a temperature
        :param temp: temperature
        """
        self._temp: int = temp
        self._unit: str = unit

    @property
    def temp(self) -> int:
        """
        returns the temperature
        :return: _temp
        """
        return self._temp

    @temp.setter
    def temp(self, temp: int) -> None:
        """
        sets the temperature
        :param temp: temperature
        """
        self._temp = temp

    @property
    def unit(self) -> str:
        """
        Property to get/set unit of temperature
        Returns:
                        str: unit
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str) -> None:
        self._unit = unit

    def is_negative(self) -> bool:
        """Checks if the _temp is negative

        Returns:
            bool: True if _temp is < 0; False otherwise
        """
        return self._temp < 0

    def __str__(self) -> str:
        """Retuns the string representation.

        Returns:
            str: string represention to print.
        """
        return f'{self._temp} {self.unit}'

    def __repr__(self) -> str:
        """Returns string representation of object.

        Returns:
            str: string representation.
        """
        return f'{self._temp} {self.unit}'

    def __lt__(self, other: 'Temperature') -> bool:
        """Less than comparison.

        Args:
            other (Temperature): the other object to compare with

        Returns:
            bool: True if this temperature is less than the other.
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._temp < other._temp

    def __gt__(self, other: 'Temperature') -> bool:
        """Greater than comparision.

        Args:
            other (Temperature): the other object to compare with

        Returns:
            bool: True if this temperature is greater than the other.
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._temp > other._temp

    def __eq__(self, other: Any) -> bool:
        """Equal comparision.

        Args:
            other (Any): other object to compare with.

        Returns:
            bool: True if this object is equal to the other
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._temp == other._temp

    def __le__(self, other: 'Temperature') -> bool:
        """Less than or equal to comparison

        Args:
            other (Temperature): Other object to compare with.

        Returns:
            bool: True if this temp is less than or equal to the other.
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._temp <= other._temp

    def __ge__(self, other: 'Temperature') -> bool:
        """Greater than or equal to comparision.

        Args:
            other (Temperature): Other object to compare with.

        Returns:
            bool: True if this object is greater than the other.
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._temp >= other._temp
