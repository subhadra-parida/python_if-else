# Number is divisible by both/5 or 11 ...........
number=int(input("enter any number"))
if number%5==0 and number%11==0:
    print(number,"is divisible by both")
else:
    print(number,"is not divisible by both")