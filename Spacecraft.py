############################################################################################
#############             Game By Peiyao        #####################
###############          SPACESHIP VOYAGE    #########################
##########################################################################################
##########################################################################################

#Click the play key to start the game!
##           _____
#           |     |
# Click the | |\  | Button to start the game!
#           | |/  |
#           |_____|
##################################################

#import module
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
space_angle=0
a=0
i=0
rock_num=1
rock_a=0
shot=range(1,100)
shot_is=range(1,100)
rock=range(1,13)
rock_is=[1,0,0,0,0,0,0,0,0,0,0,0]
started = False

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0.5
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.m=0
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        if self.thrust==False and self.m==0:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size,self.angle)
        elif self.thrust==True and self.m==0:
            
            canvas.draw_image(self.image, [self.image_center[0]+self.image_size[0],self.image_center[1]], self.image_size, self.pos, self.image_size,self.angle)
            canvas.draw_image(self.image, [self.image_center[0] + self.image_size[0], self.image_center[1]] , self.image_size,self.pos, self.image_size, self.angle)
        if self.m>0:
            center =explosion_info.get_center()
            size = explosion_info.get_size()
            if self.m<26:
                canvas.draw_image(explosion_image, [center[0]+size[0]*self.m,center[1]], size, self.pos,size )
                self.m+=1
                print self.m
            elif self.m==26:
                self.m=0
        # canvas.draw_circle(self.pos, self.radius, 1, "White", "White")

    def update(self):
        pass
    def create_a_shot(self):
        global a 
        global i
        global shot
        a=1
        forward=angle_to_vector(self.angle)
        #print "in, i",i
        shot[i]=Sprite([self.pos[0]+self.radius*forward[0],self.pos[1]+self.radius*forward[1]], [forward[0],forward[1]], 0, 0, missile_image, missile_info, missile_sound)
        shot_is[i]='y'
        i+=1
        if i>90:
            i=0
        #shot[i].draw(canvas)
    def make_thrust(self,on):
        self.thrust=on
        if on:
            forward=2000*angle_to_vector(self.angle)
            self.pos[0]+=5*forward[0]
            self.pos[1]+=5*forward[1]
            print 5*forward[0]
    def exploid(self):
        self.m=1
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.m=0
        self.es=1
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        if self.m==0 and self.es==1:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos,self.image_size ,self.angle)
        elif self.m>0 and self.es==0:
            center =explosion_info.get_center()
            size = explosion_info.get_size()
            if self.m<26:
                canvas.draw_image(explosion_image, [center[0]+size[0]*self.m,center[1]], size, self.pos,size )
                self.m+=1
            else:
                self.m=0
        elif self.es==0 and self.m==0:
            pass
            
    def update(self):
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]
        pass
    def exploid(self):
        self.m=1
        
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
    
           
def draw(canvas):
    global time
    global a
    global i
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    #a_rock.draw(canvas)
    a_missile.draw(canvas)
    # update ship and sprites
    my_ship.update()
    #a_rock.update()
    a_missile.update()
    for k in range(0,rock_num):
        rock[k].draw(canvas)
        if rock[k].es==1:
            
            rock[k].update()
        if dist(my_ship.pos,rock[k].pos)<rock[k].radius and rock[k].es==1:
                    
                            rock[k].es=0
                            my_ship.exploid()
        for j in range(0,i):
            if a==1 and shot[j].es==1:
            #if a==1:         ##one shot two down    
                shot[j].draw(canvas)
                shot[j].update()
                if dist(shot[j].pos,rock[k].pos)<rock[k].radius:
                    
                            rock[k].es=0
                            shot[j].es=0
                            #if rock[k].m==26:
                                #rock[k].es=0
                                #rock_is[k]=0               
                            rock[k].exploid()
                            #rock[k].draw(canvas)
               
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())      

                            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_num
    global rock_a
    rock_a=1
    if rock_num<12:
        pos=[random.randrange(20,780),random.randrange(20,600)]
        rock[rock_num]=Sprite(pos, [0, 0], 0, 0, asteroid_image, asteroid_info)
        rock[rock_num].es=1
        rock_num+=1
        
       
    else:
        for j in range(0,12):
            if rock[j].es==0:
                pos=[random.randrange(20,780),random.randrange(20,600)]
               
                rock[j]=Sprite(pos, [0, 0], 0, 0, asteroid_image, asteroid_info)
                rock[j].es=1
                rock_is[j]==1
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
frame.set_mouseclick_handler(click)
# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [10, 5], 0, ship_image, ship_info)
print my_ship.angle_vel
rock[0] = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
#set handlers
def keydown(key):
    global my_ship
    global i
    if key==simplegui.KEY_MAP['z']:
        my_ship.angle-=my_ship.angle_vel
    elif key==simplegui.KEY_MAP['x']:
        my_ship.angle+=my_ship.angle_vel
    elif key==simplegui.KEY_MAP['up']:
        my_ship.pos[1]-=my_ship.vel[1]
    elif key==simplegui.KEY_MAP['down']:
        my_ship.pos[1]+=my_ship.vel[1]
    elif key==simplegui.KEY_MAP['left']:
        my_ship.pos[0]-=my_ship.vel[0]   
    elif key==simplegui.KEY_MAP['right']:
        my_ship.pos[0]+=my_ship.vel[0]   
    if key==simplegui.KEY_MAP['space']:
        my_ship.create_a_shot()
    if key==simplegui.KEY_MAP['a']:
        my_ship.make_thrust(True)
    if key==simplegui.KEY_MAP['g']:
        my_ship.exploid()
def keyup(key):
    if key==simplegui.KEY_MAP['a']:
        my_ship.make_thrust(False)
# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(1000.0, rock_spawner)
label0 = frame.add_label('Game made by Peiyao', 200)
label1 = frame.add_label('',200)
label2 = frame.add_label('Instructions:',200)
label3 = frame.add_label('Key "Z" and "X" to rotate')
label4 = frame.add_label('Key "Up" to go up', 200)
label5 = frame.add_label('Key "Down" to go down', 200)
label6 = frame.add_label('Key "Left" to go left', 200)
label7 = frame.add_label('Key "Right" to go right', 200)
label10 = frame.add_label('Key "Space" to throw bullets',300)
label8 = frame.add_label('',200)
label9 = frame.add_label('Attention:',200)

label11 = frame.add_label('Try to avoid being hitted by rocks or debris or you may exploid',200)
# get things rolling
timer.start()
frame.start()
