#Test till programmet gymkalkylator
def totalvikt(x):
	plattorvikt = vikt - 20 
	print(plattorvikt)
	return plattorvikt

def antalplattor(x):
	plattorvikt = totalvikt(vikt)
	while plattorvikt > 50:
		antal25 = plattorvikt // int(vikter[0])
		print(antal25)
		return antal25
		if plattorvikt < 50:
			plattorvikt = plattorvikt // vikter[1]
			print(plattorvikt)
		elif plattorvikt < 40:
			print()



vikter = [25,20,15,10,5,2.5,1.25]


print (vikter,'plattor')

vikt = int(input('Hur mycket vikt vill du ha?: '))

totalvikt(vikt)
antalplattor(totalvikt)
