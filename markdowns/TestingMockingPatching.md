# Mocking and Patching Objects for Testing

### Topics

- the motivation behind mocking/facking/patching objects
- What is a Magic Mock?
- use Mock to imitate objects in your tests
- check usage data to understand how you use your objects
- customize your mock objects' return values and side effects
- patch() objects throughout your codebase
- common mock problems and avoiding them

## Motivation

- isolated problems are easier to diagnose and solve
- if a test fails, diagnosing/debugging many interrelated components can be very difficult
    - e.g., why the engine of a gasoline car not firing
- we often want to isolate items and testing environments by providing simplified imitations (facking real objects)
- two reasons to replace actual code/API with imitation or **mock/fake** objects
    1. isolate a unit under test - create collaborating classes and functions so we can test one unknown component
    2. test code that requires an object that is either expensive or risky to use;
       - things like shared databases, filesystems, and cloud infrastructures can be very expensive to setup and tear down for testing

### Problems

- two immediate problems we've been facing when solving Kattis problems are:
1. how to programmatically assert what result the function printed to standard output?
2. how to automate data from standard input with out manually entering the input?


```python
# Quick demo of patching stdout object to write to a file
# instead of the console.
from sys import stdout
```


```python
# by default, stdout is a file object that writes to the console
stdout.write('Hello World!\n')
```


```python
save_stdout = stdout # save the original stdout object
stdout = open('log.txt', 'w')
stdout.write('This is a log file\n')
stdout.close()
```


```python
! cat log.txt
```


```python
stdout = save_stdout # restore the original stdout object
stdout.write('Back to the console\n')
```


```python
def print():
    x = input('enter')
```


```python
x = print()
```

## Imitating objects using Mocks

