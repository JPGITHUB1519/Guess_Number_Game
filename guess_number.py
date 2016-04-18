from random import randint 

def generar_aleatorio(mini,maxi) :

	return randint(mini,maxi)

def analize_number(number, random_number) :

	if(number < random_number) :

		print "The Guess number is greater than your input"

	if(number > random_number) :

		print "The Guess number is less than your input"


analize_number(5, generar_aleatorio(0,10))