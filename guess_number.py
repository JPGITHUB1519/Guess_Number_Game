from random import randint 

def generar_aleatorio(mini,maxi) :

	return randint(mini,maxi)

def analize_number(number, random_number) :

	if(number < random_number) :

		print "The Guess number is greater than your input"
		return False

	if(number > random_number) :

		print "The Guess number is less than your input"
		return False
	return True
	



        
    
 

        


