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
                response = float(input(question))
                # if the answer is greater than 0 then it will return
                # the input as there response.
                if 0 < response:
                    return response
                else:  # if the answer is less than 0 it will print the error.
                    print(error)
            except ValueError:
                print(error)
    else:
        return None



def solve_triangle(side_a=None, side_b=None, side_c=None, angle_A=None, angle_B=None, angle_C=None):
    # Check that we have enough information to solve the triangle
    sides = [side_a, side_b, side_c]
    angles = [angle_A, angle_B, angle_C]
    known_sides = sum(side is not None for side in sides)
    known_angles = sum(angle is not None for angle in angles)
    if known_angles + known_sides <= 2 and known_sides != 2 :
        print('Sorry not enough data to solve a triangle.')
        return 'STOP'

    # uses math to calculate angles when sides are known.
    if known_sides == 3:
        angle_A = math.degrees(math.acos((side_b ** 2 + side_c ** 2 - side_a ** 2) / (2 * side_b * side_c)))
        angle_B = math.degrees(math.acos((side_c ** 2 + side_a ** 2 - side_b ** 2) / (2 * side_c * side_a)))
        angle_C = math.degrees(math.acos((side_a ** 2 + side_b ** 2 - side_c ** 2) / (2 * side_a * side_b)))
        return side_a, side_b, side_c, angle_A, angle_B, angle_C

    # uses pythagarus and then uses the same math from 3 sides to calculate the angles.
    elif known_sides == 2:
        def base_length(hyp, alt):
            base = math.sqrt((hyp ** 2) - (alt ** 2))
            return base
        if not side_a:
            side_a = base_length(side_c, side_b)
        elif not side_b:
            side_b = base_length(side_c, side_a)
        elif not side_c:
            side_c = math.hypot(side_a, side_b)
        angle_A = math.degrees(math.acos((side_b ** 2 + side_c ** 2 - side_a ** 2) / (2 * side_b * side_c)))
        angle_B = math.degrees(math.acos((side_c ** 2 + side_a ** 2 - side_b ** 2) / (2 * side_c * side_a)))
        angle_C = math.degrees(math.acos((side_a ** 2 + side_b ** 2 - side_c ** 2) / (2 * side_a * side_b)))
        return side_a, side_b, side_c, angle_A, angle_B, angle_C
    #this calculates the two sides and the last angle.
    if known_angles == 2 and known_sides == 1:
        if angle_A is None:
            angle_A = 180 - angle_B - angle_C
        elif angle_B is None:
            angle_B = 180 - angle_A - angle_C
        elif angle_C is None:
            angle_C = 180 - angle_A - angle_B

        side = next((s for s in [side_a, side_b, side_c] if s is not None))

        if side_a is None:
            side_a = side * math.sin(math.radians(angle_A)) / math.sin(math.radians(angle_C))
        if side_b is None:
            side_b = side * math.sin(math.radians(angle_B)) / math.sin(math.radians(angle_C))
        if side_c is None:
            side_c = side * math.sin(math.radians(angle_C)) / math.sin(math.radians(angle_A))
        return side_a, side_b, side_c, angle_A, angle_B, angle_C
        # returns all sides in a list.
    

# uses a number input checker to get the sides and angles that the user knows
side_a = num_input('Side A', 'Please enter a positive whole integer.', 'Sorry that is not a positive whole integer')
side_b = num_input('Side B', 'Please enter a positive whole integer.', 'Sorry that is not a positive whole integer')
side_c = num_input('Side C', 'Please enter a positive value.', 'Sorry that is not a positive whole integer')
angle_a = num_input('Angle A', 'Please enter a positive value.', 'Sorry that is not a positive whole integer')
angle_b = num_input('Angle B', 'Please enter a positive value.', 'Sorry that is not a positive whole integer')
angle_c = num_input('Angle C', 'Please enter a positive value.', 'Sorry that is not a positive whole integer')

# solves the triangle if the user gives enough information
triangle = solve_triangle(side_a, side_b, side_c, angle_a, angle_b, angle_c)

if triangle == 'STOP':
    print("thank you for using this software")
else:
    #assigns the new values of the triangle 
    side_a = triangle[0]
    side_b = triangle[1]
    side_c = triangle[2]
    angle_a = triangle[3]
    angle_b = triangle[4]
    angle_c = triangle[5]

    # prints the results out.
    print((f'Side A = {side_a}'))
    print((f'Side B = {side_b}'))
    print((f'Side C = {side_c}'))
    print((f'Angle A = {angle_a}'))
    print((f'Angle B = {angle_b}'))
    print((f'Angle C = {angle_c}'))
    print("thank you for using this software")
