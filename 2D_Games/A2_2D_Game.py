
from OpenGL.GL import *     
from OpenGL.GLUT import *   
from OpenGL.GLU import *   
import random
import time
pixels=[]
zone=0
flag_play_pause=True
score=0
stop_game=False



def mpl(x1,y1,x2,y2):
    global pixels
    #if I want to draw vertical line
    if x1 == x2:
        #this check is for, if point 2 is smaller than point 1
        if y1 > y2:
            y1, y2 = y2, y1
        for i in range(y1, y2 + 1):
            pixels.append((x1, i))
        return pixels
    
    #for the swap if point 2 is smaller than point 1
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    elif x1 == x2 and y1 > y2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx=x2-x1
    dy=y2-y1
    d=2*dy-dx
    incE=2*dy
    incNE=2*(dy-dx)
    x=x1
    y=y1
    while x<=x2:
        pixels.append((x,y))
        x+=1
        if d>0:
            y+=1
            d+=incNE      
        else:
            d+=incE
    return pixels




#findig zone
def find_zone(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    Zone=0
    if dx>0 and dy>0:
      if abs(dx)>=abs(dy):
            Zone=0   
      
      elif abs(dx)<abs(dy):
            Zone=1

    elif dx<0 and dy>0:
      if abs(dx)<abs(dy):
            Zone=2   
      elif abs(dx)>=abs(dy):
            Zone=3   
    
    elif dx<0 and dy<0:
      if abs(dx)>=abs(dy):
            Zone=4   
      elif abs(dx)<abs(dy):
            Zone=5

    elif dx>0 and dy<0:
      if abs(dx)<abs(dy):
            Zone=6   
      elif abs(dx)>=abs(dy):
            Zone=7
    return Zone



#conversion to zone 0
def convert_zone(x1,y1,x2,y2,zone):
    var_x1=0
    var_x2=0
    var_y1=0
    var_y2=0
    if zone==0:
        var_x1=x1
        var_y1=y1
        var_x2=x2
        var_y2=y2
    elif zone==1:
        var_x1=y1
        var_y1=x1
        var_x2=y2
        var_y2=x2
    elif zone==2:
        var_x1=y1
        var_y1=-x1
        var_x2=y2
        var_y2=-x2
    elif zone==3:
        var_x1=-x1
        var_y1=y1
        var_x2=-x2
        var_y2=y2
    elif zone==4:
        var_x1=-x1
        var_y1=-y1
        var_x2=-x2
        var_y2=-y2
    elif zone==5:
        var_x1=-y1
        var_y1=-x1
        var_x2=-y2
        var_y2=-x2
    elif zone==6:
        var_x1=-y1
        var_y1=x1
        var_x2=-y2
        var_y2=x2
    elif zone==7:
        var_x1=x1
        var_y1=-y1
        var_x2=x2
        var_y2=-y2
    return var_x1,var_y1,var_x2,var_y2




#converting back to original zone
def bring_back_zoneo(x1,y1,zone): 
    if zone==0:
        return x1, y1
    if zone==1:
        x_original=y1
        y_original=x1
    elif zone==2:
        x_original=-y1
        y_original=x1
    elif zone==3:
        x_original=-x1
        y_original=y1
    elif zone==4:
        x_original=-x1
        y_original=-y1
    elif zone==5:
        x_original=-y1
        y_original=-x1
    elif zone==6:
        x_original=y1
        y_original=-x1   
    elif zone==7:
        x_original=x1
        y_original=-y1
    return x_original,y_original



#Arrow drawing function=========================================================================================================

def arrow_button(x1,y1,x2,y2,x3,y3,x4,y4):
    global pixels,zone
    pixels=[]
    zone=find_zone(x1,y1,x2,y2)
    
    #drwing the middle line of the arrow
    x1_zo,y1_zo,x2_zo,y2_zo=convert_zone(x1,y1,x2,y2,zone)
  
    pixels=mpl(x1_zo,y1_zo,x2_zo,y2_zo,)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]

    #drawing the above head of the arrow
    zone=find_zone(x2,y2,x3,y3)
    x2_zo,y2_zo,x3_zo,y3_zo=convert_zone(x2,y2,x3,y3,zone)
    
    pixels=mpl(x2_zo,y2_zo,x3_zo,y3_zo)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]


    #drawing the below head of the arrow
    zone=find_zone(x2,y2,x4,y4)
    x2_zo,y2_zo,x4_zo,y4_zo=convert_zone(x2,y2,x4,y4,zone)
    # if x2_zo > x4_zo:
    #     x2_zo, x4_zo = x4_zo, x2_zo
    #     y2_zo, y4_zo = y4_zo, y2_zo
    pixels=mpl(x2_zo,y2_zo,x4_zo,y4_zo)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]




