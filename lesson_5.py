# import random
from random import  randint as generate_number
from utils import calculator as calc
from utils.person import Student
from termcolor import cprint

# print(random.randint(1,6))
print(generate_number(1,6))
print(calc.addition(9, 1))

my_friend = Student('Kevin',29)
print(my_friend)
cprint("Hello, World!", "green", "on_red")
