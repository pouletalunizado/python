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
player1_score = 0
player2_score = 0
# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
# initialize paddle_pos and paddle_vel
paddle1_vel, paddle2_vel = 0, 0
paddle1_pos = [0,HEIGHT/2]
paddle2_pos = [WIDTH,HEIGHT/2]
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):    
    global ball_pos, ball_vel # these are vectors stored as lists    
    if direction == "RIGHT":        
        ball_vel[0] = random.randrange(120,240)/50
        ball_vel[1] = -random.randrange(60,180)/50
    elif direction == "LEFT":
        ball_vel[0] = -random.randrange(120,240)/50
        ball_vel[1] = -random.randrange(60,180)/50

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.choice(["LEFT","RIGHT"]))

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
    global player1_score, player2_score
    paddle_width = 70
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1]-BALL_RADIUS < 0 or ball_pos[1]+BALL_RADIUS > HEIGHT:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[0] < PAD_WIDTH+BALL_RADIUS and (ball_pos[1] > paddle1_pos[1]+paddle_width/2 or ball_pos[1] < paddle1_pos[1]-paddle_width/2):
        player2_score += 1
        ball_pos = [WIDTH/2,HEIGHT/2]        
        spawn_ball("RIGHT")
    elif ball_pos[0] > WIDTH-PAD_WIDTH-BALL_RADIUS and (ball_pos[1] > paddle2_pos[1]+paddle_width/2 or ball_pos[1] > paddle2_pos[1]+paddle_width/2):
        player1_score += 1
        ball_pos = [WIDTH/2,HEIGHT/2]
        spawn_ball("LEFT")        
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS,1,'RED','RED')            
    
    # draw paddles    
    canvas.draw_line([0,paddle1_pos[1]+paddle_width/2],[0,paddle1_pos[1]-paddle_width/2],20,'White')    
    canvas.draw_line([WIDTH,paddle2_pos[1]+paddle_width/2],[WIDTH,paddle2_pos[1]-paddle_width/2],20,'White')

    # update paddle's vertical position, keep paddle on the screen        
    if paddle1_pos[1] < paddle_width/2:
        paddle1_vel = 0
        paddle1_pos[1] = paddle_width/2
    elif paddle1_pos[1] > HEIGHT-paddle_width/2:
        paddle1_vel = 0
        paddle1_pos[1] = HEIGHT-paddle_width/2
    else:
        paddle1_pos[1] += paddle1_vel   
        
    if paddle2_pos[1] < paddle_width/2:
        paddle2_vel = 0
        paddle2_pos[1] = paddle_width/2
    elif paddle2_pos[1] > HEIGHT-paddle_width/2:
        paddle2_vel = 0
        paddle2_pos[1] = HEIGHT-paddle_width/2
    else:
        paddle2_pos[1] += paddle2_vel       
    
    # determine whether paddle and ball collide    
    if ball_pos[0] <= 11+BALL_RADIUS and ball_pos[1] >= paddle1_pos[1]-paddle_width/2 and ball_pos[1] <= paddle1_pos[1]+paddle_width/2:
        ball_vel[0] = -1.1*ball_vel[0]       
    if ball_pos[0] >= WIDTH-11-BALL_RADIUS and ball_pos[1] >= paddle2_pos[1]-paddle_width/2 and ball_pos[1] <= paddle2_pos[1]+paddle_width/2:
        ball_vel[0] = -1.1*ball_vel[0]        
    # draw scores
    canvas.draw_text(str(player1_score),(WIDTH/2-60,80),50,'Red')
    canvas.draw_text(str(player2_score),(WIDTH/2+60,80),50,'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos      
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -4
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 4
   
def keyup(key):
    global paddle1_vel, paddle2_vel           
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
        
def restart():
    global paddle1_pos, paddle2_pos, ball_pos, player1_score, player2_score
    paddle1_pos = [0,HEIGHT/2]
    paddle2_pos = [WIDTH,HEIGHT/2]
    ball_pos = [WIDTH/2,HEIGHT/2]
    player1_score = 0
    player2_score = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('RESTART',restart,100)


# start frame
new_game()
frame.start()
