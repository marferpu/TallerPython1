# Create a Python program that converts a temperature from Fahrenheit to Celsius.
# The user should enter the temperature in Fahrenheit, and the program should print
# the equivalent temperature in Celsius.

def temperatureFunction(num1:int):
    celsius = (num1-32)/1.8
    return celsius

fahrenheit = int(input('Give a Fahrenheit temperature: '))

result = temperatureFunction(fahrenheit)
print(f'Fahrenheit temperature: {fahrenheit}°F is in Celsius temperature: {result}°C')