from OpenGL.GL import *     
from OpenGL.GLUT import *   
from OpenGL.GLU import *    
import random
import time
#global_var for blinking
bflag = False
last_time=time.time() #when last blink happened
bgap=0.2


frozen=False



left,right,up,down=100,800,700,100 #bouning area
points=[]
speed=0.1
directions=[(-1, 1), (-1, -1), (1, 1), (1, -1)]


#drawing the points
def draw_points(x, y,size,color):
    glPointSize(size)          
    glBegin(GL_POINTS)  
    A,B,C=color
    glColor3f(A,B,C)    
    glVertex2f(x, y)       
    glEnd()     


#boundary drawing
def draw_bounding_box():
    glBegin(GL_LINE_LOOP)
    glColor3f(1,1,1)
    glVertex2f(left, down)
    glVertex2f(right, down)
    glVertex2f(right, up)
    glVertex2f(left, up)
    glEnd()



def mouse_listener(button, state, x, y):
    global left, right, up, down, points,directions,bflag,last_time
    y=750 - y  #y axis er top point ulta tai flip korte hobe
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if left < x <right and down < y < up:
            color=(random.random(), random.random(), random.random())
            size = random.randint(2,5)
            x_direc,y_direc=random.choice(directions)
            points.append((x, y, size, color, x_direc, y_direc, color))
            glutPostRedisplay()

    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
       bflag = not bflag
       if bflag:
        for i in range(len(points)):
            x, y, size, color, x_direc, y_direc, color_unchanged=points[i]
            points[i] = (x, y, size, color_unchanged, x_direc, y_direc, color_unchanged)
       last_time = time.time()
       glutPostRedisplay()



def setup_projection():
    glViewport(0, 0, 1000, 1000)     
    glMatrixMode(GL_PROJECTION)    
    glLoadIdentity()               
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)     




def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  
    glLoadIdentity()                                    
    setup_projection()   
    draw_bounding_box()                                                        
    for x, y, size, color,direc_dx,direc_dy,color_unchanged in points:
        draw_points(x, y, size, color)
    glutSwapBuffers()                                



#diagonal movment + bouncing + blinking
def animate():
    global points,speed,bflag,last_time,frozen
    if frozen:
        glutPostRedisplay()
        return
    current_time = time.time()
    #diagonal movment + bouncing
    for i in range(len(points)):
        x,y,size,color,direc_dx,direc_dy,color_unchanged=points[i]
        x+=direc_dx*speed
        y+=direc_dy*speed
        if x<=left or x>=right:
            direc_dx*=-1
        if y<=down or y>=up:
            direc_dy*=-1
        points[i]=(x,y,size,color,direc_dx,direc_dy,color_unchanged)
    #blinking
    if bflag and (current_time - last_time > bgap):
           for i in range(len(points)):
               x, y, size, color, direc_dx, direc_dy, color_unchanged = points[i]
               if color == (0, 0, 0):
                   color = color_unchanged
               else:
                   color = (0, 0, 0)
               points[i] = (x, y, size, color, direc_dx, direc_dy, color_unchanged)
           last_time = current_time
    glutPostRedisplay()



#speed increase and decrease
def special_key_listener(key, x, y):
    global speed
    if key == GLUT_KEY_UP: 
        speed *= 2
    elif key == GLUT_KEY_DOWN:
        speed /= 2
    glutPostRedisplay()


#frozen
def keyboard_listener(key, x, y):
    global frozen
    if key == b' ':  
        frozen = not frozen
    glutPostRedisplay()


def main():
    glutInit()                            
    glutInitDisplayMode(GLUT_RGBA)           
    glutInitWindowSize(1000, 1000)             
    glutInitWindowPosition(0, 0)             
    glutCreateWindow(b"Task_2")     
    glutDisplayFunc(display) 
    glutSpecialFunc(special_key_listener)  
    glutMouseFunc(mouse_listener)  
    glutIdleFunc(animate)   
    glutKeyboardFunc(keyboard_listener)         
    glutMainLoop()                     



if __name__ == "__main__":
    main()
