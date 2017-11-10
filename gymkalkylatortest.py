#Räkna plattor för stången
def totalvikt(x):
	plattorvikt = vikt - 20 
	print(plattorvikt,'kg')
	return plattorvikt

def antalplattor(x):
	plattorvikt = totalvikt(vikt)
	if plattorvikt >= 50:
		antal25 = plattorvikt // int(vikter[0])
		print(antal25,'st 25kg plattor')
		return antal25
	elif plattorvikt - antal25 * int(vikter[0]) < 50:
		antal20 = (plattorvikt - antal25 * int(vikter[0])) // int(vikter[1])
		print(antal20,'st 20kg plattor')
		return antal20
	elif plattorvikt - antal25 * int(vikter[0]) - antal20 * int(vikter[1]) < 40:
		antal15 = (antal25 * int(vikter[0]) - antal20 * int(vikter[1])) // int(vikter[2])
		print(antal15,'st 15kg plattor')
		return antal15
	elif plattorvikt - antal25 * int(vikter[0]) - antal20 * int(vikter[1]) > 40:
		antal10 = (plattorvikt - antal25 * int(vikter[0]) - antal20 * int(vikter[1]) - antal15 * int(vikter[2]))


vikter = [25,20,15,10,5,2.5,1.25]


print (vikter,'plattor')

vikt = int(input('Hur mycket vikt vill du ha?: '))
antalplattor(totalvikt)
