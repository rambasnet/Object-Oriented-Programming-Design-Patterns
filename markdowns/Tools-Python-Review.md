# Tools

- install and learn to use the following tools:
    - Docker
    - GitHub -- git client, GitHub Project, Issues, etc.
    - Terminal
    - VS Code
    - Kattis
    - Jupyter Notebook

# Python fundamentals

- Learn fundamentals and basic syntax
- learn from my Jupyter Notebooks: https://github.com/rambasnet/Python-Fundamentals
- find and learn from tutorials, e.g. https://realpython.com/
- use interactive mode on a Terminal
- use Jupyter Notebook with ipykernel (default) with conda installation
- learn how script works
- Basic Building Blocks/Concepts
    1. Data and Variables
    2. Input/Output
    3. Basic Math and operators
    4. Functions
    5. Conditional Statements
    6. Loops
    


```python
print('Hello World!')
```

    Hello World!


## Data and Variables
- Fundamental data types
- variable declaration and rules
- escape sequences - \n, \t

- work through some examples


```python
name: str = "John Smith"
```


```python
full_name = "Michael Jordan"
```


```python
lastName = "Obama"
```


```python
num: str = 10
```


```python
x = 5
```


```python
x = 10.5
```


```python
x = "abc"
```

## Standard Input/Output

- sys module
    - sys.stdin; sys.stdout
- input()
- print()


```python
print('Hello World!')
```

    Hello World!



```python
print(b'Hello World!')
```

    b'Hello World!'



```python
name = input()
```

     John Smith



```python
print(f'Hell there {name}!')
```

    Hell there John Smith!


## Basic Math and operators

- math module
- some functions inside math
- built-in help function
- operators: +, -, \*, \**, /, //


```python
2+2
```




    4




```python
2-2
```




    0




```python
2*2
```




    4




```python
2**3
```




    8




```python
4/3
```




    1.3333333333333333




```python
4//3
```




    1



## Functions and return value

- function definition syntax
- type of functions (fruitful and fruitless/None)

- work through some examples


```python
def add(x: int, y: int) -> int:
    return x+y
```


```python
print(add(2, 1.5))
```

    3.5



```python
print(add("Hello ", "World!"))
```

    Hello World!


## Conditional Statements

- one way
- two way
- multiway selectors


```python
a = 10
```


```python
if a %2 ==0:
    print('even')
```

    even



```python
if a%2 == 0:
    print('even')
else:
    print('odd')
```

    even



```python
if a == 0:
    print(f'{a=}')
elif a%2 ==0:
    print('even')
else:
    print('odd')
```

    even



```python
num = int(input('Enter an integer:' ))
if num == 0:
    print(f'{num} is Zero.')
elif num%2 == 0:
    print(f'{num} is Even.')
else:
    print(f'{num} is odd.')
```

    Enter an integer: 10


    10 is Even.


## Loops

- for loop
- while loop


```python
for i in range(10):
    print(f'{i+1} Mississippi!')
```

    1 Mississippi!
    2 Mississippi!
    3 Mississippi!
    4 Mississippi!
    5 Mississippi!
    6 Mississippi!
    7 Mississippi!
    8 Mississippi!
    9 Mississippi!
    10 Mississippi!



```python
while True:
    num = input('Enter a number: ')
    if num == '0':
        break
    else:
        print(f'You entered {num}')
```

    Enter a number:  1


    You entered 1


    Enter a number:  0


## Built-in Data Structures

### Tuple


```python
a = 1, 2, 'hello'
```


```python
a[-1]
```




    'hello'



### List
- similar to array/vector in C++


```python
values = [1, 2, 'hi', [1, 2, 3], a]
```


```python
values
```




    [1, 2, 'hi', [1, 2, 3], (1, 2, 'hello')]



### Dictionary
- key->vlue mapping DS


```python
engToSpan = {'one': 'uno'}
```


```python
engToSpan['two'] = 'dos'
```


```python
engToSpan
```




    {'one': 'uno', 'two': 'dos'}




```python
engToSpan['one']
```




    'uno'



## Modules
- see `src/modules/` file

