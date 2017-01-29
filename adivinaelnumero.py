# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math

# global variables
number_range = 100
secret_number = 0
count = 0




#header
print "Welcome to Guess the Number" 
print " "
print "Select and option from the control pane,"
print "then type your first guess"
print "Game 1-100 allows 7 guesses, Game 1-1000 allows 10 guesses"
print "- - - - - - - - - - - - - - - - - - - - "
print " "

# helper function to start and restart the game
def new_game():
    global number_range
    global secret_number
    global count
    
    secret_number = random.randrange(0, number_range)
    
    if number_range == 100:
        count = 7
    else:
        count = 10


# define event handlers for control panel
def range100():
    global number_range
    number_range = 100
    new_game()

def range1000():
    global number_range
    number_range = 1000
    new_game()

    
def input_guess(guess):
    global secret_number
    global count 
    
    count = count - 1
    if count > 0:
        
        print "You guessed:  " + guess

        int_guess = int(guess)

        if int_guess == secret_number:
            print "Congratulations, you guessed the number!"
            print " "

        elif int_guess > secret_number:
            print "Lower!!"
            print "You now have " + str(count) + " remaining." 
            print " "

        else:
            print "Higher!!"
            print "You now have " + str(count) + " remaining."
            print " "
    
    else:
        print "- - - - -"
        print "SORRY YOU ARE OUT OF GUESSES!"
        print "The number was " + str(secret_number)
        print " "
        print "Let's try again!"
        print "- - - - -"
        new_game()
        


  
    
    
# create frame
frame = simplegui.create_frame("Guess the Number", 10, 300)


# register event handlers for control elements and start frame
frame.add_button("Range 0-100", range100, 200)
frame.add_button("Range 0-1000", range1000, 200)
frame.add_input("Type guess and press Enter", input_guess, 200)
frame.add_button("Reset", new_game, 200)

# call new_game 
new_game()
frame.start() 

# always remember to check your completed program against the grading rubric
