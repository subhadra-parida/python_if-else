# Accept three numbers from the user & display the 2nd largest number......
num1=int(input("enter any number="))
num2=int(input("enter any number="))
num3=int(input("enter any number="))
if num1>num2 and num1<num3:
    print(num1,"is second largest number")
elif num2>num1 and num2<num3:
    print(num2,"is second largest number")
elif num3>num1 and num3<num2:
    print(num3,"is second largest number")
    