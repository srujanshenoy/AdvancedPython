# An unnecessarily complex version of the tree
"""
     *
    ***
   *****
  *******
 *********
***********
"""

# def tree_string(n, max_val): return f"{' ' * int(max_val/2)}{'*' * n}{' ' * int(max_val/2)}"
# maxval = 12
# for _ in range(1, maxval): print(tree_string(_, maxval)

def tree_oneliner(n):[print(f"{' ' * (n - i)}{'*' * (2 * i - 1)}{' ' * (n - i)}") for i in range(1, (n + 1) // 2 + 1) if n % 2 != 0 or (n % 2 == 0 and i < (n + 1) // 2 + 1)] if n % 2 != 0 else print("n must be odd")
#                          |       1        |                   |                |                                  |                                                       |                    odd check            |
tree_oneliner(11)