- based on: [https://realpython.com/python-mock-library/](https://realpython.com/python-mock-library/) and [https://docs.python.org/3/library/unittest.mock.html](https://docs.python.org/3/library/unittest.mock.html)
- `unittest.mock` module provides Mock base class for mocking objects
- you can pass mock objects as arguments to functions
- assign/patch other objects
- when substituting an object in your code, the Mock must look like the real object it is replacing
    - mock objects must have the same members (attributes and methods) that are being tested
    - e.g., if you're mocking `json` library and your program calls `dumps()`, then the mock object must also contain `dumps()` 
- Mock must simulate any object that it replaces
    - Mock creates attributes/members when you access them dynamically!
- Mock methods can take whatever arguments you provide but always return Mock object


```python
from unittest.mock import Mock
```


```python
help(Mock)
```


```python
mock = Mock()
```


```python
mock
```


```python
mock.some_attribute
```


```python
mock.do_something()
# mock methods return Mock object
```


```python
# let's use this Hello class to use some mocking/patching concepts
class Hello(object):
    def __init__(self, msg="Hello there") -> None:
        self.__msg = msg
        
    def greet(self) -> str:
        return self.__msg
    
    def other_method(self) -> str:
        # 
        return "Other method called"
```


```python
hi = Hello()
```


```python
print(hi.greet())
```


```python
mock_hi = Mock()
```


```python
# returns a Mock object by default
mock_hi.greet()
```


```python
mock_hi.greet.return_value = 'Hello there'
```


```python
print(mock_hi.greet())
```


```python
type(mock_hi)
```


```python
type(mock_hi.greet)
```


```python
assert mock_hi.greet() == 'Hello there'
```


```python
mock_hi.greet.assert_called()
```


```python
mock_hi.greet.call_count
```


```python
mock_hi.__msg = 'Hi there'
```


```python
# greet() doesn't return __msg attribute
mock_hi.greet()
```


```python
mock_hi.__msg
```


```python
# let's see the Python std JSON library
import json
```


```python
help(json)
```


```python
# dump requires two positional arguments - see '*' in dump definition
data = json.dump()
```


```python
# Patching JSON object
json = Mock()
```


```python
json.dump()
# takes any or no arguments; returns Mock object
```

### Assertions and Inspection

- Mock instances store data on how you used them
    - e.g., if you called a method, the instance stores information on how you called the method, how many times, and so on...
- examples of how to use this information


```python
from unittest.mock import Mock
```


```python
# create a mock object
json = Mock()
```


```python
json.loads('{"key": "value"}')
```


```python
# we know that we called loads() 
# so we can make assertions to test that expectation
json.loads.assert_called()
```


```python
json.loads.assert_called_once()
```


```python
json.loads.assert_called_with('{"key": "value"}')
```


```python
# this will raise an AssertionError
json.loads.assert_called_with('{"key1": "value1"}')
```


```python
json.loads.assert_called_once_with('{"key": "value"}')
```


```python
json.loads('{"key": "value"}')
```


```python
json.loads.assert_called_once()
```


```python
json.loads.assert_not_called()
```

### Mock special attributes

- Mock objects have several special attributes, e.g.:
- `call_count`
- `call_args`
- `method_calls`
- helps you understand how your application used an object


```python
from unittest.mock import Mock
```


```python
json = Mock()
```


```python
json.loads('{"key": "value"}')
```


```python
json.loads('{"key1": "value1"}')
```


```python
# number of times you called loads
json.loads.call_count
```


```python
# the last loads call
json.loads.call_args
```


```python
# list of calls to json's methods (recursively)
json.method_calls
```

### Managing a Mock's return value

- mocks let you control your code's behavior during tests
- one important aspect of the testing is to control object's behavior (methods) and their return values
- e.g., write a function that determines whether today is a weekday
    - depending on what day the test is run, you may get different results from your `calendar` utility
- you can mock `datetime` and set the `.return_value` for `.today()` to a day that you choose


```python
from datetime import datetime
```


```python
datetime.today()
```


```python
def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5

```


```python
# Test if today is a weekday
assert is_weekday()
# if you run the test on weekend, you'll get an AssertionError
```


```python
# pick couple of days from the past!
tuesday = datetime(year=2023, month=1, day=3)
saturday = datetime(year=2023, month=1, day=7)
```


```python
# Mock datetime to control today's date
datetime = Mock()
```


```python
def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return 0 <= today.weekday() < 5
```


```python
is_weekday()
```


```python
# Mock .today() to return Tuesday
datetime.today.return_value = tuesday
```


```python
datetime.today.return_value
```


```python
datetime.today().day
```


```python
datetime.today().month
```


```python
datetime.today().weekday() # Tuesday is 1
```


```python
# Test tuesday is a weekday
assert is_weekday()
```


```python
# Mock .today() to return Saturday
datetime.today.return_value = saturday
```


```python
# Test Saturday is not a weekday
assert is_weekday()
```


```python
# but saturday is not weekday!
assert not is_weekday()
```

### Managing Mock's side effects

- you can control code's behavior by specifying a mocked function's side effects (https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect)
- side effect defines what happens when you call the mocked function
- you can use side effects to mock the return values, e.g.
- see `src/mocking/mock_demo.py` file for a full demo


```python
mock = Mock()
```


```python
# using side_effect to raise an exception
mock.side_effect = Exception('Boom')
```


```python
mock()
```


```python
# using side_effect to return a sequence of values
mock = Mock()
mock.side_effect = [3, 2, 1]
```


```python
# call mock three times to return each side effect
mock()
```

### Configuring Your Mock

- can configure Mock to set some of the object's behaviors and attributes
- two ways to configure Mock:
    - when you create it (during init)
    - when you use `.configure_mock()` method on Mock object


```python
mock = Mock(side_effect=Exception)
```


```python
# the return value is an exception
mock()
```


```python
mock = Mock(name='Mocking with Python')
```


```python
mock.name
```


```python
mock = Mock(return_value=True)
```


```python
mock()
```


```python
# using .configure_mock()
mock = Mock()
```


```python
mock.configure_mock(return_value=True)
```


```python
mock()
```


```python
# same as
mock = Mock(return_value='fish')
```


```python
mock()
```

## Patching

- patching makes it easier to Mock objects that are imported from a different module
- `unittest.mock` provides a powerful mechanism for mocking objects called `patch()`
- `patch()` looks up an object in a given module and replaces that object with a Mock
- usually, you use patch() as a decorator or a context manager to provide a scope in which you'll mock the target object
- patching a class replaces the class with `MagicMock` instance
- see these demos: `src/mocking/patch_demo.py` and `src/mocking/patch_demo1.py`

### patch( ) as a Decorator
- use patch() as a decorator to mock an object for the duration of your entire test function
- you can stack multiple patch decorators - see examples here: https://docs.python.org/3/library/unittest.mock.html


```python
from unittest.mock import patch
```


```python
help(patch)
```


```python
# Hello class before patched
Hello().greet()
```


```python
@patch('__main__.Hello', spec=True)
def test_Hello(Hello_Mock):
    assert Hello_Mock is Hello
    # If the class is instantiated in the code under test 
    # then it will be the return_value of the mock that will be used
    h = Hello_Mock.return_value
    h.greet.return_value = "Howdy!"
    #h.say_hi.return_value = 'hi'
    assert h.greet() == 'Howdy!'
    o = Hello()
    assert o.greet() == 'Howdy!'
    assert Hello().greet() == 'Howdy!'
    assert Hello_Mock.called
    assert Hello.called
```


```python
# Hello class patched within the test_Hello function
test_Hello()
```


```python
# Hello class after the patch shouldn't change!
Hello().greet()
```

### patch( ) as a Context Manager

- you only want to mock an object for a part of the test scope
- you're already using too many decorators or parameters which hurts your test readability


```python
def test_Hello_context():
    with patch('__main__.Hello', spec=True) as Hello_Mock:
        assert Hello_Mock is Hello
        h = Hello_Mock.return_value
        h.greet.return_value = "Good Bye!"
        assert h.greet() == 'Good Bye!'
        assert Hello().greet() == 'Good Bye!'
        assert Hello_Mock.called
        assert Hello.called
```


```python
test_Hello_context()
```

### patching only object's attributes/methods/API

- you can also mock only one method of an object instead of the entire object
- use `patch.object(class, 'class_method')`


```python
from unittest.mock import patch
```


```python
# just mock the greet method
from typing import Callable as callable
@patch.object(Hello, 'greet', spec=True)
def test_greet(mock_greet: callable) -> None:
    Hello.greet.return_value = 'Howdy!'
    # mock_greet is same as Hello.greet
    assert mock_greet() == 'Howdy!'

```


```python
test_greet()
```


```python
# let's install requests library
! pip install requests
```


```python
import requests
from requests.exceptions import Timeout
```


```python
help(requests)
```


```python
response = requests.get('https://example.com')
```


```python
print(response)
```


```python
response.status_code
```


```python
help(response)
```


```python
response.text
```


```python
# test 404
@patch.object(requests, 'get') # (module, 'function')
def test_requests_get_404(mock_method):
    url = 'http://localhost/calendar/api/holidays'
    requests.get.return_value = Mock(status_code=404)
    response = requests.get(url)
    mock_method.assert_called_with(url)
    assert(response.status_code == 404)
```


```python
test_requests_get_404()
```


```python
# test holidays
@patch.object(requests, 'get') # (module, 'function')
def test_requests_get_christmas(mock_get):
    url = 'http://localhost/calendar/api/holidays'
    holiday_json = '{"Christmas: "December 25, 2023"}'
    requests.get.return_value = Mock(status_code=202, return_value=holiday_json)
    response = requests.get(url)
    mock_get.assert_called_with(url)
    assert(response.status_code == 202)
    assert(response.return_value == holiday_json)
```


```python
test_requests_get_christmas()
```

### Patching Standard IO

- if the Class API/function uses print/stdout, input/stdin, it'll be difficult to unittest without patching stdio
- you can patch stdio with StringIO


```python
# StringIO has API similar to stdio
from io import StringIO
```


```python
help(StringIO)
```

    Help on class StringIO in module io:
    
    class StringIO(_TextIOBase)
     |  StringIO(initial_value='', newline='\n')
     |  
     |  Text I/O implementation using an in-memory buffer.
     |  
     |  The initial_value argument sets the value of object.  The newline
     |  argument is like the one of TextIOWrapper's constructor.
     |  
     |  Method resolution order:
     |      StringIO
     |      _TextIOBase
     |      _IOBase
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getstate__(...)
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __setstate__(...)
     |  
     |  close(self, /)
     |      Close the IO object.
     |      
     |      Attempting any further operation after the object is closed
     |      will raise a ValueError.
     |      
     |      This method has no effect if the file is already closed.
     |  
     |  getvalue(self, /)
     |      Retrieve the entire contents of the object.
     |  
     |  read(self, size=-1, /)
     |      Read at most size characters, returned as a string.
     |      
     |      If the argument is negative or omitted, read until EOF
     |      is reached. Return an empty string at EOF.
     |  
     |  readable(self, /)
     |      Returns True if the IO object can be read.
     |  
     |  readline(self, size=-1, /)
     |      Read until newline or EOF.
     |      
     |      Returns an empty string if EOF is hit immediately.
     |  
     |  seek(self, pos, whence=0, /)
     |      Change stream position.
     |      
     |      Seek to character offset pos relative to position indicated by whence:
     |          0  Start of stream (the default).  pos should be >= 0;
     |          1  Current position - pos must be 0;
     |          2  End of stream - pos must be 0.
     |      Returns the new absolute position.
     |  
     |  seekable(self, /)
     |      Returns True if the IO object can be seeked.
     |  
     |  tell(self, /)
     |      Tell the current file position.
     |  
     |  truncate(self, pos=None, /)
     |      Truncate size to pos.
     |      
     |      The pos argument defaults to the current file position, as
     |      returned by tell().  The current file position is unchanged.
     |      Returns the new absolute position.
     |  
     |  writable(self, /)
     |      Returns True if the IO object can be written.
     |  
     |  write(self, s, /)
     |      Write string to file.
     |      
     |      Returns the number of characters written, which is always equal to
     |      the length of the string.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  closed
     |  
     |  line_buffering
     |  
     |  newlines
     |      Line endings translated so far.
     |      
     |      Only line endings translated during reading are considered.
     |      
     |      Subclasses should override.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _TextIOBase:
     |  
     |  detach(...)
     |      Separate the underlying buffer from the TextIOBase and return it.
     |      
     |      After the underlying buffer has been detached, the TextIO is in an
     |      unusable state.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _TextIOBase:
     |  
     |  encoding
     |      Encoding of the text stream.
     |      
     |      Subclasses should override.
     |  
     |  errors
     |      The error setting of the decoder or encoder.
     |      
     |      Subclasses should override.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _IOBase:
     |  
     |  __del__(...)
     |  
     |  __enter__(...)
     |  
     |  __exit__(...)
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  fileno(self, /)
     |      Returns underlying file descriptor if one exists.
     |      
     |      OSError is raised if the IO object does not use a file descriptor.
     |  
     |  flush(self, /)
     |      Flush write buffers, if applicable.
     |      
     |      This is not implemented for read-only and non-blocking streams.
     |  
     |  isatty(self, /)
     |      Return whether this is an 'interactive' stream.
     |      
     |      Return False if it can't be determined.
     |  
     |  readlines(self, hint=-1, /)
     |      Return a list of lines from the stream.
     |      
     |      hint can be specified to control the number of lines read: no more
     |      lines will be read if the total size (in bytes/characters) of all
     |      lines so far exceeds hint.
     |  
     |  writelines(self, lines, /)
     |      Write a list of lines to stream.
     |      
     |      Line separators are not added, so it is usual for each of the
     |      lines provided to have a line separator at the end.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _IOBase:
     |  
     |  __dict__
    



```python
import sys
```


```python
help(sys.stdin)
```

    Help on TextIOWrapper object:
    
    class TextIOWrapper(_TextIOBase)
     |  TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)
     |  
     |  Character and line based layer over a BufferedIOBase object, buffer.
     |  
     |  encoding gives the name of the encoding that the stream will be
     |  decoded or encoded with. It defaults to locale.getpreferredencoding(False).
     |  
     |  errors determines the strictness of encoding and decoding (see
     |  help(codecs.Codec) or the documentation for codecs.register) and
     |  defaults to "strict".
     |  
     |  newline controls how line endings are handled. It can be None, '',
     |  '\n', '\r', and '\r\n'.  It works as follows:
     |  
     |  * On input, if newline is None, universal newlines mode is
     |    enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
     |    these are translated into '\n' before being returned to the
     |    caller. If it is '', universal newline mode is enabled, but line
     |    endings are returned to the caller untranslated. If it has any of
     |    the other legal values, input lines are only terminated by the given
     |    string, and the line ending is returned to the caller untranslated.
     |  
     |  * On output, if newline is None, any '\n' characters written are
     |    translated to the system default line separator, os.linesep. If
     |    newline is '' or '\n', no translation takes place. If newline is any
     |    of the other legal values, any '\n' characters written are translated
     |    to the given string.
     |  
     |  If line_buffering is True, a call to flush is implied when a call to
     |  write contains a newline character.
     |  
     |  Method resolution order:
     |      TextIOWrapper
     |      _TextIOBase
     |      _IOBase
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  close(self, /)
     |      Flush and close the IO object.
     |      
     |      This method has no effect if the file is already closed.
     |  
     |  detach(self, /)
     |      Separate the underlying buffer from the TextIOBase and return it.
     |      
     |      After the underlying buffer has been detached, the TextIO is in an
     |      unusable state.
     |  
     |  fileno(self, /)
     |      Returns underlying file descriptor if one exists.
     |      
     |      OSError is raised if the IO object does not use a file descriptor.
     |  
     |  flush(self, /)
     |      Flush write buffers, if applicable.
     |      
     |      This is not implemented for read-only and non-blocking streams.
     |  
     |  isatty(self, /)
     |      Return whether this is an 'interactive' stream.
     |      
     |      Return False if it can't be determined.
     |  
     |  read(self, size=-1, /)
     |      Read at most n characters from stream.
     |      
     |      Read from underlying buffer until we have n characters or we hit EOF.
     |      If n is negative or omitted, read until EOF.
     |  
     |  readable(self, /)
     |      Return whether object was opened for reading.
     |      
     |      If False, read() will raise OSError.
     |  
     |  readline(self, size=-1, /)
     |      Read until newline or EOF.
     |      
     |      Returns an empty string if EOF is hit immediately.
     |  
     |  reconfigure(self, /, *, encoding=None, errors=None, newline=None, line_buffering=None, write_through=None)
     |      Reconfigure the text stream with new parameters.
     |      
     |      This also does an implicit stream flush.
     |  
     |  seek(self, cookie, whence=0, /)
     |      Change stream position.
     |      
     |      Change the stream position to the given byte offset. The offset is
     |      interpreted relative to the position indicated by whence.  Values
     |      for whence are:
     |      
     |      * 0 -- start of stream (the default); offset should be zero or positive
     |      * 1 -- current stream position; offset may be negative
     |      * 2 -- end of stream; offset is usually negative
     |      
     |      Return the new absolute position.
     |  
     |  seekable(self, /)
     |      Return whether object supports random access.
     |      
     |      If False, seek(), tell() and truncate() will raise OSError.
     |      This method may need to do a test seek().
     |  
     |  tell(self, /)
     |      Return current stream position.
     |  
     |  truncate(self, pos=None, /)
     |      Truncate file to size bytes.
     |      
     |      File pointer is left unchanged.  Size defaults to the current IO
     |      position as reported by tell().  Returns the new size.
     |  
     |  writable(self, /)
     |      Return whether object was opened for writing.
     |      
     |      If False, write() will raise OSError.
     |  
     |  write(self, text, /)
     |      Write string to stream.
     |      Returns the number of characters written (which is always equal to
     |      the length of the string).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  buffer
     |  
     |  closed
     |  
     |  encoding
     |      Encoding of the text stream.
     |      
     |      Subclasses should override.
     |  
     |  errors
     |      The error setting of the decoder or encoder.
     |      
     |      Subclasses should override.
     |  
     |  line_buffering
     |  
     |  name
     |  
     |  newlines
     |      Line endings translated so far.
     |      
     |      Only line endings translated during reading are considered.
     |      
     |      Subclasses should override.
     |  
     |  write_through
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from _IOBase:
     |  
     |  __del__(...)
     |  
     |  __enter__(...)
     |  
     |  __exit__(...)
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  readlines(self, hint=-1, /)
     |      Return a list of lines from the stream.
     |      
     |      hint can be specified to control the number of lines read: no more
     |      lines will be read if the total size (in bytes/characters) of all
     |      lines so far exceeds hint.
     |  
     |  writelines(self, lines, /)
     |      Write a list of lines to stream.
     |      
     |      Line separators are not added, so it is usual for each of the
     |      lines provided to have a line separator at the end.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from _IOBase:
     |  
     |  __dict__
    



