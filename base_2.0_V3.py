import math as mt
import pandas as pd

# Yes no checker.
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return 'yes'
        elif response == 'no' or response == 'n':
            return 'no'
        else:
            print('Please Enter Yes Or No.')


#Statement_Gen is for all the fancy decorations and and stuff.
def statement_gen(statement, decoration,lines,dec_num,del_num) :
    #(Statement is what you say)(This is the charecter for your lines to be "^")(This is how many rows.)(This is how long the decor4ation is on either side)(This is how many charecters need to be deleted)
    sides = decoration * dec_num
    statement = ("{} {} {}".format(sides,statement,sides))
    if lines == 3:
        #this is what happens when you wantg three rows
        
        topbottomlenth = len(statement) - del_num # Number cannot * a string in the same variable
        topbottomv2 = topbottomlenth * decoration 

        print(topbottomv2)
        print(statement)
        print(topbottomv2)

        #This is what happens when you want only one row
        
    else:
        print(statement)
    
    return ""

# this is the input function that i use to take in angles.
def num_input(question, error, side_or_angle, hypot_found):
    while True:
        try:
            response = float(input(question))
            if side_or_angle == 0:
                if response < 90 and response > 0:
                    return response
                else:
                    print(error) 
            elif side_or_angle == 1:
                
                if response > 0:
                    if hypot_found == 'yes':
                        return response, 'no'
                    else:
                        hypot = yes_no('\nIs this side your hypotonuse? ')
                        return response, hypot
                else:
                    print(error) 
        except ValueError:
            print(error)

def solve_triangle(hypotnuse, small_side_1, small_side_2, angle_1, angle_2, angle_3):
    
    if hypotnuse is not None and angle_1 is not None:
        angle_1 = mt.radians(angle_1)
        small_side_1 = mt.sin(angle_1) * hypotnuse
        small_side_1 = round_to(small_side_1, 4)
        small_side_2 = mt.sqrt((hypotnuse ** 2) - (small_side_1 ** 2))
        small_side_2 = round_to(small_side_2, 4)
        angle_1 = mt.degrees(angle_1)
    elif small_side_1 is not None and angle_1 is not None:
        angle_1 = mt.radians(angle_1)
        small_side_2 = mt.tan(angle_1) * small_side_1
        small_side_2 = round_to(small_side_2, 4)
        hypotnuse = mt.hypot(small_side_1, small_side_2)
        angle_1 = mt.degrees(angle_1)
    elif angle_1 is None:
        if hypotnuse is None:
            hypotnuse = mt.hypot(small_side_1,small_side_2)
        elif small_side_2 is None:
            small_side_2 = mt.sqrt(hypotnuse ** 2  - small_side_1 ** 2)
        print(hypotnuse)
        angle_3 = 90.00
        print(small_side_1)
        angle_1 = round_to(mt.degrees(mt.asin(small_side_1 / hypotnuse)), 4)
        print(angle_1)
        angle_2 = 90 - angle_1

    
    return(hypotnuse, small_side_1, small_side_2, angle_1, angle_2, angle_3)



def round_to(x, significant_figs):
   return round(x, significant_figs - mt.floor(mt.log10(abs(x))) - 1)
 




#-------------------$ Start Of Program $-------------------#

#------$ Instructions $------#

# This is the instruction set tells you how the program works
# also lets you exit the program if you do not have correct data

instructions = yes_no('Would you like to read the instructions for this program? \n(If This your first time it is reccomended.) ')

if instructions == 'yes':
    print('\n')
    statement_gen('Instructions', '*', 3, 9, 0)
    print('\n\nThis is a program designed to solve right angled triangles.\nIf your triangle is not right angled (ie: It does not have a square in one corner)\nPlease kindly exit this program as it will not help you.\n')
    input(statement_gen('Press ENTER To Continue...', '-', 1, 6, 0))
    cont = yes_no('\nKnowing this information, would you like to\ncontinue with the program? ')
    if cont == 'yes':
        #instructions 
        print('\nThis function works by taking in two values of data from your triangle.\nThe program will solve the rest of the sides and angles for you.\n\n')
        input(statement_gen('Press ENTER To Continue...', '-', 1, 6, 0))
        print('\n\nYou will also need to label if your side is the hypotonuse or not.\nThis helps our computer solve the triangle with the most precision.\n(For those that do not know what the hypotonuse is, it is the largest side on the triangle.)\n\n')
        input(statement_gen('Press ENTER To Continue...', '-', 1, 6, 0))
        print('\n\nNow with tha all said and done we can start the program\n\n')
        input(statement_gen('Press ENTER To Continue...', '-', 1, 6, 0))
        print('\n')
        

    else:
        print('\nThank you very much for using this program.\nWe are sorry that it doesnt meet your needs and wish\nyou best of luck with solving your problems.\n\n')
        statement_gen('Goodbye :))', '*', 3, 9, 0)
        exit()
