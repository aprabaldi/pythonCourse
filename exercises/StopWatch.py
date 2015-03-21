# template for "Stopwatch: The Game"

# define global variables
import simplegui
seconds = 0
attempts = 0
hits = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(input):
    decisec = str(input % 10)
    seconds = input/10 % 1000
    minutes = str(seconds / 60)
    seconds = str(seconds % 60)
    if(len(seconds) == 1):
        seconds = '0' + seconds
    return minutes + ':' + seconds + '.' + decisec    

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
def stop_handler():
    global hits,attempts,seconds
    if(timer.is_running()):
        timer.stop()
        attempts += 1
        if((seconds % 10) == 0):
            hits +=1
def reset_handler():
    global seconds,hits,attempts
    timer.stop()
    seconds = 0
    hits = 0
    attempts = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global seconds
    seconds += 1

# define draw handler
def draw_handler(canvas):
    global seconds,hits,attempts
    canvas.draw_text(format(seconds), (30, 175), 100, 'White')
    canvas.draw_text(str(hits) + '/' + str(attempts), (220, 30), 30, 'Red')
    
# create frame
frame = simplegui.create_frame("StopWatch",300,300)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
button_start = frame.add_button('Start', start_handler)
button_stop = frame.add_button('Stop', stop_handler)
button_reset = frame.add_button('Reset', reset_handler)

# start frame
frame.start()


# Please remember to review the grading rubric
