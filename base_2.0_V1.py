import math as mt

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



#---------$ Start Of Program $---------#

instructions = yes_no('Would you like to read the instructions for this program? \n(If This your first time it is reccomended.) ')

if instructions == 'yes':
    print('\n')
    statement_gen('Instructions', '*', 3, 9, 0)
    print('\n\nThis is a program designed to solve right angled triangles.\nIf your triangle is not right angled (ie: It does not have a square in one corner)\nPlease kindly exit this program as it will not help you.\n')
    input(statement_gen('Press ENTER To Continue...', '-', 1, 6, 0))
    cont = yes_no('\nKnowing this information, would you like to\ncontinue with the program? ')
    if cont == 'yes':
        #instructions 
        print('\nThis function works by taking in one of the sides of your triangle, and one of the \nangles that is not 90 degrees. The program will solve the rest of the sides and angles for you.\n\n')
        input(statement_gen('Press ENTER To Continue...', '-', 1, 6, 0))
        print('\n\nYou will also need to label if your side is the hypotonuse or not.\nThis helps our computer solve the triangle with the most precision.\n(For those that do not know what the hypotonuse is, it is the largest side on the triangle.)\n\n')
        input(statement_gen('Press ENTER To Continue...', '-', 1, 6, 0))
        print('\n\nNow with tha all said and done we can start the program\n\n')
        input(statement_gen('Press ENTER To Continue...', '-', 1, 6, 0))
        print('\n')
        statement_gen('Program Starts', '*', 3, 9, 0)

    else:
        print('\nThank you very much for using this program.\nWe are sorry that it doesnt meet your needs and wish\nyou best of luck with solving your problems.\n\n')
        statement_gen('Goodbye :))', '*', 3, 9, 0)
        exit()