#Play button drawing function=========================================================================================================
def play_button(x1,y1,x2,y2,x3,y3,x4,y4):
    global pixels,zone
    pixels=[]
    zone=find_zone(x1,y1,x2,y2)
    
    #drawing the first line of the play button
    x1_zo,y1_zo,x2_zo,y2_zo=convert_zone(x1,y1,x2,y2,zone)
  
    pixels=mpl(x1_zo,y1_zo,x2_zo,y2_zo,)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]


    #drawing the second line of the play button
    zone=find_zone(x3,y3,x4,y4)
    x3_zo,y3_zo,x4_zo,y4_zo=convert_zone(x3,y3,x4,y4,zone)
    
    pixels=mpl(x3_zo,y3_zo,x4_zo,y4_zo)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]






#Pause button drawing function=========================================================================================================
def pause_button(x1,y1,x2,y2,x3,y3):
    global pixels,zone
    pixels=[]
    zone=find_zone(x1,y1,x2,y2)
    
    #drawing the vertical line of the pause button
    x1_zo,y1_zo,x2_zo,y2_zo=convert_zone(x1,y1,x2,y2,zone)
  
    pixels=mpl(x1_zo,y1_zo,x2_zo,y2_zo,)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]


    #drawing the first curved line of the pause button
    zone=find_zone(x2,y2,x3,y3)
    x2_zo,y2_zo,x3_zo,y3_zo=convert_zone(x2,y2,x3,y3,zone)
    
    pixels=mpl(x2_zo,y2_zo,x3_zo,y3_zo)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]

    #drawing the second curved line of the pause button
    zone=find_zone(x1,y1,x3,y3)
    x1_zo,y1_zo,x3_zo,y3_zo=convert_zone(x1,y1,x3,y3,zone)
    
    pixels=mpl(x1_zo,y1_zo,x3_zo,y3_zo)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()





#Cross button drawing function=========================================================================================================
def cross_button(x1,y1,x2,y2,x3,y3,x4,y4):
    global pixels,zone
    pixels=[]
    zone=find_zone(x1,y1,x2,y2)
    
    #drawing the first line of the cross button
    x1_zo,y1_zo,x2_zo,y2_zo=convert_zone(x1,y1,x2,y2,zone)
  
    pixels=mpl(x1_zo,y1_zo,x2_zo,y2_zo,)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]

    #drawing the second line of the cross button
    zone=find_zone(x3,y3,x4,y4)
    x3_zo,y3_zo,x4_zo,y4_zo=convert_zone(x3,y3,x4,y4,zone)
    
    pixels=mpl(x3_zo,y3_zo,x4_zo,y4_zo)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]
     




#Catcher drawing function=========================================================================================================
def catcher_drawing(x1, y1, x2, y2, x3, y3, x4, y4):
    global pixels,zone
    pixels=[]
    zone=find_zone(x1,y1,x2,y2)
    
    #drawing the above line of the catcher
    x1_zo,y1_zo,x2_zo,y2_zo=convert_zone(x1,y1,x2,y2,zone)
  
    pixels=mpl(x1_zo,y1_zo,x2_zo,y2_zo,)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]
    

    #drawing the below line of the catcher
    zone=find_zone(x3,y3,x4,y4)
    x3_zo,y3_zo,x4_zo,y4_zo=convert_zone(x3,y3,x4,y4,zone)
    pixels=mpl(x3_zo,y3_zo,x4_zo,y4_zo)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]

    #drawing the left line of the catcher
    zone=find_zone(x1,y1,x4,y4)
    x1_zo,y1_zo,x3_zo,y3_zo=convert_zone(x1,y1,x3,y3,zone)
    
    pixels=mpl(x1_zo,y1_zo,x3_zo,y3_zo)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]

    #drawing the right line of the catcher
    zone=find_zone(x2,y2,x3,y3)
    x2_zo,y2_zo,x4_zo,y4_zo=convert_zone(x2,y2,x4,y4,zone)
    
    pixels=mpl(x2_zo,y2_zo,x4_zo,y4_zo)
    glPointSize(3)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]





#Global variables for diamond movement and animation
diamond_colour=(random.random(), random.random(), random.random())
d_start_x=(random.randint(100,500)) #ensuring, each time diamond will start from random position
d_start_y=500
d_speed=50
last_frame_time=time.time()


#Diamond drawing function=========================================================================================================
# Top:(d_start_x, d_start_y)