## System command
- execute system/shell commands from with Python
- powerful feature but can be a security vulnerability!

### os.system( )


```python
import os
```


```python
cmd = "git --version"
ret_val = os.system(cmd)
print(f'returned: {ret_val}')
```

    git version 2.39.2
    returned: 0


### subprocess.call()
- subprocess.check_output() allows to store the output in a variable


```python
import subprocess
```


```python
help(subprocess)
```

    Help on module subprocess:
    
    NAME
        subprocess - Subprocesses with accessible I/O streams
    
    MODULE REFERENCE
        https://docs.python.org/3.12/library/subprocess.html
    
        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.
    
    DESCRIPTION
        This module allows you to spawn processes, connect to their
        input/output/error pipes, and obtain their return codes.
    
        For a complete description of this module see the Python documentation.
    
        Main API
        ========
        run(...): Runs a command, waits for it to complete, then returns a
                  CompletedProcess instance.
        Popen(...): A class for flexibly executing a command in a new process
    
        Constants
        ---------
        DEVNULL: Special value that indicates that os.devnull should be used
        PIPE:    Special value that indicates a pipe should be created
        STDOUT:  Special value that indicates that stderr should go to stdout
    
    
        Older API
        =========
        call(...): Runs a command, waits for it to complete, then returns
            the return code.
        check_call(...): Same as call() but raises CalledProcessError()
            if return code is not 0
        check_output(...): Same as check_call() but returns the contents of
            stdout instead of a return code
        getoutput(...): Runs a command in the shell, waits for it to complete,
            then returns the output
        getstatusoutput(...): Runs a command in the shell, waits for it to complete,
            then returns a (exitcode, output) tuple
    
    CLASSES
        builtins.Exception(builtins.BaseException)
            SubprocessError
                CalledProcessError
                TimeoutExpired
        builtins.object
            CompletedProcess
            Popen
    
        class CalledProcessError(SubprocessError)
         |  CalledProcessError(returncode, cmd, output=None, stderr=None)
         |
         |  Raised when run() is called with check=True and the process
         |  returns a non-zero exit status.
         |
         |  Attributes:
         |    cmd, returncode, stdout, stderr, output
         |
         |  Method resolution order:
         |      CalledProcessError
         |      SubprocessError
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |
         |  Methods defined here:
         |
         |  __init__(self, returncode, cmd, output=None, stderr=None)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |
         |  __str__(self)
         |      Return str(self).
         |
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |
         |  stdout
         |      Alias for output attribute, to match stderr
         |
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from SubprocessError:
         |
         |  __weakref__
         |      list of weak references to the object
         |
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
         |
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.BaseException:
         |
         |  __delattr__(self, name, /)
         |      Implement delattr(self, name).
         |
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |
         |  __reduce__(...)
         |      Helper for pickle.
         |
         |  __repr__(self, /)
         |      Return repr(self).
         |
         |  __setattr__(self, name, value, /)
         |      Implement setattr(self, name, value).
         |
         |  __setstate__(...)
         |
         |  add_note(...)
         |      Exception.add_note(note) --
         |      add a note to the exception
         |
         |  with_traceback(...)
         |      Exception.with_traceback(tb) --
         |      set self.__traceback__ to tb and return self.
         |
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from builtins.BaseException:
         |
         |  __cause__
         |      exception cause
         |
         |  __context__
         |      exception context
         |
         |  __dict__
         |
         |  __suppress_context__
         |
         |  __traceback__
         |
         |  args
    
        class CompletedProcess(builtins.object)
         |  CompletedProcess(args, returncode, stdout=None, stderr=None)
         |
         |  A process that has finished running.
         |
         |  This is returned by run().
         |
         |  Attributes:
         |    args: The list or str args passed to run().
         |    returncode: The exit code of the process, negative for signals.
         |    stdout: The standard output (None if not captured).
         |    stderr: The standard error (None if not captured).
         |
         |  Methods defined here:
         |
         |  __init__(self, args, returncode, stdout=None, stderr=None)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |
         |  __repr__(self)
         |      Return repr(self).
         |
         |  check_returncode(self)
         |      Raise CalledProcessError if the exit code is non-zero.
         |
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |
         |  __class_getitem__ = GenericAlias(...) from builtins.type
         |      Represent a PEP 585 generic type
         |
         |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
         |
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |
         |  __dict__
         |      dictionary for instance variables
         |
         |  __weakref__
         |      list of weak references to the object
    
        class Popen(builtins.object)
         |  Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, user=None, group=None, extra_groups=None, encoding=None, errors=None, text=None, umask=-1, pipesize=-1, process_group=None)
         |
         |  Execute a child program in a new process.
         |
         |  For a complete description of the arguments see the Python documentation.
         |
         |  Arguments:
         |    args: A string, or a sequence of program arguments.
         |
         |    bufsize: supplied as the buffering argument to the open() function when
         |        creating the stdin/stdout/stderr pipe file objects
         |
         |    executable: A replacement program to execute.
         |
         |    stdin, stdout and stderr: These specify the executed programs' standard
         |        input, standard output and standard error file handles, respectively.
         |
         |    preexec_fn: (POSIX only) An object to be called in the child process
         |        just before the child is executed.
         |
         |    close_fds: Controls closing or inheriting of file descriptors.
         |
         |    shell: If true, the command will be executed through the shell.
         |
         |    cwd: Sets the current directory before the child is executed.
         |
         |    env: Defines the environment variables for the new process.
         |
         |    text: If true, decode stdin, stdout and stderr using the given encoding
         |        (if set) or the system default otherwise.
         |
         |    universal_newlines: Alias of text, provided for backwards compatibility.
         |
         |    startupinfo and creationflags (Windows only)
         |
         |    restore_signals (POSIX only)
         |
         |    start_new_session (POSIX only)
         |
         |    process_group (POSIX only)
         |
         |    group (POSIX only)
         |
         |    extra_groups (POSIX only)
         |
         |    user (POSIX only)
         |
         |    umask (POSIX only)
         |
         |    pass_fds (POSIX only)
         |
         |    encoding and errors: Text mode encoding and error handling to use for
         |        file objects stdin, stdout and stderr.
         |
         |  Attributes:
         |      stdin, stdout, stderr, pid, returncode
         |
         |  Methods defined here:
         |
         |  __del__(self, _maxsize=9223372036854775807, _warn=<built-in function warn>)
         |
         |  __enter__(self)
         |
         |  __exit__(self, exc_type, value, traceback)
         |
         |  __init__(self, args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, user=None, group=None, extra_groups=None, encoding=None, errors=None, text=None, umask=-1, pipesize=-1, process_group=None)
         |      Create new Popen instance.
         |
         |  __repr__(self)
         |      Return repr(self).
         |
         |  communicate(self, input=None, timeout=None)
         |      Interact with process: Send data to stdin and close it.
         |      Read data from stdout and stderr, until end-of-file is
         |      reached.  Wait for process to terminate.
         |
         |      The optional "input" argument should be data to be sent to the
         |      child process, or None, if no data should be sent to the child.
         |      communicate() returns a tuple (stdout, stderr).
         |
         |      By default, all communication is in bytes, and therefore any
         |      "input" should be bytes, and the (stdout, stderr) will be bytes.
         |      If in text mode (indicated by self.text_mode), any "input" should
         |      be a string, and (stdout, stderr) will be strings decoded
         |      according to locale encoding, or by "encoding" if set. Text mode
         |      is triggered by setting any of text, encoding, errors or
         |      universal_newlines.
         |
         |  kill(self)
         |      Kill the process with SIGKILL
         |
         |  poll(self)
         |      Check if child process has terminated. Set and return returncode
         |      attribute.
         |
         |  send_signal(self, sig)
         |      Send a signal to the process.
         |
         |  terminate(self)
         |      Terminate the process with SIGTERM
         |
         |  wait(self, timeout=None)
         |      Wait for child process to terminate; returns self.returncode.
         |
         |  ----------------------------------------------------------------------
         |  Class methods defined here:
         |
         |  __class_getitem__ = GenericAlias(...) from builtins.type
         |      Represent a PEP 585 generic type
         |
         |      E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
         |
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |
         |  __dict__
         |      dictionary for instance variables
         |
         |  __weakref__
         |      list of weak references to the object
         |
         |  universal_newlines
    
        class SubprocessError(builtins.Exception)
         |  # Exception classes used by this module.
         |
         |  Method resolution order:
         |      SubprocessError
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |
         |  Data descriptors defined here:
         |
         |  __weakref__
         |      list of weak references to the object
         |
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
         |
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.BaseException:
         |
         |  __delattr__(self, name, /)
         |      Implement delattr(self, name).
         |
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |
         |  __reduce__(...)
         |      Helper for pickle.
         |
         |  __repr__(self, /)
         |      Return repr(self).
         |
         |  __setattr__(self, name, value, /)
         |      Implement setattr(self, name, value).
         |
         |  __setstate__(...)
         |
         |  __str__(self, /)
         |      Return str(self).
         |
         |  add_note(...)
         |      Exception.add_note(note) --
         |      add a note to the exception
         |
         |  with_traceback(...)
         |      Exception.with_traceback(tb) --
         |      set self.__traceback__ to tb and return self.
         |
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from builtins.BaseException:
         |
         |  __cause__
         |      exception cause
         |
         |  __context__
         |      exception context
         |
         |  __dict__
         |
         |  __suppress_context__
         |
         |  __traceback__
         |
         |  args
    
        class TimeoutExpired(SubprocessError)
         |  TimeoutExpired(cmd, timeout, output=None, stderr=None)
         |
         |  This exception is raised when the timeout expires while waiting for a
         |  child process.
         |
         |  Attributes:
         |      cmd, output, stdout, stderr, timeout
         |
         |  Method resolution order:
         |      TimeoutExpired
         |      SubprocessError
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |
         |  Methods defined here:
         |
         |  __init__(self, cmd, timeout, output=None, stderr=None)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |
         |  __str__(self)
         |      Return str(self).
         |
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |
         |  stdout
         |
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from SubprocessError:
         |
         |  __weakref__
         |      list of weak references to the object
         |
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
         |
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.BaseException:
         |
         |  __delattr__(self, name, /)
         |      Implement delattr(self, name).
         |
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |
         |  __reduce__(...)
         |      Helper for pickle.
         |
         |  __repr__(self, /)
         |      Return repr(self).
         |
         |  __setattr__(self, name, value, /)
         |      Implement setattr(self, name, value).
         |
         |  __setstate__(...)
         |
         |  add_note(...)
         |      Exception.add_note(note) --
         |      add a note to the exception
         |
         |  with_traceback(...)
         |      Exception.with_traceback(tb) --
         |      set self.__traceback__ to tb and return self.
         |
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from builtins.BaseException:
         |
         |  __cause__
         |      exception cause
         |
         |  __context__
         |      exception context
         |
         |  __dict__
         |
         |  __suppress_context__
         |
         |  __traceback__
         |
         |  args
    
    FUNCTIONS
        call(*popenargs, timeout=None, **kwargs)
            Run command with arguments.  Wait for command to complete or
            timeout, then return the returncode attribute.
    
            The arguments are the same as for the Popen constructor.  Example:
    
            retcode = call(["ls", "-l"])
    
        check_call(*popenargs, **kwargs)
            Run command with arguments.  Wait for command to complete.  If
            the exit code was zero then return, otherwise raise
            CalledProcessError.  The CalledProcessError object will have the
            return code in the returncode attribute.
    
            The arguments are the same as for the call function.  Example:
    
            check_call(["ls", "-l"])
    
        check_output(*popenargs, timeout=None, **kwargs)
            Run command with arguments and return its output.
    
            If the exit code was non-zero it raises a CalledProcessError.  The
            CalledProcessError object will have the return code in the returncode
            attribute and output in the output attribute.
    
            The arguments are the same as for the Popen constructor.  Example:
    
            >>> check_output(["ls", "-l", "/dev/null"])
            b'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'
    
            The stdout argument is not allowed as it is used internally.
            To capture standard error in the result, use stderr=STDOUT.
    
            >>> check_output(["/bin/sh", "-c",
            ...               "ls -l non_existent_file ; exit 0"],
            ...              stderr=STDOUT)
            b'ls: non_existent_file: No such file or directory\n'
    
            There is an additional optional argument, "input", allowing you to
            pass a string to the subprocess's stdin.  If you use this argument
            you may not also use the Popen constructor's "stdin" argument, as
            it too will be used internally.  Example:
    
            >>> check_output(["sed", "-e", "s/foo/bar/"],
            ...              input=b"when in the course of fooman events\n")
            b'when in the course of barman events\n'
    
            By default, all communication is in bytes, and therefore any "input"
            should be bytes, and the return value will be bytes.  If in text mode,
            any "input" should be a string, and the return value will be a string
            decoded according to locale encoding, or by "encoding" if set. Text mode
            is triggered by setting any of text, encoding, errors or universal_newlines.
    
        getoutput(cmd, *, encoding=None, errors=None)
            Return output (stdout or stderr) of executing cmd in a shell.
    
            Like getstatusoutput(), except the exit status is ignored and the return
            value is a string containing the command's output.  Example:
    
            >>> import subprocess
            >>> subprocess.getoutput('ls /bin/ls')
            '/bin/ls'
    
        getstatusoutput(cmd, *, encoding=None, errors=None)
            Return (exitcode, output) of executing cmd in a shell.
    
            Execute the string 'cmd' in a shell with 'check_output' and
            return a 2-tuple (status, output). The locale encoding is used
            to decode the output and process newlines.
    
            A trailing newline is stripped from the output.
            The exit status for the command can be interpreted
            according to the rules for the function 'wait'. Example:
    
            >>> import subprocess
            >>> subprocess.getstatusoutput('ls /bin/ls')
            (0, '/bin/ls')
            >>> subprocess.getstatusoutput('cat /bin/junk')
            (1, 'cat: /bin/junk: No such file or directory')
            >>> subprocess.getstatusoutput('/bin/junk')
            (127, 'sh: /bin/junk: not found')
            >>> subprocess.getstatusoutput('/bin/kill $$')
            (-15, '')
    
        run(*popenargs, input=None, capture_output=False, timeout=None, check=False, **kwargs)
            Run command with arguments and return a CompletedProcess instance.
    
            The returned instance will have attributes args, returncode, stdout and
            stderr. By default, stdout and stderr are not captured, and those attributes
            will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
            or pass capture_output=True to capture both.
    
            If check is True and the exit code was non-zero, it raises a
            CalledProcessError. The CalledProcessError object will have the return code
            in the returncode attribute, and output & stderr attributes if those streams
            were captured.
    
            If timeout is given, and the process takes too long, a TimeoutExpired
            exception will be raised.
    
            There is an optional argument "input", allowing you to
            pass bytes or a string to the subprocess's stdin.  If you use this argument
            you may not also use the Popen constructor's "stdin" argument, as
            it will be used internally.
    
            By default, all communication is in bytes, and therefore any "input" should
            be bytes, and the stdout and stderr will be bytes. If in text mode, any
            "input" should be a string, and stdout and stderr will be strings decoded
            according to locale encoding, or by "encoding" if set. Text mode is
            triggered by setting any of text, encoding, errors or universal_newlines.
    
            The other arguments are the same as for the Popen constructor.
    
    DATA
        DEVNULL = -3
        PIPE = -1
        STDOUT = -2
        __all__ = ['Popen', 'PIPE', 'STDOUT', 'call', 'check_call', 'getstatus...
    
    FILE
        /usr/local/lib/python3.12/subprocess.py
    
    



```python
ret_val = subprocess.call(cmd, shell=True)
```

    git version 2.39.2



```python
# providing list as command is recommended
output = subprocess.check_output(['git --version'], shell=True)
```


```python
output
```




    b'git version 2.39.2\n'




```python
# print the output binary in ASCII
print(output)
```

    b'git version 2.39.2\n'



```python
print(*output)
```

    103 105 116 32 118 101 114 115 105 111 110 32 50 46 51 57 46 50 10



```python
# print the returned binary as a utf-8 encoded string
print(output.decode('utf-8'))
```

    git version 2.39.2
    



```python
import sys
# providing list as command is recommended
subprocess.check_output(["/bin/sh", "-c", "ls -l; exit 0"], 
             stderr=sys.stdout)
```




    b'total 1268\n-rw-r--r--  1 user users   2186 Feb  8 18:43 00-TableOfContents.ipynb\n-rw-r--r--  1 user users 114112 Feb  6 20:33 ABCOperatorOverloading.ipynb\n-rw-r--r--  1 user users   5591 Feb  6 20:33 AdvancedDesignPatterns.ipynb\n-rw-r--r--  1 user users  35482 Feb  6 20:33 CommonDesignPatterns.ipynb\n-rw-r--r--  1 user users  36312 Feb  8 17:33 ExpectingTheUnexpected.ipynb\n-rw-r--r--  1 user users 452267 Feb  6 20:33 IntersectionOfOOPAndFunctionalProgramming.ipynb\n-rw-r--r--  1 user users  24000 Feb  6 20:33 IteratorPattern.ipynb\n-rw-r--r--  1 user users  13113 Feb  8 18:44 ObjectOrientedDesign.ipynb\n-rw-r--r--  1 user users 115891 Feb  6 20:33 PythonDataStructures.ipynb\n-rw-r--r--  1 user users  55381 Feb  8 16:36 PythonObjects.ipynb\n-rw-r--r--  1 user users 120138 Feb  6 20:33 SerializationAndJSON.ipynb\n-rw-r--r--  1 user users   1966 Feb  8 18:49 SoftwareEngineering.ipynb\n-rw-r--r--  1 user users  42885 Feb  8 17:35 TestDataGeneration.ipynb\n-rw-r--r--  1 user users 130939 Feb  6 20:33 TestingMockingPatching.ipynb\n-rw-r--r--  1 user users  13786 Feb  8 17:31 TestingOOP.ipynb\n-rw-r--r--  1 user users  16622 Feb  8 18:42 Tools-Python-Review.ipynb\n-rw-r--r--  1 user users  52924 Feb  6 20:33 WhenObjectsAreAlike.ipynb\n-rw-r--r--  1 user users  27248 Feb  6 20:33 WhenToUseOOP.ipynb\n-rw-r--r--  1 user users     19 Feb  6 20:33 filename.txt\ndrwxr-xr-x 24 user users    768 Feb  6 20:33 resources\n'



## Exercise

- Complete the following quizzes from: https://realpython.com/quizzes/
- Take the screenshot of the first attempt. Take the screenshot of the final attempt when you receive 100%

1. Basic Data Types in Python ( https://realpython.com/quizzes/python-data-types/) 
2. How to Run Your Python Scrpts (https://realpython.com/quizzes/run-python-scripts/)
3. Python Basics: Code Your First Python Program - https://realpython.com/quizzes/python-basics-first-program/
4. Python Basics: Conditional Logic and Control Flow (https://realpython.com/quizzes/python-basics-conditional-logic-and-control-flow/)
5. Python Basics: Dictionaries - https://realpython.com/quizzes/python-basics-dictionaries/
6. Python Basics: Functions and Loops - https://realpython.com/quizzes/python-basics-functions-and-loops/
7. Python Basics: Numbers and Math - https://realpython.com/quizzes/python-basics-numbers-and-math/
8. Python Basics: Scopes - https://realpython.com/quizzes/python-basics-scopes/
9. Python Basics: Strings and String Methods - https://realpython.com/quizzes/python-basics-strings-and-string-methods/
10. Python Basics: Python Lists and Tuples - https://realpython.com/quizzes/python-lists-tuples/
11. Python Operators and Expressions - https://realpython.com/quizzes/python-operators-expressions/
12. Python f-String: https://realpython.com/quizzes/f-strings/
13. HTTP Requests with "requests" Library - https://realpython.com/quizzes/python-requests/



```python

```