```python
def answer():
    # get result
    print('Some Result', end='\n')
# since, answer doesn't return a value, it's impossible to do regular unittest
```


```python
answer()
```

    Some Result



```python
# using patch as a decorator
@patch('sys.stdout', new_callable=StringIO)
def test_answer(mock_stdout) -> None:
    answer()
    assert mock_stdout.getvalue() == 'Some Result\n'
    
    # print('all test passed') doesn't print to standard out
```


```python
print('hi')
```

    hi



```python
test_answer()
```


```python
# using context syntax
with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
    answer()
    print('test')

    assert mock_stdout.getvalue() == 'Some Result\ntest\n'
```


```python
print('hi')
```

    hi



```python
# standard input
import sys

def getData():
    x = sys.stdin.read()
    return x

def getLines():
    x = sys.stdin.readlines()
    return x

def getInput():
    x = input()
    return x
```


```python
data = getInput()
```


```python
data
```




    'hello'




```python
@patch('sys.stdin')
def test_getData(mock_stdin) -> None:
    mock_stdin.read.return_value = '2 3\n'
    data = getData()
    # use the data
    # get the result
    assert data == '2 3\n'
    # assert result
```


```python
test_getData()
```


```python
with patch('sys.stdin') as mock_stdin:
    mock_stdin.readlines.return_value = ['1 2\n', '3 4\n']
    data = getLines()
    print(data)
    assert data == ['1 2\n', '3 4\n']
    
```

    ['1 2\n', '3 4\n']



