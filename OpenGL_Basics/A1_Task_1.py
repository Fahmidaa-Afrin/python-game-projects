from OpenGL.GL import *     
from OpenGL.GLUT import *   
from OpenGL.GLU import *    
import random

colour=0
xrain_ini=random.randint(0,1000)
yrain_ini=random.randint(700,1000)

speed=1 #used in animat, rain koto speed e porche
raindrops=[]
max_bend=10
step_size=1 #kototuku bend korbe per press
updation=0 #so that new rain drops are also bended, keeps track of current bending amount

def draw_house():
    #either go clockwise or anticlockwise
    
    #main house
    glColor3f(1.0, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(250,200)
    glVertex2f(600,200)
    glVertex2f(250,350)
    glEnd()
 
    glColor3f(1.0, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(250,350)
    glVertex2f(600,350)
    glVertex2f(600,200)
    glEnd()
    
    #hood
    glColor3f(0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex2f(250,350)
    glVertex2f(425,450)
    glVertex2f(600,350)
    glEnd()


    #door
    glColor3f(0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex2f(400,280)
    glVertex2f(450,280)
    glVertex2f(450,200)
    glEnd()

    glColor3f(0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex2f(400,280)
    glVertex2f(450,200)
    glVertex2f(400,200)
    glEnd()


    glPointSize(6)          
    glBegin(GL_POINTS)  
    glColor3f(1,0, 0.0)   
    glVertex2f(440,225)  
    glEnd() 
    
    #window
    
    glColor3f(0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex2f(310,280)
    glVertex2f(360,230)
    glVertex2f(310,230)
    glEnd()

    glColor3f(0,0,1)
    glBegin(GL_TRIANGLES)
    glVertex2f(360,230)
    glVertex2f(360,280)
    glVertex2f(310,280)
    glEnd()

    glLineWidth(3)
    glBegin(GL_LINES)
    glColor3f(1.0, 0,0)
    glVertex2f(335,280) 
    glVertex2f(335,230)
    glEnd()

    glLineWidth(3)
    glBegin(GL_LINES)
    glColor3f(1.0, 0,0)
    glVertex2f(310,255) 
    glVertex2f(360,255)
    glEnd()

#day and night
def keyboard_listener(key,x,y):
    global colour
    if key == b"d" and colour<1: 
        colour+=0.1
    elif key == b"n" and colour>0:
        colour-=0.1
    glutPostRedisplay()

#raindrop
def raindrop_generator():
    global xrain_ini,yrain_ini,raindrops
    for i in range(100):
       x = random.randint(0,1000)
       y = random.randint(700,1000)
       raindrops.append([x, y, x, y-20])#co-ordinate of starting and ending position of rain drop
       

def draw_rain():
    global raindrops
    for i in raindrops:
        glLineWidth(3)
        glBegin(GL_LINES)
        glColor3f(0.5, 0.5, 0.7)
        glVertex2f(i[0], i[1])
        glVertex2f(i[2], i[3])
        glEnd()
    

#rainfall
#logic: y er value kombe for downfall of the drops
def animate():  
    global raindrops, speed
    for k in raindrops:
        k[1]-=speed
        k[3]-=speed #y postion kombe
        if k[1] < 0 or k[3] < 0: #top theke abr rain drop ashbe ekbare niche cole gele
            var=random.randint(700,1000)
            var1=random.randint(0,1000)
            k[1]=var
            k[3]=k[1]-20 #################line er 2 ta point er difference
            k[0] = var1
            k[2] = var1+updation #so the new rain drops are also bended, we were increasing both x position in left bend, so this update needed
    glutPostRedisplay()



#left-right bend
#logic: left bend e x er value barche upor and nich 2 ta point er jonnoi

def special_key_listener(key, x, y):
    global raindrops, updation, max_bend, step_size
    if key == GLUT_KEY_LEFT:
        if updation < max_bend:
            updation += step_size
        for drop in raindrops:
            drop[0] += 1
            drop[2] += 1
            drop[1] -= 1
            drop[3] -= 1
    elif key == GLUT_KEY_RIGHT:
        if updation > -max_bend:
            updation -= step_size
        for drop in raindrops:
            drop[0] -= 1
            drop[2] -= 1
            drop[1] -= 1
            drop[3] -= 1
    glutPostRedisplay()



# ===== Set up 2D coordinate system =====
def setup_projection():
    glViewport(0, 0, 1000, 1000)     #xmin,ymin,width,height
    glMatrixMode(GL_PROJECTION)    
    glLoadIdentity()               
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)  #left,right,bottom,top,near,far
    glMatrixMode(GL_MODELVIEW)     

def display():
    glClearColor(colour, colour, colour, 1.0) #day and night
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    glLoadIdentity()                                   
    setup_projection()                                 
    glColor3f(1.0, 1.0, 0.0)                            
    draw_house() #house drawing   
    draw_rain() #rain drawing
    glutSwapBuffers()                                   


def main():
    glutInit()                              
    glutInitDisplayMode(GLUT_RGBA)          
    glutInitWindowSize(1000, 1000)   #width, height         
    glutInitWindowPosition(0, 0)            
    glutCreateWindow(b"Task_1")   
    raindrop_generator()  #generate raindrops
    glutDisplayFunc(display) 
    glutIdleFunc(animate) #animate 
    glutKeyboardFunc(keyboard_listener)    
    glutSpecialFunc(special_key_listener)       
    glutMainLoop()                           



if __name__ == "__main__":
    main()
