a=open("name.txt","r")
c=0
for i in a:
    if a[i]!=" ":
        c=c+1
    print(c)
a.close()
