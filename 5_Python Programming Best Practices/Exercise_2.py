# Create a Python decorator called timer that measures the time taken to execute a
# function. Use this decorator on a function that sorts a list of random numbers and
# prints the sorted list.

import datetime
import random

def timer(list):
    time_init = datetime.datetime.now()
    sorting_list(list)
    time_end = datetime.datetime.now()
    time = time_end - time_init
    print(f'The time taken to execute the function was {time}')

def sorting_list(list):
    list.sort()
    print(f'The sorted list is: ### {list} ###')

list_desorted = random.sample(range(1, 100), 25)
print(f'The desorded list is: *** {list_desorted} ***')

timer(list_desorded)