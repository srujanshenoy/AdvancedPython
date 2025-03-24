"""
TIP #2: Printing Iterables Fancily

learnt from Idently@YouTube
"""

# Define an iterable object, like a list

l: list[int] = [1, 2, 3, 4, 5]



# instead of printing it like this:
print(l)
# (OUTPUT): [1, 2, 3, 4, 5]

print("\n\n\nversus\n\n\n") # Show gap for contrast



# print like this:
print(*l , sep=' ', end=f'\nis the iterable list\n')
""" Output:

1 2 3 4 5 
is the iterable [1, 2, 3, 4, 5]

"""

# --------------- EXPLANATION ------------------

"""
Here, 

sep: 
    The separator between the elements of the iterable
    Can be any string
    Eg: ' '     ', '    ' - '    etc.
    Defaults to none
    
end:
    The string to end the printing of the iterable. 
    Defaults to none
"""