```python
# patching the input() function
with patch('__main__.input') as mock_input:
    mock_input.return_value = '1 2 3 4'
    assert getInput() == '1 2 3 4'
```

### where to patch

- for patching to work, you must ensure that you patch the name used by the system under test
- must tell `patch()` correctly where to look for the object/name you want mocked
- if you choose the wrong target location, the result of `patch()` could be something you didn't expect
- good rule of thumb is to patch() the object where it is *looked up*


```python
# datetime module is imported
import datetime
from unittest.mock import patch
```


```python
# patch datetime class
with patch('datetime.datetime'):
    # datetime module is NOT patched
    print(datetime)
    # datetime class is patched MagicMock now
    print(datetime.datetime)
```

    <module 'datetime' from '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/datetime.py'>
    <MagicMock name='datetime' id='4567279264'>



```python
# just the datetime class is imported
from datetime import datetime
```


```python
# the patch has no effect because there's 
# unmocked datetime class imported into the current scope
with patch('datetime.datetime'):
    print(datetime)
    print(datetime.today())
```

    <class 'datetime.datetime'>
    2025-10-14 11:57:09.507544



```python
# if you need to patch datetime class imported into the global namespace
# you do the following
with patch('__main__.datetime'):
    print(datetime)
```

    <MagicMock name='datetime' id='4567159808'>


