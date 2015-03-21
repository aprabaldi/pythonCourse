# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
direction = LEFT
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
score2 = 0
score1 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH/2,HEIGHT/2]
    
    hor_speed = random.randrange(120, 240)
    ver_speed = random.randrange(60, 180)
    
    if(direction == LEFT):
        hor_speed = - hor_speed
    ver_dir = random.randint(0, 1)
    if ver_dir:
        ver_speed = - ver_speed
    
    ball_vel = [hor_speed/60.0,ver_speed/60.0]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global direction
    score1 = 0
    score2 = 0
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score2), [WIDTH / 2 - 50, 40], 30, 'White')
    canvas.draw_text(str(score1), [(WIDTH / 2) + 30, 40], 30, 'White')
    
    # update ball
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] <= paddle2_pos + (PAD_HEIGHT / 2) and ball_pos[1] >= paddle2_pos - (PAD_HEIGHT / 2):
            ball_vel[0] *= - 1.10
            ball_vel[1] *= 1.10
        else:
            score1 += 1
            spawn_ball(RIGHT)
            
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] <= paddle1_pos + (PAD_HEIGHT / 2) and ball_pos[1] >= paddle1_pos - (PAD_HEIGHT / 2):
            ball_vel[0] *= - 1.10
            ball_vel[1] *= 1.10
        else:
            score2 += 1
            spawn_ball(LEFT)
    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
            
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 5, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    final_pad1_pos = paddle1_pos + paddle1_vel
    final_pad2_pos = paddle2_pos + paddle2_vel
    if final_pad1_pos >= PAD_HEIGHT / 2 and final_pad1_pos <= HEIGHT - PAD_HEIGHT / 2:
        paddle1_pos = final_pad1_pos
    if final_pad2_pos >= PAD_HEIGHT / 2 and final_pad2_pos <= HEIGHT - PAD_HEIGHT / 2:
        paddle2_pos = final_pad2_pos
    
    # draw paddles
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle1_pos - PAD_HEIGHT / 2],[WIDTH - HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT / 2], PAD_WIDTH, "Red")
    canvas.draw_line([HALF_PAD_WIDTH, paddle2_pos - PAD_HEIGHT / 2],[HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT / 2], PAD_WIDTH, "Red")
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel -= 2        
    if key == simplegui.KEY_MAP['down']:
        paddle1_vel += 2
    if key == simplegui.KEY_MAP['w']:
        paddle2_vel -= 2
    if key == simplegui.KEY_MAP['s']:
        paddle2_vel += 2

def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel += 2
    if key == simplegui.KEY_MAP['down']:
        paddle1_vel -= 2
    if key == simplegui.KEY_MAP['w']:
        paddle2_vel += 2
    if key == simplegui.KEY_MAP['s']:
        paddle2_vel -= 2
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()
