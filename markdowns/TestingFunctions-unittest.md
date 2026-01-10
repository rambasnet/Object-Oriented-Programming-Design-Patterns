# Testing Functions and Programs

## Topics

- the importance of unit testing
- Test-driven development
- the `unittest` package and `mock` module
- the `pytest` tool
- code coverage

## Why test?

- programmers must know the importance of testing
- strongly and statically typed languages (C++, Java) are usually safer 
    - type checking is done during compile time
- testing is more important in Python
    - Python checks for data/values, not types; i.e., during runtime
- *Software features that can't be demonstrated by automated tests simply don't exist* - Kent Beck
- four main reasons to write tests:
    1. to ensure that code is working the way the developer thinks it should
    2. to ensure that the code continues working when we make changes
    3. to ensure that the developer understood the requirements
    4. to ensure that the code we are writing has a maintainable interface

## Tips
#### Test Early, Test Often, Test Automatically
#### Coding Ain't Done 'Till All the Tests Run
#### Find Bugs Once
#### Test State Coverage, Not Just Code Coverage
#### Don't Use Manual Procedures; Automate Everything!
#### Delight Users, Don't Just Deliver Code
#### Sign Your Work

## Anatomy of Test

- [https://docs.pytest.org/en/8.0.x/explanation/anatomy.html#test-anatomy]
- You can think of a test as being broken down into four steps:

### Arrange

- we prepare everything for our test
- lineup all the dominos; generate controlled input data

### Act

- the singular, state-changing action that kicks off the behavior we want to test

### Assert

- look at the resulting state and check if it looks how we’d expect after the dust has settled

### Cleanup

- cleanup so other tests aren’t being accidentally influenced by the current test

## Test-driven development
- mantra: write tests first
- tests you'll write later, will **NEVER** be written!
- can be fun; allows us to build little puzzles to solve
- then, we implement the code to solve those puzzles
- two goals:
    1. ensures that tests **really** get written
    2. forces us to consider how the code will be used
- helps us to break up the initial problem into smaller, testable problems
- combine the tested solutions into larger, also tested, solutions

## Testing objectives

- goals/objectives of running tests that lead to different kinds of testing
- for other testing types see: https://www.softwaretestinghelp.com/
- if you do thorough testing, you may end up lot more testing code than production code!

### Unit testing

- the foundation of all the other forms of testing
    - Integration testing, validation, and verification, performance/stress testing, testing the tests
- confirm that software components work in isolation
- Fowler's Test Pyramid seems to suggest unit testing creates the most value - https://martinfowler.com/articles/practical-test-pyramid.html
- unit can be a function, method, class, or a whole module
- if the basic/unit components are tested well, there'll be few surprises when they're integrated
- common to use **coverage** tool to be sure all the lines of code are exercised as part of the unit test suite

### Integration testing

- confirm software components work when integrated
    - make sure the major subsystems of the project work and play well with each other
- also called system tests, functional tests, and acceptance tests among others
- when integration test fails, it often means an interface wasn't defined properly
- perhaps unit tests didn't include some edge cases

### Validation and Verification

- a bug-free system that answers the wrong question isn't very useful!
- as soon as the project has an executable user interface or prototype, verify with the user if it is what they need.
- does it meet the functional requirements?

### Performance testing

- does the software product meet the real-world performance requirements?
    - number of users, connections, or transactions per second
    - is it scalable?


## Testing patterns

- there are many software design patterns
- testing is simple and essentially uses the same pattern for all software design patterns

```
GIVEN some precondition(s) for a scenario
WHEN we exercise some method of a class 
THEN some state change(s) or side effect will occur that we can confirm
````

- use the three-part pattern to disentangle the **setup, execution, and expected results**
- e.g, testing if the water is hot enough for a cup of tea
    1. GIVEN a kettle of water on the stove
    2. AND the burner is off
    3. WHEN we flip the lid on the kettle
    4. THEN we see steam escaping

### Test cases

- how many test cases to write and what data should be picked for testing can be challenging
- some techniques that can be used to design test cases are **equivalence partitioning** and **boundary value analysis**
- see this article for details: https://www.softwaretestinghelp.com/what-is-boundary-value-analysis-and-equivalence-partitioning/
- let's say the input text boxes should only accept the value between 1-1000 inclusively
- testing all possible values from 1-1000 is not plausible and in many cases not feasible
    - also don't gain anything valuable with exhaustive testing

#### Equivalence partitioning

1. test one value from a valid range: 1-1000
2. test one value from an invalid range smaller than the minimum value (1)
3. test one value from an invalid range larger than the maximum value (1000)

#### Boundary value analysis

1. test the boundary values: 1 and 1000
2. test data just below the extreme values: 0 and 999
3. test data just above the extreme values: 2 and 1001


### Example of Test Driven Development (TDD)

- write a function that finds the average of a list of numbers
- input assumptions:
    - input is a list of integers
    - list can be empty
    - list may contain None for missing values
- output assumptions:
    - output is a float
    - if the list is empty or contains only None throw DivisionByZeroError exception
    - answer should be correct to 7 decimal places


```python
from typing import Optional, List

def average(data: List[Optional[int]]) -> float:
    """
    GIVEN a list, data = [1, 2, None, 3, 4]
    WHEN we compute m = average(data)
    THEN the result, m is 2.5
    
    Finds and returns average of a List of optional integers.
    
    Assumptions:
        - Ignore None.
        - Throw ZeroDivisionError if data is an empty list.
    """
```


```python
# test cases for the average function
def test_average1():
    ans = average([1, 2, 3, 4])
    expected = 2.5
    assert ans == expected
```


```python
def test_average2():
    data = [1, 2, None, 3, 4]
    assert average(data) == 2.5
```


```python
def test_average3():
    assert average([1, 1, 1, 1, None]) == 1.0
```


```python
def test_average4():
    try:
        average([])
    except ZeroDivisionError:
        pass
```


```python
def test_average5():
    assert average([-1, -2, None, 1, 2]) == 0
```


```python
def test_average6():
    # float literal comparison or code comparison
    # float literal comparison may require tolerance (error less than 0.0001 or 10^-4, e.g.)
    # average([1, 3, 4]) = 2.6666666666666665...
    assert abs(average([1, 3, 4]) - 2.6666666) < 10**-7
```


```python
def test_average7():
    #assert average([None, None, None, None]) == ????
    pass
```


```python
def run_all_tests():
    test_average1()
    test_average2()
    test_average3()
    test_average4()
    test_average5()
    test_average6()
    test_average7()
```


```python
run_all_tests()
```

## Implement average( )

- implement average function and run the tests functions again!
- use built-in `filter` function or write your own filter to exclude None values
    - `filter(None, lst_object)`

## Unit testing with unittest library

- Python provides built-in unittest library
- provides a common object-oriented interface for writing unit tests
- `import unittest`
- create a subclass inheriting from TestCase
- every test case method must start with the prefix **test_**


```python
import unittest

class TestAverage(unittest.TestCase):
    def test_average1(self):
        ans = average([1, 2, 3, 4])
        expected = 2.5
        #assert ans == expected
        # better
        self.assertEqual(ans, expected, f'{ans} != {expected}')

    # implement test_average2
```

## More unittest examples

- see `src/unittesting/test_demo.py`
```
python test_demo.py
pytest
python -m pytest
```

- special methods `setUp()` and `tearDown()` are called before and after each test case is executed
    - see `src/unittesting/tests/test_setup_teardown.py` for example
- for more detailed example, see `src/unittesting/stats.py` and `src/unittesting/tests/` folder

## Pytest

- pytest framework executes the tests written using unittest library
- pytest can discover all the test modules that are named `test_*.py`
- pytest can discover all the test classes that are named `Test*` and test methods that are named `test_*()`
- pytest can be executed for a single file, or all the files and subfolders within a folder
- provides advanced contexts called fixtures - [https://docs.pytest.org/en/8.0.x/explanation/fixtures.html](https://docs.pytest.org/en/8.0.x/explanation/fixtures.html)
- fixtures are similar to unittest setUp() and tearDown() methods that lets your create data for testing

## Exercises

- Solve the following Kattis problem using OOD
- must use unittest with adequate number of testcases to test important class methods/interfaces

1. Dog & Gopher - https://open.kattis.com/problems/doggopher
2. Morse Code Palindromes - https://open.kattis.com/problems/morsecodepalindromes




```python

```
