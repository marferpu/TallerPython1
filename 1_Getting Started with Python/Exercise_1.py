# Write a Python program that takes two numbers as input from the 
# user and prints their sum.

def sum(variable1:int, variable2:int):
    return variable1+variable2

num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))

# num1 = int(num1)


result = sum(num1,num2)
print('The sum is: ', result)