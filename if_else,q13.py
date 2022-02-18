# Write a programm which is greater or which is less....
a=int(input("enter any number"))
b=int(input("enter any number"))
c=int(input("enter any number"))
if a>=b and a>=c:
    print(a,"is greter than b and c")
elif b>=a and b>=c:
    print(b,"is greater then a and c")
elif c>=a and c>=b:
    print(c,"is greater than a and b")
elif a<=b and a<=c:
    print (a,"is less than b and c")
elif b<=a and b<=c:
    print(b,"is less than a and c")
elif c<=a and c<=b:
    print(c,"is less than a and b")