"""

TIP #3: Partial Functions

A fucntion that builds on another one
"""

from functools import partial

def multiply(a, b): return a*b

double = partial(multiply, 2)

"""
To use function `partial`

Takes:
    - 1st arg  : Function name
    - Next Args: Function's args to modify. 
"""

num1 = double(5)
print(num1)