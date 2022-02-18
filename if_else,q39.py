# write a program to find the median of three values .....
num1=int(input("enter any number="))
num2=int(input("enter any number="))
num3=int(input("enter any number="))
if num1>num2:
    if num1<num3:
        median=num2
    else:
        median=num3
else:
    if num1>num3:
        median=num1
    elif num2<num3:
        median=num2
    else:
        median=num3
    print("The median is",median)