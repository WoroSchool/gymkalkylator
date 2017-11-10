#Test till programmet gymkalkylator
def totalvikt(x):
	plattorvikt = vikt - 20 
	print(plattorvikt)
	return plattorvikt

def antalplattor(x):
	plattorvikt = totalvikt(vikt)
	while plattorvikt > 70:
		plattorvikt = plattorvikt // vikter[0]
		print(plattorvikt)
		if plattorvikt < 70:
			plattorvikt = plattorvikt // vikter[1]
			print(plattorvikt)
		elif plattorvikt < 60:
			print()



vikter = [25,20,15,10,5,2.5,1.25]


print (vikter,'plattor')

vikt = int(input('Hur mycket vikt vill du ha?: '))

totalvikt(vikt)
antalplattor(totalvikt)
