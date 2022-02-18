# STRONG PASSWORD.......
password=input("enter the password:")
if password>="A" and password<="Z" and password>="a" and password<="b" and password>="0" and password<="9"and password or "@" in password or "#" in password or "&" in password and len(password)>=6 and len(password)<=12:
	print("strong password")
else:
	print("wrong password")


# pw=input("enter a password")
# if (pw>="a" and pw<="z" ) or (pw<="A" and pw>="Z") or (pw<="0" and pw>="9") or (pw=="#",pw=="%",pw=="$",pw=="@",pw=="&",pw=="₹",pw=="_"):
# 	if len(pw)>=6 and len(pw)<=20:
# 		print("strong password")
# 	else:
# 		print("wrong pasword")
# else:
# 	print("wrong paasword")