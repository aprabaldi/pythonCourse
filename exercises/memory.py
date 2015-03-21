# implementation of card game - Memory

import simplegui
import random

card_list = []
exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
status = 0
first_exp = 0
sec_exp = 0
turn = 0

# helper function to initialize globals
def new_game():
    global card_list, turn, exposed, first_exp, sec_exp
    first_exp = 0
    sec_exp = 0
    turn = 0
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    card_list_str = '01234567'
    card_list_str += card_list_str
    card_list = list(card_list_str)
    random.shuffle(card_list)
     
# define event handlers
def mouseclick(pos):
    global exposed, status, first_exp, sec_exp, card_list, turn
    
    card_num = pos[0] / 50
    
    if(not exposed[card_num]):
        exposed[card_num] = True
        
        if status == 0:
            status = 1
            first_exp = card_num
        elif status == 1:
            status = 2
            sec_exp = card_num
            turn += 1
        else:
            status = 1
            print first_exp,sec_exp
            print card_list[first_exp],card_list[sec_exp]
            if( card_list[first_exp] != card_list[sec_exp] ):
                exposed[first_exp] = False
                exposed[sec_exp] = False
            first_exp = card_num
        
    
                    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_list, exposed
    i = 0
    for card in card_list:
        if(exposed[i]):
            canvas.draw_text(str(card), [(50 * (i + 1)) - 30,55], 20, "Red")
        else:
            canvas.draw_line([(50 * (i + 1)) - 25,0], [(50 * (i + 1)) - 25,100], 50, "Green")
            canvas.draw_line([(50 * (i + 1)),0], [(50 * (i + 1)),100], 1, "White")
        
        i += 1
    label.set_text('Turns = ' + str(turn))   


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
