import math


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return 'yes'
        elif response == 'no' or response == 'n':
            return 'no'
        else:
            print('Please Enter Yes Or No.')


def num_input(task, question, error):
    cont = yes_no('Do you have a value for ' + task + '?')
    if cont == 'yes':
        valid = False
        while not valid:
            # This means it will try asking for the integer first.
            # if it gets a value error it will move to the 'Except"
            # method. Where it prints the predetermined error method.
            try:
                # input has to be a integer or else it will get a
                # value error.
                response = int(input(question))
                # if the answer is greater than 0 then it will return
                # the input as there response.
                if 0 < response:
                    return response
                else:  # if the answer is less than 0 it will print the error.
                    print(error)
            except ValueError:
                print(error)
    else:
        return ''


def pythagoras(a, b, c):
    # Check which variable is missing and solve for it.

    def base_length(hyp, alt):
        base = math.sqrt((hyp ** 2) - (alt ** 2))
        return base

    if not a:
        missing_side = base_length(c, b)
        side_missing = 'a'
    elif not b:
        missing_side = base_length(c, a)
        side_missing = 'b'
    elif not c:
        missing_side = math.hypot(a, b)
        side_missing = 'c'

    return missing_side, side_missing  # Return the missing side.


# Base Code

tick = 0

side_a = num_input('Side A', 'Please enter a positive whole integer.', 'Sorry that is not a positive whole integer')
side_b = num_input('Side B', 'Please enter a positive whole integer.', 'Sorry that is not a positive whole integer')
side_c = num_input('Side C', 'Please enter a positive whole integer.', 'Sorry that is not a positive whole integer')

if side_a != '':
    tick += 1
if side_b != '':
    tick += 1
if side_c != '':
    tick += 1

if tick == 2:
    solve = pythagoras(side_a, side_b, side_c)
    print('Your side missing is side {} and its value is {}'.format(solve[1], solve[0]))
elif tick == 3:
    print('You have all three sides all ready :)')
elif tick == 1:
    print('You only have one side, which is not enough to perform pythagaros')
elif tick == 0:
    print('You have no sides :(')


