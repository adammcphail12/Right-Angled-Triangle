import math


def solve_right_triangle():
    # Get user input for known values
    side_a = input("Enter the value of side a (opposite angle A): ")
    side_b = input("Enter the value of side b (adjacent to angle A): ")
    angle_a = input("Enter the value of angle A (in degrees): ")

    # Convert input to floats or None if 'x' is entered
    side_a = float(side_a) if side_a != 'x' else None
    side_b = float(side_b) if side_b != 'x' else None
    angle_a = math.radians(float(angle_a)) if angle_a != 'x' else None

    # Solve for missing values using trigonometric ratios
    if side_a is None:
        side_a = side_b / math.tan(angle_a)
    elif side_b is None:
        side_b = side_a * math.tan(angle_a)
    elif angle_a is None:
        angle_a = math.atan(side_a / side_b)

    # Calculate remaining values using Pythagoras' theorem
    side_c = math.sqrt(side_a ** 2 + side_b ** 2)
    angle_b = math.degrees(math.asin(side_a / side_c))
    angle_c = 90 - angle_a - angle_b

    # Display results
    print("Results:")
    print("Side a (opposite angle A):", side_a)
    print("Side b (adjacent to angle A):", side_b)
    print("Side c (hypotenuse):", side_c)
    print("Angle A (in degrees):", math.degrees(angle_a))
    print("Angle B (in degrees):", angle_b)
    print("Angle C (in degrees):", angle_c)


# Call the function to start the solver
solve_right_triangle()
