# Accept the number of days from the user & calculate 
# the charge for library according to  following......
# 1st five days:RS 2/days.
# 6-10 days: RS 3/days.
# 10-15 days: RS 4/days.
# After 15 days :RS 5/days.
num=int(input("enter any numvber="))
if num<=5:
    print(num*2)
elif num>=6 and num<=10:
    print(num*3)
elif num>=10 and num<=15:
    print(num*4)
elif num>=15:
    print(num*5)
    