## common mocking problems

### changes to object interfaces and misspellings

- when interface of an object changes, any tests relying on a Mock of that object may become irrelevant
- misspelling can break a test; recall that Mock creates its interface when you access its members
    - you'll essentially create a new interface when you misspell a name

### changes to external dependencies

- when external dependency changes its interface, your Python objects will become invalid
- your tests will pass but the actual production code will fail

### avoiding common problems using specifications

- use `spec` parameter providing the list of valid interface/method names of module/class you're mocking


```python
from unittest.mock import Mock
from unittest.mock import patch
```


```python
# provide a list of valid api names of the class you want to mock 
calendar = Mock(spec=['is_weekday', 'get_holidays'])
```


```python
calendar.is_weekday()
```




    <Mock name='mock.is_weekday()' id='4567162064'>




```python
# Mock raises AttributeError as create_event() is not in sepc
calendar.create_event()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[143], line 2
          1 # Mock raises AttributeError as create_event() is not in sepc
    ----> 2 calendar.create_event()


    File /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/unittest/mock.py:630, in NonCallableMock.__getattr__(self, name)
        628 elif self._mock_methods is not None:
        629     if name not in self._mock_methods or name in _all_magics:
    --> 630         raise AttributeError("Mock object has no attribute %r" % name)
        631 elif _is_magic(name):
        632     raise AttributeError(name)


    AttributeError: Mock object has no attribute 'create_event'



```python
# automatically create specifications
from unittest.mock import create_autospec

