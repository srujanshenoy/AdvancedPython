"""
Learnt from Indently@YouTube

 Tip #4: A faster for i in range type of loop :/

Keep in mind that you can only use the faster method if you dont care about the value,
The faster method uses the    i (or) _     in the script as a NoneType object.

TODO: Fix the damn code to an example that works!
"""

# Slower method to go through a list: (with timing)

import time
from itertools import repeat



start_time = time.time()

for _  in range(0, 100): print(_^4)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Using `for _ in range(...): {elapsed_time}")

# Faster method to go through a list: (with timing)

start_time_2 = time.time()

for _ in repeat(None, 100): print(_^4)

end_time_2 = time.time()
elapsed_time_2 = end_time_2 - start_time_2

print(f"Using `repeat(None, 100): {elapsed_time_2}")