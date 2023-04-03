import math


def pythagoras(a, b, c):
    # Check which variable is missing and solve for it.
    if not a:
        missing_side = math.sqrt((c ** 2) - (b ** 2))
    elif not b:
        missing_side = math.sqrt((c ** 2) - (a ** 2))
    elif not c:
        missing_side = math.hypot(a, b)
    else:
        return None  # if all sides are given, the function returns None.

    return missing_side  # Return the missing side.


solve = pythagoras(8, 8, '')
print(solve)
