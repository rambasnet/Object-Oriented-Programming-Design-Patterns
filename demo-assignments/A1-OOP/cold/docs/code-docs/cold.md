Module cold
===========
Kattis problem - cold
https://open.kattis.com/problems/cold

Classes
-------

`Solution()`
:   Solution class to solve the problem
    
    Constructor

    ### Static methods

    `main() ‑> None`
    :   Entry static method

    ### Methods

    `find_answer(self) ‑> int`
    :   Counts the number of temperatures below zero
        
        Returns:
            int: number of temperatures below zero

    `get_data(self) ‑> str`
    :   Returns the data
        
        Returns:
            str: data

    `get_n(self) ‑> int`
    :   Returns the number of temperature readings
        
        Returns:
            int: number of temperature readings

    `read_data(self, source: Any) ‑> None`
    :   Reads data from provided source.
        
        Args:
            source (Any): stdin typically for kattis problem

    `solve(self, source: Any) ‑> None`
    :   Solves the problem.