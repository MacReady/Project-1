# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


import random

def number_to_name(number):


    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    

def name_to_number(name):


    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    
    



def rpsls(name): 

    
    
    
    comp_number = random.randrange(0, 5)
    result = (comp_number - player_number) % 5
    player_name = number_to_name

    if result == 1 or result == 2:
        print ('Player chooses', number_to_name(name))
        print ('Computer chooses', number_to_name(comp_number))
        print ('Computer wins!')
        print ()
    elif result == 3 or result == 4:
        print ('Player chooses', number_to_name(name))
        print ('Computer chooses', number_to_name(comp_number))
        print ('Player wins!')
        print ()
    elif result == 0:
        print ('Player chooses', number_to_name(name))
        print ('Computer chooses', number_to_name(comp_number))
        print ('Player and computer tie!')
        print ()


    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric




