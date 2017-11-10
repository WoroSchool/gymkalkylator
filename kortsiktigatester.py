#Random inget som sparas en längre tid
#Test till programmet gymkalkylator
def totalvikt(x):
	plattorvikt = vikt - 20 
	return plattorvikt

def antalplattor(x):
	plattorvikt = totalvikt(vikt)
	print('Plattornas vikt:',plattorvikt)
	if plattorvikt >= 50:
		antal25 = plattorvikt // int(vikter[0])
		print(1*antal25)
	else:
		print('NEJ')



vikter = [25,20,15,10,5,2.5,1.25]


print (vikter,'plattor')

vikt = int(input('Hur mycket vikt vill du ha?: '))

totalvikt(vikt)
antalplattor(totalvikt)