else: 
    print('\n\n')

#------$ Data Input $------#

# we need to take in one angle so we can determine the other two angles.
loop = True
while loop is True:
    hypotnuse = None
    small_side_1 = None
    small_side_2 = None
    angle_1 = None
    angle_2 = None
    angle_3 = 90
    statement_gen('Program Starts', '*', 3, 9, 0)
    any_angles = yes_no('\n\nDo you have any angles on your triangle? \n(Not including the 90 degree angle that is in the square corner of your triangle)?')
    if any_angles == 'yes':
        angle_1 = num_input('\n\nWhat number represents your first angle?\nThis is not the 90 degree angle, this is one of your smaller angles : ', '\nThat is not a valid number, should be a number\nthat is greater then 0 and less then 90', 0, 'no')
        angle_2 = 90 - angle_1
        angle_3 = 90
        side = num_input('\nWhat number represents your side?', '\nThat is not a valid number, number should be positive.', 1, 'no')
        if side[1] == 'yes':
            hypotnuse = side[0]
            small_side_1 = None
            small_side_2 = None
        else:
            small_side_1 = side[0]
            small_side_2 = None
            hypotnuse = None
    else:
        angle_1 = None
        angle_2 = None
        angle_3 = 90
        side_1 = num_input('\nWhat number represents your first side?', '\nThat is not a valid number, number should be positive.', 1, 'no')
        if side_1[1] == 'yes':
            hypotnuse = side_1[0]
            side_2 = num_input('\nWhat number represents your second smaller side?', '\nThat is not a valid number, number should be positive.', 1, 'yes')
            small_side_1 = side_2[0]
            small_side_2 = None
            print(hypotnuse)
            print(small_side_1)
        else: 
            small_side_1 = side_1[0]
            side_2 = num_input('\nWhat number represents your first side?', '\nThat is not a valid number, number should be positive.', 1, 'no')
            if side_2[1] == 'yes':
                hypotnuse = side_2[0]
                small_side_2 = None
            else:
                small_side_2 = side_2[0]
                hypotnuse = None
    print(hypotnuse, small_side_1, small_side_2, angle_1, angle_2, angle_3)
            
        







    print('\n\n')
    input(statement_gen('Press ENTER To Continue...', '-', 1, 6, 0))
    print('\n\nOur computer will know solve your triangle for you.\nPlease wait one moment.')


    triangle = solve_triangle(hypotnuse, small_side_1, small_side_2, angle_1, angle_2, angle_3)
    data = {'Name': ['Hypot', 'Small Side 1', 'Small Side 2', 'Angle 1', 'Angle 2', 'Angle 3'], 'Value':triangle}
    df = pd.DataFrame(data)
    print(df.to_string(index = False))

    hypotnuse = triangle[0]
    small_side_1 = triangle[1]
    small_side_2 = triangle[2]
    angle_1 = triangle[3]
    angle_2 = triangle[4]
    angle_3 = triangle[5]

    print('\n')
    input(statement_gen('Press ENTER to have results explained', '-', 1, 6, 0))

    print('\n\nIn this triangle your Hypotnuse is {}.\nYour first small side is {}, Your second small side is {}.\n\n'.format(hypotnuse, small_side_1, small_side_2))

    input(statement_gen('Press ENTER to Continue', '-', 1, 6, 0))

    print('\n\nIn this triangle your first angle is {}, your second angle is {}\nYour third angle is 90'.format(angle_1, angle_2))

    repeat = yes_no('Would you like to run the program again?')
    if repeat == 'yes':
        loop = True
    else:
        loop = False