from src.mocking import my_calendar
```


```python
help(my_calendar)
```

    Help on module src.mocking.my_calendar in src.mocking:
    
    NAME
        src.mocking.my_calendar - A module for dealing with calendars.
    
    FUNCTIONS
        get_holidays() -> Any
            Get the upcoming holidays.
            
            Returns:
                Any: The upcoming holidays
        
        is_weekday() -> bool
            Return True if today is a weekday, False otherwise.
            
            Returns:
                bool: True if today is a weekday, False otherwise
    
    DATA
        Any = typing.Any
            Special type indicating an unconstrained type.
            
            - Any is compatible with every type.
            - Any assumed to have all methods.
            - All values assumed to be instances of Any.
            
            Note that all the above statements are true from the point of view of
            static type checkers. At runtime, Any should not be used with instance
            or class checks.
    
    FILE
        /Users/rbasnet/Fall2025/Object-Oriented-Programming-Design-Patterns/notebooks/src/mocking/my_calendar.py
    
    



```python
calendar = create_autospec(my_calendar)
```


```python
calendar.is_weekday()
```




    <MagicMock name='mock.is_weekday()' id='4567379536'>




```python
calendar.sepc
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[149], line 1
    ----> 1 calendar.sepc


    File /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/unittest/mock.py:630, in NonCallableMock.__getattr__(self, name)
        628 elif self._mock_methods is not None:
        629     if name not in self._mock_methods or name in _all_magics:
    --> 630         raise AttributeError("Mock object has no attribute %r" % name)
        631 elif _is_magic(name):
        632     raise AttributeError(name)


    AttributeError: Mock object has no attribute 'sepc'



