# we need to import libraries.
import math


# first we will look at a pythagoras function

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

    if sides_found < 2:
        print('Sorry You need at least two sides to solve for a third side')
    else:
        print('Ok we will solve now ... (Press Enter to begin solver)')
        input()
        if c_missing == 0:
            c_pow_2 = (a^2) + (b^2)
            missing_side = math.sqrt(c_pow_2)
            return missing_side
