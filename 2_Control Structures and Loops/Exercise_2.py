# Create a Python program that checks if a given number is prime or not. The user
# should input a number, and the program should print whether it is prime or not.}

def prime(num):
    if num and num % 2 != 0:
        return f"The number {num} is prime"
    return f"The number {num} is not prime"
    
num = int(input('Write a number: '))

print(prime(num))