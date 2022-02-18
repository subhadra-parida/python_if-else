# Electricity question....
# for first 50 units RS.0.50 / Unit.
# for next 100 units RS.0.75 / Unit.
# for next 100 units RS.1.20 / Unit.
# for unit above 250 units RS.1.50 / Unit.
Electricity=input("Enter any unit charge=")
Calculate=(50+100+100+250)
if Electricity<="50 Units":
    print("RS.0.50/Unit")
elif Electricity<="100 Units":
    print("RS.0.75/Unit")
elif Electricity<="100 Units":
    print("RS.1.20/ Unit")
elif Electricity<="250 units":
    print("RS.1.50/Units")
    