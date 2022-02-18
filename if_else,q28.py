# write a program to input marks of five subjects(Physics,Chemestry,Biology,Mathematics & Computer) calculate perrive subjects
# (Physics,Chemestry,Biology,Mathematics & Computer) calculate percentage and
# # grade according to following......

# Percentage >= 90% - Grade A
# Percentage >= 80% - Grade B
# Percentage >= 70% - Grade C
# Percentage >= 60% - Grade D
# Percentage >= 50% - Grade E
# Percentage <  40% - Grade F

Physics=int(input("enter any number="))    
Chemestry=int(input("enter any number="))
Biology=int(input("enter any number="))
Mathematics=int(input("enter any number="))
Computer=int(input("enter any number="))
Percentage=(Physics+Chemestry+Biology+Mathematics+Computer*5/100)
if Percentage >= 90:
    print("Grade A")
elif Percentage >= 80:
    print("Grade B")
elif Percentage >= 70:
    print("Grade c")
elif Percentage >= 60:
    print("Grade D")
elif Percentage >= 50:
    print("Grade E") 
elif Percentage < 40:
    print("Grade F")
