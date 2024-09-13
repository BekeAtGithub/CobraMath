#Intro - Welcome to Calcuatron - a simple calculator script 

#Startup process 
#Print lines to the screen to simulate an operating system booting up
#random OS boot screen stuff 
#maybe a text picture of brand
#greeting screen where your brand says hello
from time import sleep
def Calcuatron():
    print('Starting Calcuatron OS_1.0..........'); sleep(0.5)
    print('Hungarian Nerd is testing extended memory....'); sleep(0.5)
    print('                              done....'); sleep(0.5)
    print('Virtual Machine Folder Sharing'); sleep(0.5)
    print('Copyright (C) 2020 Hungarian Nerd Corp. All Rights Reserved')
    print(); sleep(0.5)
    print('  _____________________  '); sleep(0.25)
    print(' |  _________________  | '); sleep(0.25)  
    print(' | | CM           0.1| | '); sleep(0.25)
    print(' | |_________________| | '); sleep(0.25)
    print(' |  ___ ___ ___   ___  | '); sleep(0.25)
    print(' | | 7 | 8 | 9 | | + | | '); sleep(0.25)
    print(' | |___|___|___| |___| | '); sleep(0.25)
    print(' | | 4 | 5 | 6 | | - | | '); sleep(0.25)
    print(' | |___|___|___| |___| | '); sleep(0.25)
    print(' | | 1 | 2 | 3 | | x | | '); sleep(0.25)
    print(' | |___|___|___| |___| | '); sleep(0.25)
    print(' | | . | 0 | = | | / | | '); sleep(0.25)
    print(' | |___|___|___| |___| | '); sleep(0.25)
    print(' |_____________________| '); sleep(0.25)
    print(); sleep(0.50)
    print('     CALCULATRON   ')



Calcuatron()    # << name of my bootup function

#programming calculator function
#addition function
def add(x, y):
    return x + y

#subtraction function
def subtract(x, y):
    return x - y

#multiplication function
def multiply(x, y):
    return x * y

#division function
def divide(x, y):
    return x / y

print('Select operation.')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')

while True:
    #take input from the user
    choice = input("Enter choice(1/2/3/4):  ")

    #check if choice is on of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print('Invalid Input')

#to make another calculation without closing        
#repeatcalculation = input('Would you like to make another calculation?(y/N)')

#while repeatcalculation = 'y':







