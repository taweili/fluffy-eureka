# generate a random number between 1 and 10 inclusive using python

import random

number = random.randint(1, 10)
print(number)

# write a function that generate a random number between 1 and 10 inclusive using python

def generate_random_number():
    return random.randint(1, 10)
random_number = generate_random_number()
print(random_number)

def print_random_number():
    print(generate_random_number())

print_random_number()

# write a function to generate random numbers between 1 and 100 
import random

def generate_random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]

# implement a bubble sort algorithm to sort the list of numbers 
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# write a function to add two numbers
def add_two_numbers(a, b):
  return a + b

# write a function to sum up three numbers
def sum_three_numbers(a, b, c):
    """
    This function takes three arguments and returns their sum.
    
    Parameters:
        a (int): The first number.
        b (int): The second number.
        c (int): The third number.
        
    Returns:
        int: The sum of the three numbers.
    """
    return a + b + c
