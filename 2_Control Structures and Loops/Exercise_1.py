# Write a Python program that prints the first 10 Fibonacci 
# numbers using a loop.

import sys

def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print('Ten first fibonacci numbers ', [fibonacci(i) for i in range(1,11)])