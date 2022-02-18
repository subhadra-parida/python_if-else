# ATM QUESTION...........
print("WELCOME TO SBI BANK")
print("Please insert your ATM card")
print("Hi,Please don't remove your chip card.Leave your card inserted during entire transaction")
Language=input("enter any language=")
if Language=="English":
    print("Thanks for English Language")
if Language=="Hindi":
    print("Thanks for Hindi Language")
if Language=="Odia":
    print("Thanks for Odia Language")
if Language=="Telugu":
    print("Thanks for Telugu Language")
Number=int(input("enter any two number between 10 to 99="))
if Number>10 and Number<99:
    print("Yes")
else:
    print("No")
print("Please enter your ATM number")
print("Please choosing Banking for cash withdrawal")
print("Please press your withdrawal transaction")
print("Please select our 'saving' account type")
ammount=int(input("Enter your ammount="))
if ammount>=100 and ammount<=20000:
    print("yes,cash is available")
else:
    print("No,Cash is not available")
print("Your transaction is being processed")
print("Collect your cash please")
print("Transaction is complete")
print("Available balance")