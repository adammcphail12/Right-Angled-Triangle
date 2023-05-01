import math


def solve_triangle(side_a, side_b, side_c, angle_A, angle_B, angle_C):
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
    # If we have one side and one angle, use basic trigonometry to find remaining parts
    elif known_sides == 1 and known_angles == 1:
        if angle_A is None:
            angle_A = math.degrees(math.asin(side_a / side_b * math.sin(math.radians(angle_B))))
            angle_C = 180 - angle_A - angle_B
            side_c = side_b * math.sin(math.radians(angle_C)) / math.sin(math.radians(angle_B))
        elif angle_B is None:
            angle_B = math.degrees(math.asin(side_b / side_a * math.sin(math.radians(angle_A))))
            angle_C = 180 - angle_A - angle_B
            if side_a is None:
                side_a = side_b * math.sin(math.radians(angle_A)) / math.sin(math.radians(angle_B))
            elif side_b is None:
                side_b = side_a * math.sin(math.radians(angle_B)) / math.sin(math.radians(angle_A))
            elif side_c is None:
                side_c = side_a / math.sin(math.radians(angle_A)) * math.sin(math.radians(angle_C))
        else:
            print("Invalid input.")
            return ''
        return side_a, side_b, side_c, angle_A, angle_B, angle_C


solve = solve_triangle()
print(solve)
