import math


def pythagoras(side_a, side_b, side_c):
    # Check which variable is missing and solve for it.
    def base_length(hyp, alt):
        base = math.sqrt((hyp ** 2) - (alt ** 2))
        return base
    if not side_a:
        side_a = base_length(side_c, side_b)
    elif not side_b:
        side_b = base_length(side_c, side_a)
    elif not side_c:
        side_c = math.hypot(side_a, side_b)
    else:
        return None  # if all sides are given, the function returns None.

    return missing_side  # Return the missing side.


solve = pythagoras(41, 62, '')
print(solve)
