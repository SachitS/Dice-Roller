import random
def decor(a):
	if(a==1):
		print(" = = = = = = ")
		print("||         ||")
		print("||    1    ||")
		print("||         ||")
		print(" = = = = = = ")
	if(a==2):
		print(" = = = = = = ")
		print("|| 2       ||")
		print("||         ||")
		print("||       2 ||")
		print(" = = = = = = ")
	if(a==3):
		print(" = = = = = = ")
		print("|| 3       ||")
		print("||    3    ||")
		print("||       3 ||")
		print(" = = = = = = ")
	if(a==4):
		print(" = = = = = = ")
		print("|| 4     4 ||")
		print("||         ||")
		print("|| 4     4 ||")
		print(" = = = = = = ")
	if(a==5):
		print(" = = = = = = ")
		print("|| 5     5 ||")
		print("||    5    ||")
		print("|| 5     5 ||")
		print(" = = = = = = ")
	if(a==6):
		print(" = = = = = = ")
		print("|| 6     6 ||")
		print("|| 6     6 ||")
		print("|| 6     6 ||")
		print(" = = = = = = ")
	return 0
	
roll=(input("Roll?: Y or N : ")).upper()
while(roll=="Y"):
	a=random.randrange(1,7,1)
	decor(a)
	roll=(input("Roll again?: Y or N : ")).upper()