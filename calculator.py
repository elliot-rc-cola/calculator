# basic calculator
# can solve basic math between two number eg 6*5 or 7/1
# user will type in their equation and the answer will appear below, maybe with the text 'The Answeer is <answer>'
# will need to account for the user not including spaces when entering the equation 1+1 v 1 + 1
# a history will also be kept of the pevious equations and their answers
# other needed functions:
## add_history() - add equations and solutions to the list
## solution() - to split the operator from operands and calculate the equation
# error handling will need to be added to ensure only numbers and operators are used. 
# also to make sure the equations aren't more than two numbers long.
# let's get into it!


# previous equations will be stored here
history = []

# the other functions

# keeping track of previous equations
def add_history(equation, answer):

    history.append(f'{equation} = {round(answer, 3)}')

# takes the equation and splits it into individual parts before solving
def solution(equation):
    # the equation will first need to be split into individual 
    # try except to handle any errors
    try:
        equation_chars = equation.split(' ')

        # assigning each operand and operator to a variable
        operand_one = float(equation_chars[0])
        operator = equation_chars[1]
        operand_two = float(equation_chars[2])

        # lambda dictionary to do calculations
        op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '/': lambda x, y: x / y, '*': lambda x, y: x * y}

        # performing the calculation
        if operator in op:
                answer = op[operator](operand_one, operand_two)
        else:
            print("Error: Invalid operator")
                
        # add the equation and solution to history
        add_history(equation, round(answer, 3))

        print(f'The solution: {round(answer, 3)}')

    except ValueError:
        print('Error: Invalid number')

    except ZeroDivisionError:
        print('Error: Division by zero')

# rather than having the equation added as parameters, this will be done via input so the menu us displayed
def calculator():
    # if the users chooses 3 this will break the loop ending the program
    while True:
        # menu and tasks
        print('\nBasic Calculator')
        print('1. Solve an equation')
        print('2. Show history')
        print('3. Exit')

        # to start the program loop
        task = input('\nPlease choose a task: ')

        # 1. Solve an equation
        if task == '1':
            print('\nAdd, subtract, multiply, and divide any two numbers')
            print('Please include spaces between the operands and operator eg. 1 + 1')
            equation = input('The equation: ') 
            solution(equation)
        # 2. Show history
        elif task == '2':
            print(history)

        # 3. Exit
        elif task == '3':
            print('Goodbye!')
            break
            
# calling the fuction to get things started
calculator()