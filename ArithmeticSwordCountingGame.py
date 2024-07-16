#Startup process
#Print lines to the screen to simulate an operating system booting up
#random OS boot screen stuff
import re
from time import sleep
def swordCounter():
    print('Welcome Blacksmith.'); sleep(0.5)
    print('You have been hired by the King to count swords!'); sleep(0.5)
    print('▬▬ι═══════ﺤ')
    print('o==[]::::::::::::::::>'); sleep(0.5)
    print('o===::::::::::::::::::::::>✧*:･ﾟ✧'); sleep(0.5)
    print(); sleep(0.5)

swordCounter() # runs the swordCounter function

# defining aritmetic operations = x and y are dynamic variable placeholders for user input
def add (x, y):
    return x + y
def subtract (x, y):
    return x - y
def multiply (x, y):
    return x * y
def exponent (x, y):
    return x ** y
def divide (x, y):
    return x / y
def wholeDivide (x, y):
    return x // y
def modulo (x, y):
    return x % y

# defining control menu for the user to interact with
def menu():
    print('What method will thy use to menu sword quantities?')
    print('add')
    print('subtract')
    print('multiply')
    print('exponent')
    print('divide')
    print('wholeDivide')
    print('modulo')
# open menu
menu()

# functionality of the control menu - where user may interact with the menu to use the arithmetic operators defined previously in the script
while True:
    #take input from user
    choice = input("Type in choice: ")
    #check if the choice is valid
    if choice in ('add', 'subtract', 'multiply', 'exponent', 'divide', 'wholeDivide', 'modulo'):
        num1 = float(input('Enter First Number: '))
        num2 = float(input('Enter Second Number: '))

        if choice == 'add':
            print('{} + {} = '.format(num1, num2))
            print(num1 + num2)

        elif choice == 'subtract':
            print('{} - {} = '.format(num1, num2))
            print(num1 - num2)

        elif choice == 'multiply':
            print('{} * {} = '.format(num1, num2))
            print(num1 * num2)

        elif choice == 'exponent':
            print('{} ** {} = '.format(num1, num2))
            print(num1 ** num2)

        elif choice == 'divide':
            print('{} / {} = '.format(num1, num2))
            print(num1 / num2)

        elif choice == 'wholeDivide':
            print('{} // {} = '.format(num1, num2))
            print(num1 // num2)

        elif choice == 'modulo':
            print('{} % {} = '.format(num1, num2))
            print(num1 % num2)
        # to make another calculation without closing
        repeatSwordCounter = input('Would you like to make another calculation?(y/N)')
        if repeatSwordCounter == 'N':
            break
        elif repeatSwordCounter == 'y':
            menu()
    else:
        print('Invalid Input')