```python
calendar.create_event()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Cell In[148], line 1
    ----> 1 calendar.create_event()


    File /Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/unittest/mock.py:630, in NonCallableMock.__getattr__(self, name)
        628 elif self._mock_methods is not None:
        629     if name not in self._mock_methods or name in _all_magics:
    --> 630         raise AttributeError("Mock object has no attribute %r" % name)
        631 elif _is_magic(name):
        632     raise AttributeError(name)


    AttributeError: Mock object has no attribute 'create_event'



```python
# if you're using patch do the following
with patch('__main__.my_calendar', autospec=True) as calendar:
    calendar.is_weekday()
    calendar.get_holidays()
    #calendar.create_event()
```

## How much testing is enough?

- how much of your code is actutally being tested?
    - are the corner test cases generated by **hypothesis** enough to test every line, branch, result of your code?
- According to E. W. Dijkstra - "Program testing can be used to show the presence of bugs, but never to show their absence!"

### Code coverage

- with the useage of mocking/patching and hypothesis libraries, you should be able to get 100% code coverage with your unit tests without using #pragma: no cover

## Exercises

- solve the following Kattis problems using OOD
- must write adequate unittesting for the class API
- must write integration testing using Mock to simulate input and output for complete program testing
- use coverage to create html coverage report of your testing

1. FizzBuzz - https://open.kattis.com/problems/fizzbuzz
2. Mixed Fractions - https://open.kattis.com/problems/mixedfractions



```python

```
