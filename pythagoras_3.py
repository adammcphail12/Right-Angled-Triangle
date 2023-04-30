import math


def pythagoras(a, b, c):
    # Check which variable is missing and solve for it.
    def base_length(hyp, alt):
        base = math.sqrt((hyp ** 2) - (alt ** 2))
        return base
    if not a:
        missing_side = base_length(c, b)
    elif not b:
        missing_side = base_length(c, a)
    elif not c:
        missing_side = math.hypot(a, b)
    else:
        return None  # if all sides are given, the function returns None.

    return missing_side  # Return the missing side.


solve = pythagoras(41, 62, '')
print(solve)
