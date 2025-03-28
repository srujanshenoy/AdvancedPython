"""
A bunch of really non pythonic implementations of basics!
"""

"""
-------------------
Increment x: -~x

Works because: 

-(~x) = -(-x - 1) = -(-x) + -(-1) = x + 1 --> Incremented

-------------------

Decrement: ~-x

= ~(-x) = -(-x) - 1 =  x-1 --> Decremented

-------------------
"""

def add(a, b): return [-~a for _ in range(b)][-1] if b else a
def subtract(a, b): return [~-a for _ in range(b)][-1] if b else a
def multiply(a, b, result=0):
    return [(result := -~int(f"{''.join(['1' for _ in range(a)])}", 2) - (1 << a) + a + result) for _ in range(b)][-1] if b else result# def add(a, b): [(a = -~a) for i in range(0, b)] # Removed list comprehension version


print(multiply(2, 5)) # Correctly calls the function
