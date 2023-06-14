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
    if known_sides + known_angles < 3:
        print("Not enough information to solve triangle.")
        return
    # If we have three sides, use law of cosines to find angles
    if known_sides == 3:
        angle_A = math.degrees(math.acos((side_b ** 2 + side_c ** 2 - side_a ** 2) / (2 * side_b * side_c)))
        angle_B = math.degrees(math.acos((side_c ** 2 + side_a ** 2 - side_b ** 2) / (2 * side_c * side_a)))
        angle_C = math.degrees(math.acos((side_a ** 2 + side_b ** 2 - side_c ** 2) / (2 * side_a * side_b)))
        return side_a, side_b, side_c, angle_A, angle_B, angle_C
    # If we have two sides and an angle, use law of sines to find remaining parts
    elif known_sides == 2 and known_angles == 1:
        if side_a is None:
            side_a = side_b * math.sin(math.radians(angle_B)) / math.sin(math.radians(angle_A))
        elif side_b is None:
            side_b = side_a * math.sin(math.radians(angle_A)) / math.sin(math.radians(angle_B))
        elif side_c is None:
            angle = next((angle for angle in angles if angle is not None))
            side_c = side_a / math.sin(math.radians(angle_A)) * math.sin(math.radians(angle))
        return side_a, side_b, side_c, angle_A, angle_B, angle_C
    # If we have two angles and a side, use angle sum property to find remaining angle
    elif known_angles == 2 and known_sides == 1:
        if angle_A is None:
            angle_A = 180 - angle_B - angle_C
        elif angle_B is None:
            angle_B = 180 - angle_A - angle_C
        elif angle_C is None:
            angle_C = 180 - angle_A - angle_B
        side = next((s for s in sides if s is not None))
        if side_a is None:
            side_a = side * math.sin(math.radians(angle_A)) / math.sin(math.radians(angle_C))
        elif side_b is None:
            side_b = side * math.sin(math.radians(angle_B)) / math.sin(math.radians(angle_C))
        elif side_c is None:
            side_c = side * math.sin(math.radians(angle_C)) / math.sin(math.radians(angle_A))
        return side_a, side_b, side_c, angle_A, angle_B, angle_C
    if known_sides == 3:
        angle_A = math.degrees(math.acos((side_b ** 2 + side_c ** 2 - side_a ** 2) / (2 * side_b * side_c)))
        angle_B = math.degrees(math.acos((side_c ** 2 + side_a ** 2 - side_b ** 2) / (2 * side_c * side_a)))
        angle_C = math.degrees(math.acos((side_a ** 2 + side_b ** 2 - side_c ** 2) / (2 * side_a * side_b)))
        return side_a, side_b, side_c, angle_A, angle_B, angle_C


side_a = num_input('Side A', 'Please enter a positive whole integer.', 'Sorry that is not a positive whole integer')
side_b = num_input('Side B', 'Please enter a positive whole integer.', 'Sorry that is not a positive whole integer')
side_c = num_input('Side C', 'Please enter a positive value.', 'Sorry that is not a positive whole integer')
angle_a = num_input('Angle A', 'Please enter a positive value.', 'Sorry that is not a positive whole integer')
angle_b = num_input('Angle B', 'Please enter a positive value.', 'Sorry that is not a positive whole integer')
angle_c = num_input('Angle C', 'Please enter a positive value.', 'Sorry that is not a positive whole integer')

print('Side A: ', side_a)
print('Side B: ', side_b)
print('Side C: ', side_c)
print('Angle A: ', angle_a)
print('Angle B: ', angle_b)
print('Angle C: ', angle_c)

triangle = solve_triangle(side_a, side_b, side_c, angle_a, angle_b, angle_c)

print(triangle)
