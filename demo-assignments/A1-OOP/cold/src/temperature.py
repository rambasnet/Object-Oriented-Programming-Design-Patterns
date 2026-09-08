""" Temperature class to represent a temperature.
"""

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"


class Temperature:
    """ Represents a temperature
    """

    def __init__(self, temp: int, unit: str = 'F') -> None:
        """ Constructor

        Args:
            temp (int): temperature
            unit (str, optional): temperature unit.
                Defaults to 'F' for Fahrenheit.
        """
        self._temp: int = temp
        self._unit: str = unit

    @property
    def temp(self) -> int:
        """ Property to get temperature

        Returns:
            int: temperature
        """
        return self._temp

    @temp.setter
    def temp(self, temp: int) -> None:
        """ Property to set temperature

        Args:
            temp (int): temperature
        """
        self._temp = temp

    @property
    def unit(self) -> str:
        """ Property to get/set unit of temperature
        Returns:
            str: unit
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str) -> None:
        self._unit = unit

    def is_negative(self) -> bool:
        """ Checks if the _temp is negative

        Returns:
            bool: True if _temp is < 0; False otherwise
        """
        return self._temp < 0

    def __str__(self) -> str:
        """ Returns the string representation.

        Returns:
            str: string representation for printing.
        """
        return f'{self._temp} {self.unit}'

    def __repr__(self) -> str:
        """ Overloading string representation of the object.

        Returns:
            str: string representation.
        """
        return f'{self._temp} {self.unit}'

    def __lt__(self, other: 'Temperature') -> bool:
        """ Overloading less than comparison.

        Args:
            other (Temperature): the other object to compare with

        Returns:
            bool: True if this temperature is less than the other.
        """
        return self._temp < other.temp

    def __gt__(self, other: 'Temperature') -> bool:
        """ Overloading greater-than comparison.

        Args:
            other (Temperature): the other object to compare with

        Returns:
            bool: True if this temperature is greater than the other
        """
        return self._temp > other.temp

    def __eq__(self, other: object) -> bool:
        """ Overloading equal comparison.

        Args:
            other (Temperature): other object to compare with.

        Returns:
            bool: True if this object is equal to the other
        """
        if not isinstance(other, Temperature):
            raise NotImplementedError
        return self._temp == other.temp

    def __le__(self, other: 'Temperature') -> bool:
        """ Overloadign less-than or equal-to comparison

        Args:
            other (Temperature): Other object to compare with.

        Returns:
            bool: True if this temp is less than or equal to the other.
        """
        return self._temp <= other.temp

    def __ge__(self, other: 'Temperature') -> bool:
        """ Overloading greater-than or equal to comparison.

        Args:
            other (Temperature): Other object to compare with.

        Returns:
            bool: True if this object is greater than the other.
        """
        return self._temp >= other.temp
