import simplegui
import random
times=7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code    
    global target
    target=0
    global time_remainder
    time_remainder=times


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code 
    print "New game begins,your range is [0,100)"
    global time_remainder
    time_remainder=times
    global target
    target=random.randrange(0,100)
    #print target
    return

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "/n"
    print "New game begins,your range is [0,1000)"
    global time_remainder
    time_remainder=times
    global target
    target=random.randrange(0,1000)
    #print target
    return
    
def input_guess(guess):
    # main game logic goes here
    global time_remainder
    if time_remainder==-1:
        print "The game has done,try another ground."
        return
    time_remainder=time_remainder-1
    if time_remainder>-1:
        guess_num=int(guess)
        print "Your guess is",guess_num
        if guess_num==target:
            print "Yes!"
            time_remainder=-1
            return
        if guess_num>target:
            result="Lower"
        else:
            result="Higher"
    if time_remainder==0:
        print "Wrong! Game over!"
        print "The right answer is",target,"."
        time_remainder=-1
        return
    print result
    print "You still get",time_remainder,"times to guess"
        
        
        
    
    # remove this when you add your code
    return

    
# create frame
frame=simplegui.create_frame("Guess the number!",200,200)
#frame = simplegui.create_frame("Home", 300, 200)
# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
inp=frame.add_input("Enter a number!",input_guess,200)
frame.start()

# call new_game 
new_game()
