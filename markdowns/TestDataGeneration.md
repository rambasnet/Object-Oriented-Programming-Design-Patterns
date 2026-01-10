# Test Data Generation

- generating good test data can be challenging
- use Hypothesis library - https://hypothesis.readthedocs.io/en/latest/index.html
- Hypothesis is a Python library for creating unit tests by automatically generating meaningful test data
    - helps create edge test cases in your code, you'd not have thought to look for
    - can use it with `pytest` and `unittest` libraries
- hypothesis provides property-based testing 
- designed to test the aspects of a data property that should always be true
- allows for a range of inputs to be programmed and tested within a single test, rather than having to write a different test (hard-coded inputs) for every value that you want to test
- let's you do **fuzz testing**
    - an automated software testing method that injects invalid, malformed, or unexpected inputs into a system to reveal software defects and security vulnerabilities 
- install hypothesis library
- more detailed examples: [https://semaphoreci.com/blog/property-based-testing-python-hypothesis-pytest](https://semaphoreci.com/blog/property-based-testing-python-hypothesis-pytest) 

```bash
pip install hypothesis
```

- see what data you can generate and how docs: [https://hypothesis.readthedocs.io/en/latest/data.html#](https://hypothesis.readthedocs.io/en/latest/data.html#)


```python
! pip install hypothesis
```


```python
def add(nums:list[int]) -> int:
    s: int = 0
    for n in nums:
        s += n
    return s
```


```python
# typical unittesting; hardcoded input provided to functions/methods provides the expected output
assert add([1, 2, 3]) == 6, '1 2 3 did NOT add to 6'
assert add([1, 3, -1, 0, -1]) == 2, '1, 3, -1, 0, -1 did NOT add to 2'
print('all tests done...')
```


```python
# see settings docs: https://hypothesis.readthedocs.io/en/latest/settings.html
from hypothesis import given, settings, Verbosity
import hypothesis.strategies as some
```


```python
# By default generates 100 random lists of integers
@given(some.lists(some.integers()))
def test_add(nums):
    print(nums) # uncomment it to see what nums are generated
    assert add(nums) == sum(nums)
```


```python
test_add()
```


```python
# more examples...
@given(some.integers(), some.integers())
# can set it to control the no. of examples, database, randomization, etc.
@settings(max_examples=100, verbosity=Verbosity.verbose, derandomize=True)
def test_ints_are_commutative(x, y):
    #print(x, y)
    assert x + y == y - x
```


```python
test_ints_are_commutative()
```


```python
# explicitly give name to data
@given(x=some.integers(), y=some.integers())
def test_ints_cancel(x, y):
    assert (x + y) - y == x
```


```python
test_ints_cancel()
```


```python
# generate lists of arbitrary length (usually between 0 and
# 100 elements) whose elements are integers.
@given(some.lists(some.integers()))
def test_reversing_twice_gives_same_list(xs):
    ys = list(xs)
    ys.reverse()
    ys.reverse()
    assert ys == xs
```


```python
test_reversing_twice_gives_same_list()
```


```python
@given(t=some.tuples(some.booleans(), some.text()))
def test_look_tuples_work_too(t):
    # A tuple is generated as the one you provided, 
    # with the corresponding types in those positions.
    assert len(t) == 2
    assert isinstance(t[0], bool)
    assert isinstance(t[1], str)
```


```python
test_look_tuples_work_too()
```


```python
# generate even numbers between 10 and 20
# use min_value and max_value or map method
@given(some.integers(min_value=5, max_value=10).map(lambda x: x*2))
def test_somefunc(num):
    print(num)
    #assert test some functions using num!
    assert num % 2 == 0
    assert 10 <= num <= 20
```


```python
test_somefunc()
```


```python
# can compose types such as list, tuple, etc...
# list with at most 100 integers with min value of 1
@given(some.lists(some.integers(min_value=1), min_size=1, max_size=50))
def test_func1(nums):
    print(nums)
    assert len(nums) >= 1 <= 50
```


```python
test_func1()
```

### Software Requirement

1. Define a function that takes an integer value between 1 and 10 as an argument
2. Function finds and returns the square root of the integer value provided
3. Function should throw AssertionError for invalid input


```python
# see settings docs: https://hypothesis.readthedocs.io/en/latest/settings.html
from hypothesis import given, settings, Verbosity
import hypothesis.strategies as some

def int_sqrt(n: int) -> float:
    # Is this the correct implementation?

    if not isinstance(n, int):
        raise AssertionError
    assert 1 <= n <= 100
    return n**0.5
```


```python
def test_int_sqrt():
    import math
    assert int_sqrt(9) == 3, 'sqrt(9) != 3'
    assert int_sqrt(4) == 2, 'sqrt(4) != 2'
    assert int_sqrt(10) == math.sqrt(10)
    #assert int_sqrt(100)
    # any problem here...?
    try:
        assert int_sqrt(100)
        assert int_sqrt("abc")
    except AssertionError:
        pass
    print('all tests PASS...')
```


```python
test_int_sqrt()
```

    all tests PASS...



```python
# Property-based testing using hypothesis
from dataclasses import dataclass
import hypothesis.strategies as st

@dataclass
class TestData:
    int_value: st.SearchStrategy[int]

# Generating correct input data range
test_data = TestData(int_value=st.integers(min_value=1, max_value=10))
```


```python
test_data
```




    TestData(int_value=integers(min_value=1, max_value=10))




```python
@given(st.data())
def test_int_sqrt(data: st.DataObject):
    import math

    an_int = data.draw(test_data.int_value)
    root = int_sqrt(an_int)
    # TODO: uncomment to see the test data
    print(an_int, root) 

    assert isinstance(an_int, int)
    assert 1 <= an_int <= 10
    assert root == math.sqrt(an_int)
    
    print('all answer correct')
```


```python
test_int_sqrt()
```

    all tests PASS...



```python
# What if you pass a string, -negative, 0, float, larger than 10 values...?

# Let's test for -ve values
@given(some.integers(min_value=-100_000, max_value=-1))
def test_int_sqrt_negative(n: int):
    # This should throw AssertionError, but does it...?
    try:
        root = int_sqrt(n)
        print(f'root of {n} is {root}')
    except AssertionError:
        # This must be printed... to pass the test
        print('AssertionError thrown... PASS')
    else:
        print('FAIL')
```


```python
test_int_sqrt_negative()
```

    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS



```python
# let's test for larger than 10 values
@given(some.integers(min_value=11, max_value=1_000_000))
def test_int_sqrt_larger_positives(n: int):
    # This should throw AssertionError, but does it...?
    try:
        #print(n)
        root = int_sqrt(n)
        print(f'root of {n} is {root}')
    except AssertionError:
        # This must be printed... to pass the test
        print('AssertionError thrown... PASS')
    else:
        print('FAIL')
```


```python
test_int_sqrt_larger_positives()
```

    root of 11 is 3.3166247903554
    FAIL
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    root of 12 is 3.4641016151377544
    FAIL
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS



```python
# let's test with float values
@given(some.floats())
def test_int_sqrt_floats(n: float):
    # This should raise AssertionError, but does it...?
    try:
        #print(n)
        root = int_sqrt(n)
        print(f'root of {n} is {root}')
    except AssertionError:
        # This must be printed... to pass the test
        print('AssertionError thrown... PASS')
    else:
        print('FAIL')
```


```python
test_int_sqrt_floats()
```

    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS
    AssertionError thrown... PASS



```python
# Let's test with some strings
@given(some.text())
def test_int_sqrt_strings(n: str):
    # This should throw AssertionError, but does it...?
    try:
        #print(n)
        root = int_sqrt(n)
        print(f'root of {n} is {root}')
    except AssertionError:
        # This must be printed... to pass the test
        print('AssertionError thrown...PASS')
    else:
        print('FAIL')
```


```python
test_int_sqrt_strings()
```

    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS
    AssertionError thrown...PASS


## Fix int_sqrt( ) so all property-based test PASS

- since all the tests use an AssertionError exception, use assert to fix various properties of the input data
    - assert num >= 1 and num <= 10
    - ...
- you could decide to throw your custom error for invalid data and assert those errors accordingly
- re-run all the property-based tests so every test PASSes

## Property-based testing demo

- see `src/unittesting/inventory` folder
    - a simple order processing and stock control system
    - burrowed from book "The Pragmatic Programmer" by David Thomas and Andrew Hunt
- two classes:
    - `Warehouse` and `Order` in two separate modules
- run several test modules provided in the order:
- if the Warehouse doesn't have enough inventory, you shouldn't be able to create an Order!
    - how do you check if the warehouse has enough inventory?
    - Hypothesis will find this bug and report it!

```bash
pytest test_order.py # no hypothesis used; doesn't find error!
pytest test_warehouse.py # no hypothesis used
pytest test_order_fail.py # <-- this property-based testing using hypothesis will find error
pytest test_order_fixed.py # use hypothesis on fixed order.py
```

- performs several property-based tests
- automatically generates test data using `hypothesis`
- finds the data that causes tests to fail
    - use the data to create the separate explicit `unittest` - which becomes your regression test
    - since the data is generated randomly, you may not guarantee the same data will be generated
- property-based tests often surprise you!

### Regression test
- focus on the subset of unit tests targeting a subset of new code/feature
- a type of software testing technique that re-runs functional and non-functional tests to ensure that a software application works as intended after any code changes, updates, revisions, improvements, or optimizations
- change int_sqrt( ) function to accept values from 0 to 100
- see if the existing test passes
    - do you need new property-based tests?


```python

```
