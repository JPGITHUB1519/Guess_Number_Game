from random import randint 

def generar_aleatorio(mini,maxi) :

	return randint(mini,maxi)

def analize_number(number, random_number) :

	if(number < random_number) :

		print "\nThe Guess number is greater than your input"
		return False

	if(number > random_number) :

		print "\nThe Guess number is less than your input"
		return False
	return True
	
def main_function() :

    print "\nInput the Numbers of Oportunities"
    oportunities = int(input())

    cond = False

    print "\nInput the max : "
    mini = int(input())

    print "\nInput the min : "
    maxi = int(input())
    ale = generar_aleatorio(mini,maxi)

    while(oportunities > 0) :

        print "\nOportunities : ", oportunities

        print "\n Input the number you guess : "
        number = int(input())

        if(analize_number(number, ale)) == True :

            print "\nCongratulation, You win. The guess Number is ", ale
            cond = True
            return
        else :

            oportunities = oportunities - 1;

    print "\n\nYou Loose, The Guess Number was ", ale
            
main_function()

        
    
 

        


