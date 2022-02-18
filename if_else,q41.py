# Write a python program to get next day of given date......
DD=int(input("enter any date="))
MM=int(input("enter any month="))
YYYY=int(input("enter any year="))
if DD+1 and MM+1 and YYYY+1:
    print(YYYY/DD/MM)
else:
    print("not")