# Left:(d_start_x-20, d_start_y-20)

# Bottom:(d_start_x, d_start_y-40)

# Right:(d_start_x+20, d_start_y-20)

#Height=40

def diamond_drawing(x1, y1, x2, y2, x3, y3, x4, y4):
    global pixels,zone
    pixels=[]
    zone=find_zone(x1,y1,x2,y2)
    #drawing line1
    x1_zo,y1_zo,x2_zo,y2_zo=convert_zone(x1,y1,x2,y2,zone)
    pixels=mpl(x1_zo,y1_zo,x2_zo,y2_zo,)
    glPointSize(2)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]

    #drawing line2
    zone=find_zone(x2,y2,x3,y3)
    x2_zo,y2_zo,x3_zo,y3_zo=convert_zone(x2,y2,x3,y3,zone)
    pixels=mpl(x2_zo,y2_zo,x3_zo,y3_zo)
    glPointSize(2)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)  
    glEnd()
    pixels=[]

    #drawing line3
    zone=find_zone(x3,y3,x4,y4)
    x3_zo,y3_zo,x4_zo,y4_zo=convert_zone(x3,y3,x4,y4,zone)
    pixels=mpl(x3_zo,y3_zo,x4_zo,y4_zo)
    glPointSize(2)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]
    #drawing line4
    zone=find_zone(x4,y4,x1,y1)
    x4_zo,y4_zo,x1_zo,y1_zo=convert_zone(x4,y4,x1,y1,zone)
    pixels=mpl(x4_zo,y4_zo,x1_zo,y1_zo)
    glPointSize(2)
    glBegin(GL_POINTS)
    for i in range(len(pixels)):
            x_original, y_original = bring_back_zoneo(pixels[i][0], pixels[i][1], zone)
            glVertex2f(x_original, y_original)
    glEnd()
    pixels=[]




#global variables for catcher 
catcher_left=245
catcher_right=345
catcher_above=40
catcher_below=20
catcher_speed=20


#catcher_movement======================================================
def special_key_listener(key,x,y):
    global catcher_left,catcher_right,catcher_speed
    if key==GLUT_KEY_LEFT:
        catcher_left-=catcher_speed
        catcher_right-=catcher_speed
        if catcher_left<0:
            catcher_left=0
            catcher_right=100
    elif key==GLUT_KEY_RIGHT:
        catcher_left+=catcher_speed
        catcher_right+=catcher_speed
        if catcher_right>600:
            catcher_left=0
            catcher_right=100
    glutPostRedisplay()



#code for cheat mode============================================================================
cheat_mode=False
def keyboard_listener(key, x, y):
    global cheat_mode
    if key == b'c':  
        cheat_mode = not cheat_mode
    glutPostRedisplay()



#mouse_listener===============================================================================
#goodbye print and terminate-CROSS BUTTON WORK
#PLAY-PAUSE HANDLE
def mouse_listener(button, state, x, y):
    global flag_play_pause, score,d_speed
    if (button==GLUT_LEFT_BUTTON or button==GLUT_RIGHT_BUTTON) and state==GLUT_DOWN:
      #play-pause button area
      if 290 <= x <= 320 and 540 <= (600 - y) <= 580:
            flag_play_pause = not flag_play_pause  # toggle state
            glutPostRedisplay() #refresh/update display



      #cross button area  
      if 540 <= x <=580 and 540 <= (600 - y) <= 580: #if you click on cross button's area
        print(f"                                                                                       Goodbye! Score: {score}", flush=True)
        glutLeaveMainLoop() 



      # Left arrow restart button area
      elif 40 <= x <= 80 and 540 <= (600 - y) <= 580:
            print("                                                                                    Starting Over", flush=True)# ensure the message appears instantly on the console or terminal
            # reset all variables
            score = 0
            stop_game = False
            flag_play_pause = True
            d_start_y = 500
            d_start_x = random.randint(100, 500)
            d_speed = 50
            diamond_colour = (random.random(), random.random(), random.random())
            # reset catcher position
            catcher_left = 245
            catcher_right = 345
            glutPostRedisplay()

   

def setup_projection():
    glViewport(0, 0, 600, 600)      
    glMatrixMode(GL_PROJECTION)    
    glLoadIdentity()               
    glOrtho(0.0, 600, 0.0, 600, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)     



