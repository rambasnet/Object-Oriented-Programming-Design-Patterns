Module temperature
==================
Temperature class to represent a temperature

Classes
-------

`Temperature(temp: int, unit: str = 'F')`
:   Represents a temperature
    
    Constructor
    
    Args:
        temp (int): temperature
        unit (str, optional): temperature unit.
            Defaults to 'F' for Fahrenheit.

    ### Instance variables

    `temp: int`
    :   Property to get temperature
        
        Returns:
            int: temperature

    `unit: str`
    :   Property to get/set unit of temperature
        Returns:
            str: unit

    ### Methods

    `is_negative(self) ‑> bool`
    :   Checks if the _temp is negative
        
        Returns:
            bool: True if _temp is < 0; False otherwise