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
UP=False
DOWN=True
direction=[LEFT,UP]
ball_pos=[100,100]
ball_vel=2
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if direction[0]==False:
        ball_pos[0]-=ball_vel     
    else:
        ball_pos[0]+=ball_vel    
    if direction[1]==False:
        ball_pos[1]-=ball_vel
    else:
        ball_pos[1]+=ball_vel

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos=0
    paddle2_pos=0
    paddle1_vel=40
    paddle2_vel=40
    print "a"
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global direction
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    
    if ball_pos[0]<0: #and direction==LEFT:
        direction[0]=RIGHT
        #print direction
    elif ball_pos[0]>WIDTH - PAD_WIDTH:#and direction==RIGHT:
        direction[0]=LEFT  
    if ball_pos[1]<0: #and direction==LEFT:
        direction[1]=DOWN
        #print direction
    elif ball_pos[1]>HEIGHT: #and direction==RIGHT:
        direction[1]=UP  
    spawn_ball(direction)
    # draw ball
    canvas.draw_circle(ball_pos, 20, 5, 'White','White')

    # update paddle's vertical position, keep paddle on the screen
    
    # draw paddles
    canvas.draw_polygon([[0,  paddle1_pos],[0, paddle1_pos+PAD_HEIGHT],[PAD_WIDTH/2, paddle1_pos+PAD_HEIGHT],[PAD_WIDTH/2,  paddle1_pos]], 10, 'White')
    canvas.draw_polygon([[WIDTH - PAD_WIDTH,  paddle2_pos],[WIDTH - PAD_WIDTH, paddle2_pos+PAD_HEIGHT],[WIDTH - PAD_WIDTH+PAD_WIDTH/2, paddle2_pos+PAD_HEIGHT],[WIDTH - PAD_WIDTH+PAD_WIDTH/2,  paddle2_pos]], 6, 'White')
    # determine whether paddle and ball collide 
    string=""
    if ball_pos[0]<=BALL_RADIUS and (ball_pos[1]+BALL_RADIUS>paddle1_pos-PAD_HEIGHT and ball_pos[1]-BALL_RADIUS<paddle1_pos+PAD_HEIGHT):
        string="left"
        canvas.draw_text(string,[40,69],20,'White')
    if ball_pos[0]>=WIDTH - PAD_WIDTH and (ball_pos[1]+BALL_RADIUS>paddle2_pos-PAD_HEIGHT and ball_pos[1]-BALL_RADIUS<paddle2_pos+PAD_HEIGHT):
        string="right"
        canvas.draw_text(string,[540,69],20,'White')
    # draw scores
    string=""
def keydown(key):
    global paddle1_vel, paddle2_vel
    global paddle1_pos,paddle2_pos
    
    if key==simplegui.KEY_MAP["down"] and paddle1_pos<312:
        paddle1_pos+= paddle1_vel
    elif key==simplegui.KEY_MAP["S"] and paddle2_pos<312:
        paddle2_pos+= paddle2_vel
def keyup(key):
    global paddle1_vel, paddle2_vel
    global paddle1_pos,paddle2_pos
    
    if key==simplegui.KEY_MAP["up"] and paddle1_pos>0:
        paddle1_pos-= paddle1_vel
    elif key==simplegui.KEY_MAP["W"]and paddle2_pos>0:
        paddle2_pos-= paddle2_vel
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
keyup(1)
