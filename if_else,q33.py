# Write aprogram to accept the cost of price & display the road tax 
# to be paid according to the following criteria.....
# no.  Cost-Price(in RS).             Tax.
#  1      >1,00,000                   15%
#  2      >50,000 and <=1,00,000      10%
#  3      <=50,000                     5%
Tax=int(input("enter any number="))
if Tax>100000:
    print("Tax to be paid 15%")
elif Tax>50000 and Tax<100000:
    print("Taxc to be paid 10%")
elif Tax<=50000:
    print("Tax to be paid 5%")