# How to print guessing game in python using if else........
import random
my_num=random.randint(0,9)
print("Hello!!! Friends I have a number, please guess it:-")
F_num=int(input("Enter any number="))
if my_num==F_num:
    print("Congratulation!!!, Your number is correct.")
elif my_num>F_num:
    print("My number is greater than your number.")
else:
    print("My number is smaller than your number")
