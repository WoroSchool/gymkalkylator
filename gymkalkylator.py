#Ska visa hur många plattor du ska ha på stången
print('Svara med ja/nej.')

vikter = [25,20,15,10,5,2.5,1.25]

def stång(x):
	x = 20

def totalvikt(x, y, z, c, v, b, n):
	stång + 25*x, 20*y, 15*z, 10*c, 5*v, 2.5*b, 1.25*n

platta25 = input('Har du 25kgs plattor?: ')

if str(platta25) == 'ja':
	platta25 = True
else:
	platta25 = False

running = True

while running == True:
	vikt = int(input('Hur mycket vikt ska du använda?: '))
	print(str(vikt+'kg'))
	answer = input('Vill du fortsätta? (JA eller NEJ) ')
	if answer.upper() == 'NEJ':
    	running = False
	if answer.upper() == 'JA':
   		running = True
	else:
   		running = False
input('END')


