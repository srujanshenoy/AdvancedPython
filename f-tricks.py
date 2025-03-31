"""
Summary:

String formatting general format:

print(f"
     {(var):(fill character)(Alignment)(width)}
     ")

    Alignment:
        Left  :   <   (Default, so... redundant)
        Right :   >
        Center:   ^

    Can use variables in place of strict numbers BUT only in curly braces (  {}  )


Number Formatting:

    print(f"
    { (number / variable:float or int):(fill character)(Alignment[1])(width)(thousands_seperator[2]).(round to nth decimal)f }
    ")

    [1]:
        <    |  Left Align
        >    |  Right Align
        ^    |  Center Align

    [2]: Can only be (  ,  ) or (  _  )


"""

a:int = 5
b:int = 10
testvar:str = "Hello"

# Trick 1: Alignment

print(f"{testvar:>20}") # Right align to 20 chars
print(f"{testvar:<20}:") # Left align to 20 chars (: at end only to show)
print(f"{testvar:^20}") # Center align to 20 chars

print("\n\n\n\n")

# Using variables

width = 50 #Number of chars

print(f"{testvar:>{width}}") # Right align
print(f"{testvar:<{width}}:") # Left align
print(f"{testvar:^{width}}") # Center align

# Add a fill in character

print(f"{testvar:_>{width}}") # Right align
print(f"{testvar:_<{width}}:") # Left align
print(f"{testvar:_^{width}}") # Center align



print(f"\n\n{"NEXT CATEGORY":=^100} \n\n")


# rounding

c:float = 122323456.1234567891234567889123456789 #We may want to round this down as we are printing

print(f"{c:.4f}") # Rounds to four decimals
print(f"{c:,.4f}") # Adds commas for each thousand
print(f"{c:_^50,.4f}") # Combined Complexity