def display():
    global d_start_x, d_start_y, d_speed, last_frame_time, flag_play_pause,diamond_colour
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    glLoadIdentity()                                  
    setup_projection() 


    #arrow drawing     
    glColor3f(0.53, 0.81, 0.92)                       
    arrow_button(80,560,40,560,60,580,60,540) 


    #play and pause button drawing
    if flag_play_pause:
        glColor3f(1.0, 0.85, 0.0)                        
        play_button(290,540,290,580,320,540,320,580)         
    else:
        glColor3f(1.0, 0.85, 0.0)                        
        pause_button(290, 540, 290, 580, 320, 560)
    
  


    #cross button drawing
    glColor3f(1.0, 0.0, 0.0)  
    cross_button(540, 540, 580, 580, 580, 540, 540, 580)


    #catcher drawing along with freeze condition
    if stop_game:
       glColor3f(1.0, 0.0, 0.0)  # red catcher
    else:
      glColor3f(1.0, 1.0, 1.0)  #white catcher
    catcher_drawing(catcher_left,catcher_above,catcher_right,catcher_above,catcher_left+20, catcher_below,catcher_right-20,catcher_below)


    #diamond drawing along with freeze condition
    if stop_game:
      glColor3f(0.0, 0.0, 0.0)  # black diamond
    else:
      glColor3f(diamond_colour[0], diamond_colour[1], diamond_colour[2])
   
    diamond_drawing(d_start_x, d_start_y, d_start_x-10, d_start_y-20, d_start_x, d_start_y-40, d_start_x+10, d_start_y-20)

    glutSwapBuffers()   





#animate_func
#controls diamond animation,cheat mode,play_pause handle==============================================================================
def animate():
    global d_start_x,d_start_y, d_speed, last_frame_time, flag_play_pause,diamond_colour
    global catcher_left, catcher_right, catcher_speed, cheat_mode
    global score,stop_game
 
    if not flag_play_pause: #paused
        return
    if stop_game:
         glutPostRedisplay() #the window needs to be redrawn.
         return


    current_frame_time=time.time()
    delta_time=current_frame_time-last_frame_time
    last_frame_time=current_frame_time
    #speed increase over_time
    d_speed+=4*delta_time
    #using s=vt to change y position meaning controlling the diamond movement
    d_start_y-=d_speed*delta_time


    #diamond_height=40
    #catcher upper y axis=40
    #diamond starting from above again and with random colour
    #<= ensures even if it goes slightly below 40 due to delta_time motion, it still resets correctly.
    # if d_start_y-40<=40: #diamond's lower portion reached the catcher's upper portion
    #     d_start_y=500
    #     d_start_x=random.randint(100, 500) #diamond satrts at random position and doesn,t go beyond screen
    #     diamond_colour=(random.random(), random.random(), random.random())
    

    #cheat_mode_control======================================================
    if cheat_mode:
        middle_point_c=(catcher_left+catcher_right)/2
        
        step_size=catcher_speed*delta_time*5
        if catcher_left<d_start_x<catcher_right:
            pass
        elif abs(d_start_x-middle_point_c)<20: #distance kom hole
            middle_point_c=d_start_x  
            
        else: #else manually delta time diye movement
            if d_start_x>middle_point_c:
                middle_point_c+=step_size*d_speed
            else:
                middle_point_c-=step_size*d_speed

        #the cather position needs to be updated, as I am moving the middle point
        catcher_left=middle_point_c-50
        catcher_right=middle_point_c+50

        if catcher_left<0:
            catcher_left=0
            catcher_right=100
        elif catcher_right>600:
            catcher_left=0
            catcher_right=100

    #score_calculation=====================================================
    d_below_y=d_start_y - 40
    if d_below_y <=40:
        if catcher_left <= d_start_x <= catcher_right:
            score += 1
            print(f"                                                                               Score: {score}",flush=True)
       
            d_start_y=500
            d_start_x=random.randint(100, 500)
            diamond_colour=(random.uniform(0.7, 1.0), random.uniform(0.7, 1.0), random.uniform(0.7, 1.0))
        else:
             stop_game=True
             print(f"                                                                               Game Over| Score: {score}", flush=True)

    glutPostRedisplay() #redraw current window





def main():
    glutInit()                               
    glutInitDisplayMode(GLUT_RGBA)           
    glutInitWindowSize(600, 600)             
    glutInitWindowPosition(0, 0)             
    glutCreateWindow(b"Catch the Diamonds!")     
    glutDisplayFunc(display) 
    #diamond movement and speed control 
    glutIdleFunc(animate)  
    #catcher mover
    glutSpecialFunc(special_key_listener)  
    glutKeyboardFunc(keyboard_listener)    
    glutMouseFunc(mouse_listener)        
    glutMainLoop()                           
if __name__ == "__main__":
    main()
