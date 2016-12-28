# Tim Jordan and Daniel Wilson
# 8/20/2016
# Project 1 Let's Play a Game

# This program is coded to play "rock, paper, scissors, lizard, spock" with the user.
import random

# I created a function so that the game could be called again after the game is played.
def game():
	print

# This part consisted of the player's input that would then be made lowercase so that 
# the program can read the input regardless of case.
	human_raw = raw_input("You have challenged the computer master to a game of \
\"rock, paper, scissors, lizard, Spock.\" Choose one or input q to quit: ")
	human = human_raw.lower()

# Here I listed the possiblities that the computer could choose then used a function
# that would randomly select a choice from the given list.
	options = ["rock","paper","scissors","lizard","spock"]
	cpu = random.choice(options)

# Below I used if and elif statements to create all of the potential scenarios for what
# the user and what the computer might select, printing the selected options and the
# results. The section below are all the possiblities of the human winning.
	if human == "q" or human == "quit":
		print "You'd better run."
	else:
		if human == "scissors" and cpu == "paper":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Scissors cut paper, you win!"
	
		elif human == "paper" and cpu == "rock":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Paper covers rock, you win!" 
	
		elif human == "rock" and cpu == "lizard":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Rock crushes lizard, you win!" 

		elif human == "lizard" and cpu == "spock":
			print
			print "You chose %s and the computer chose %s." % (human, cpu) 
			print "Lizard poisons Spock, you win!" 
	
		elif human == "spock" and cpu == "scissors":
			print 
			print "You chose %s and the computer chose %s." % (human, cpu) 
			print "Spock smashes scissors, you win!"

		elif human == "scissors" and cpu == "lizard":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Scissors decapitate lizard, you win!"

		elif human == "lizard" and cpu == "paper":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Lizard eats paper, you win!"
	
		elif human == "paper" and cpu == "spock":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Paper disproves Spock, you win!" 
	
		elif human == "spock" and cpu == "rock":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Spock vaporizes rock, you win!"
	
		elif human == "rock" and cpu == "scissors":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Rock crushes scissors, you win!"
	
# The section below this are all the possibilities of the human losing.
		elif cpu == "scissors" and human == "paper":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Paper is cut by scissors, you lose!"
	
		elif cpu == "paper" and human == "rock":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Rock is covered by paper, you lose!" 
	
		elif cpu == "rock" and human == "lizard":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Lizard is crushed by rock, you lose!"
	
		elif cpu == "lizard" and human == "spock":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Spock is poisoned by lizard, you lose!"
	
		elif cpu == "spock" and human == "scissors":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Scissors are smashed by Spock, you lose!" 
	
		elif cpu == "scissors" and human == "lizard":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Lizard is decapitated by scissors, you lose!"
	
		elif cpu == "lizard" and human == "paper":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Paper is eaten by lizard, you lose!" 
	
		elif cpu == "paper" and human == "spock":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Spock is disproved by paper, you lose!"
	
		elif cpu == "spock" and human == "rock":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Rock is vaporized by Spock, you lose!" 
	
		elif cpu == "rock" and human == "scissors":
			print
			print "You chose %s and the computer chose %s." % (human, cpu)
			print "Scissors are crushed by rock, you lose!"
	
# I inclueded the possiblity of a tie, where the inputs of the human and cpu are the same.
		elif human == cpu:
			print 
			print "You and the computer both chose %s" % (human)
			print "It's a tie!"
	
# Here I created and error message for if the user input any other words than choices
# offered by the game.
		elif human != "rock" or human != "paper" or human != "scissors" or human != "lizard" or human != "spock":
			print
			print "Error, invalid input."
		
	        game()

game()






