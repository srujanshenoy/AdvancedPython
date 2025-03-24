"""

TIP #1: Caching

Learnt from Indently@youtube

Caching in python is a way to almost instantly speed up your python programs

Caching is a way for us to save the results of the heavy duty function calls and return the result from the cache
instead of computing it again and again, using lru cache

To use this caching, we must use ait as a decorator, like this:

-----
@lru_cache
def iterative_function:
    Somthing involving iterative compute comes here (Like the example in the code below)
-----

This would be much slower that if you had not put the decorator '@lru_cache'
"""

from functools import lru_cache
import time

def fibonachi_without_caching(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonachi_without_caching(n-1) + fibonachi_without_caching(n-2)

@lru_cache
def fibonachi_with_caching(n):
    return 1 if (n == 1) or (n == 2) else fibonachi_with_caching(n-1) + fibonachi_with_caching(n-2)
#   Same implementation in one line (Other than for if n>2 has been replaced with else, be careful with that


# ---------------------------------------TESTING------------------------------------------------------------


start_time = time.time()  # Start timing here

for i in range(1, 40):
    print(f"{fibonachi_without_caching(i)}, ", end="")

end_time = time.time() # And end it here

elapsed_time = end_time - start_time
print(f"\nTime taken without caching: {elapsed_time:.6f} seconds")



# With Caching



start_time_2 = time.time()

for i in range(1, 40):
    print(f"{fibonachi_with_caching(i)}, ", end="")

end_time_2 = time.time()

elapsed_time_2 = end_time_2 - start_time_2
print(f"\nTime taken with caching: {elapsed_time_2:.6f} seconds")

# See the improvement? A flipping LOT!

