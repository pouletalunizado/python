# first example of drawing on the canvas

import simplegui

# define draw handler
def draw(canvas):
    canvas.draw_text("Hello!",[100, 100], 24, "Yellow")
    canvas.draw_circle([100, 100], 2, 2, "Blue")
    canvas.draw_circle([119, 100], 2, 2, "Blue")
    canvas.draw_circle([150, 100], 2, 2, "Blue")
    canvas.draw_circle([156, 100], 2, 2, "Blue")
    canvas.draw_circle([158, 100], 2, 2, "Blue")
    canvas.draw_circle([197, 100], 2, 2, "Blue")
    canvas.draw_circle([189, 100], 2, 2, "Blue")
    canvas.draw_circle([156, 100], 2, 2, "Blue")
    canvas.draw_circle([156, 100], 2, 2, "Blue")

# create frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register draw handler    
frame.set_draw_handler(draw)

# start frame
frame.start()