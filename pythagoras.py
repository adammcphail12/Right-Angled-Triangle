import math

import math


def pythagoras(a, b, c):
    # need a not blank to figure out which variable is missing, so we can solve for it.
    a_missing, b_missing, c_missing = 1, 1, 1

    # Checks which variables are blank.
    if a == '':
        a_missing = 0
        print('Variable a is missing.')
    elif b == '':
        b_missing = 0
        print('Variable b is missing.')
    elif c == '':
        c_missing = 0
        print('Variable c is missing.')

    # Creates a total score, score needs to be 2 to use pythagoras function.
    sides_found = a_missing + b_missing + c_missing

    if sides_found == 3:
        return None
    elif c_missing == 0:
        c_pow_2 = (a ** 2) + (b ** 2)
        missing_side = math.sqrt(c_pow_2)
        return missing_side
    elif b_missing == 0:
        b_pow_2 = (c ** 2) - (a ** 2)
        missing_side = math.sqrt(b_pow_2)
        return missing_side
    elif a_missing == 0:
        a_pow_2 = (c ** 2) - (b ** 2)
        missing_side = math.sqrt(a_pow_2)
        return missing_side


solve = pythagoras(8, 8, '')
print(solve)
