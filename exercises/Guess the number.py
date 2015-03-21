import simplegui
import random

#starts new game
def new_game():
    global secret_number
    global attempts
    global rnd_range
    
    secret_number = random.randrange(0, rnd_range)
    attempts = 0
    print "\nNew Game started with a range of", rnd_range

#defines de range to 100 and its variables and starts new game
def range100():
    global max_attempts
    global rnd_range
    
    max_attempts = 7
    rnd_range = 100
    new_game()

#defines de range to 100 and its variables and starts new game
def range1000():
    global max_attempts
    global rnd_range
    
    max_attempts = 10
    rnd_range = 1000
    new_game()
    
#handler for the guess input
def input_guess(guess):
    global secret_number
    global attempts
    global max_attempts
    
    correct = False
    attempts += 1
    print  
    guess_int = int(guess)
    print "Guess was", guess_int
    if(secret_number > guess_int):
        print "Higher"
    elif(secret_number < guess_int):
        print "Lower"
    else:
        correct = True
        print "Correct"
        new_game()
    attempts_left = max_attempts - attempts
    if(attempts_left == 1):
        print "1 attempt left... Last chance..."
    elif(attempts_left == 0):
        if(not correct):
            print "That's it,", max_attempts, "attempts, try again!"
            new_game()
    else:
        print max_attempts - attempts, "attempts left"    

#frame creation
frame = simplegui.create_frame('Guess de number!', 300, 300)

#frame additions
frame.add_input("Guess",input_guess,100)
frame.add_button('New Game', new_game)
frame.add_button('Range: 0 - 100', range100)
frame.add_button('Range: 0 - 1000', range1000)

#I don't use new_game to start the game, I changed a little bit
#the implementation to start the game with a default range of 100.
#Looks nicer to me.
range100()