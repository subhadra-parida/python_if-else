# write apython program weather a triangle is Equilater/Isoscale/Scalane or NOT........
a=int(input("ente r any number="))
b=int(input("enter any number="))
c=int(input("enter any number="))
if a==b==c and a+b+c==180:
    print("Equilater")
if a==b and a==c and a+b+c==180:
    print("isoscale")
if a!=b and b!=c and c!=a and a+b+c==180:
    print("Scalane")
else:
    ("not")
