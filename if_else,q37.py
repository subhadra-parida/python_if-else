# Write a python program to sum of two given integers.
# However if the sum is beetween 15 to 20 it will be return 20....
num1=int(input("enter any number="))
num2=int(input("enter any number="))
sum=num1+num2
if sum in range(15,20):
    print(sum,"it will return 20")
else:
    print(sum,"it will not return 20")

    