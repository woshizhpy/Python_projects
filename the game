import simplegui
# template for "Stopwatch: The Game"

# define global variables
time=0
t=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    #print 1
    global t
    timer1.start()
    print t
    return
def Stop():
    timer1.stop()
    print t
    return
def Reset():
    #print 3
    print t
    return

# define event handler for timer with 0.1 sec interval
def timer():
    global time
    global t 
    time=time+1
    if time%25==0:
        t=t+0.1
        print t
#  t1=int(t)
#    if t1==1:
#       print t,"5s!"
    return

# define draw handler
def draw(canvas):
    canvas.draw_text(str(timer1.is_running()),[100,100],24,'Red')
    return

    
# create frame
frame=simplegui.create_frame("The game",300,200)
button1=frame.add_button("Start",Start,100)
button2=frame.add_button("Stop",Stop,100)
button3=frame.add_button("Reset",Reset,100)
frame.set_draw_handler(draw)
timer1=simplegui.create_timer(1,timer)
# register event handlers


# start frame
frame.start()
