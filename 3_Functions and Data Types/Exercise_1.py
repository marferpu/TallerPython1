# Write a Python function called find_maximum that takes a list of numbers as input
# and returns the maximum number from the list.

def find_maximum(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

array_test = [1,6,3,4]
print(f' The maximum number is {find_maximum(array_test)}')
    
    