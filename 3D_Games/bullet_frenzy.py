from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math



##FOCUS: PLAYER GHURLE JNO CAMERA ANGLE OI ANGLE E CHANGE HOY

##gluLookAt(x, y, z,  # Camera position
             # 0, 0, 0,  # Look-at target--world er kon point e takiye achi
              #0, 0, 1)  # Up vector (z-axis) ---camera er orientation kirokom--x,y,z axis, as 1 ta z axis er upor deya, 
    #tai upward axis ta z axis, jeta typically y thake and upore gele z er + axis, niche gele z er - axis
    # z axis vertical upward bole, horizontal ta x axis and x er positive axis left side, negative axis right side
    #in and out holo y axis, out holo y er + direction, in holo y er - direction


###################Global VARIABLES####################============================================================================================

# Camera ta kothay set kora
camera_pos = (0,500,500) 

#left side writing
life=5
score=0
bullet_missed=0


fovY = 120  # Field of view


#enemy create
enemy=[]#enemy position store
enemy_count=5 #enemy creation er jonno

#player er location
player_coordinate=[0,0,0] 

#gun rotate
gun_rotation_angle = 0 #player move korche
bullet_rotation_angle = 0 #bullet move korche


#enemy boro_choto control
e_scaling = 1 #enemy er boro choto howa control
e_direction = 1 #enemy boro choto howar direction control



#s,w click korle player jno checker_board er baire cole na jay
square = 13  #koyta square
step_size = 80   #each square size
total_grid = square * step_size  #total checker board size
checkerboardxmin = -total_grid / 2
checkerboardxmax = total_grid / 2
checkerboardymin = -total_grid / 2
checkerboardymax = total_grid / 2



#bullet firing
bullets=()           
bullet_speed=10
bullet_size=10



#camera
camera_angle=0 #camera er angle control

game_finishing_status=False #game over control
go_screen_delay = 0 #game over er screen ta show korar age ektu wait korar jonno


cheat_v_key = False #camer cheat plus first person perspective e 360 rotae control
steady_camera_theta = 0 #cheat mode e camera er angle steady rakhe



#5 ta enemy create korar function =======================================================================
#enemy er co-ordinate create random x,y,z poaition e
def create_enemy_pos():
    global enemy
    enemy=[]
    i=0
    while i<enemy_count:
        x=random.randint(-480,480) ##(13*80)/2=520 er kom so that it covers enemy sphere radius
        y=random.randint(-480,480)
        z=40
        player_enemy_distance=math.sqrt((x-player_coordinate[0])**2 + (y-player_coordinate[1])**2)
        if player_enemy_distance<300:  #player er gayer upor jno enemy create na hoy
            continue
        
        overlap=False #overlapping check
        for c,d,k in enemy:  
            enemy_enemy_distance=math.sqrt((x-c)**2 + (y-d)**2) #enemy er sathe enemy jno overlap na kore
            if enemy_enemy_distance<90:  
                overlap=True
                break
        if overlap:
            continue
        enemy.append((x,y,z))
        i+=1




#enemy bullet hit er por disappear hole new random position e enemy create er function
def new_enemy_appear():
    while True:
        x=random.randint(-480,480)
        y=random.randint(-480,480)
        z=40
        player_enemy_distance=math.sqrt((x-player_coordinate[0])**2 + (y-player_coordinate[1])**2)
        if player_enemy_distance<300:
            continue
        
        overlap=False
        for c,d,k in enemy:  
            enemy_enemy_distance=math.sqrt((x-c)**2 + (y-d)**2)
            if enemy_enemy_distance<90:  
                overlap=True
                break
        if overlap:
            continue
        return (x,y,z)





#left top side e writing function==============================================================
def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    # Set up an orthographic projection that matches window coordinates
    gluOrtho2D(0, 1000, 0, 800)  # left, right, bottom, top

    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    # Draw text at (x, y) in screen coordinates
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    
    # Restore original projection and modelview matrices
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)





# Drawing player, enemy and bullets==========================================================================
def draw_shapes():
    global enemy,player_coordinate,bullets, first_person_perspective, game_finishing_status


    #Player drawing
    if not first_person_perspective:
        px,py,pz=player_coordinate
        glPushMatrix()
        glTranslatef(px,py,pz) 
        glRotatef(gun_rotation_angle,0,0,1)

        if game_finishing_status:
            glRotatef(-90, 1, 0, 0) #game over er por player shuye porbe===================================
            #+Y to +Z, +Z to -Y, -Y to -Z
        
        #leg drawing(left)
        glColor3f(0,0,1)
        glRotatef(-90,1,0,0)  # parameters are: angle, x, y, z
        ### +y to +z , +z to -y, -y to -z
        glTranslatef(-70,0,-10)  
        gluCylinder(gluNewQuadric(),20,5,90,20,20)# parameters are: quadric, base radius, top radius, height, slices, stacks
    
    
        #leg drawing(right)
    
        glTranslatef(90,0,-10)  
        gluCylinder(gluNewQuadric(),20,5,90,20,20)
        
        # #Body drawing with cube
        glRotatef(90,1,0,0)
        glColor3f(0.502, 0.502, 0.0)
        glTranslatef(-40, 0,100)
        glutSolidCube(120) 
        
        #Head drawing with sphere
        glColor3f(0, 0, 0)
        glTranslatef(0,0,130)
        gluSphere(gluNewQuadric(), 40, 15, 15)# parameters are: quadric, radius, slices, stacks
        
    

        # #Hand, leg and bullet drawing with cylinder
        # #Hand drawing(left)
        glColor3f(1.0, 0.878, 0.741)
        glTranslatef(40, 0, -60)
        glRotatef(-90, 1, 0, 0)## parameters are: angle, x, y, z
        glRotatef(-90, 0, 0, 1)
        gluCylinder(gluNewQuadric(), 30, 10, 90, 20, 20)# parameters are: quadric, base radius, top radius, height, slices, stacks

    
        # #right hand drawing
        
        glPushMatrix() 
        glColor3f(1.0, 0.878, 0.741)
        glTranslatef(0, -90, 0)
        # Rotate gun based on current angle
        gluCylinder(gluNewQuadric(),30, 10, 90, 20, 20)# parameters are: quadric, base radius, top radius, height, slices, stacks
        glPopMatrix()  

        # #rifel drawing
        glColor3f(0.3, 0.3, 0.3)
        glRotatef(bullet_rotation_angle, 0, 1, 0) #rotate angle
        glTranslatef(0, -50, 0)
        gluCylinder(gluNewQuadric(), 30, 10, 90, 20, 20)# parameters are: quadric, base radius, top radius, height, slices, stacks
        
        glPopMatrix()  
    

    #enemy drawing
    for(x,y,z) in enemy:
        glPushMatrix()
        
        #body
        glColor3f(1,0,0)
        glTranslatef(x,y,z)
        glScalef(e_scaling, e_scaling, e_scaling)
        gluSphere(gluNewQuadric(),45,20,20)
        
        #head
        glColor3f(0,0,0)
        glTranslatef(0,0,50)
        gluSphere(gluNewQuadric(),20,20,20)
        
        glPopMatrix()

    #bullet drawing
    for k in bullets:
        glPushMatrix()
        glColor3f(1,0,0)
        glTranslatef(k[0],k[1],k[2])
        glutSolidCube(bullet_size)
        glPopMatrix()


#================================================================Keyboard listener
##forward backward movement using w,s key
#player rotation/gun rotation using a,d key
#cheat mode control
#V,R key control
cheat=False #global variable for chaet mode control
def keyboardListener(key, x, y):
    """
    Handles keyboard inputs for player movement, gun rotation, camera updates, and cheat mode toggles.
    """        
    # X = left / right
    # Y = forward / backward
    # Z = height

    global player_coordinate,gun_rotation_angle,cheat,game_finishing_status,life,score,bullet_missed, cheat_v_key, steady_camera_theta
    move=5
    playerx, playery, playerz = player_coordinate
    #forward backward movement using y axis
    if key==b'w':
      if playery+move<=checkerboardymax: #player jeno checker board e rbaire cole na jay
        player_coordinate[1]+=move #forward movement control 5 unit kore

    elif key==b's':
       if playery-move>=checkerboardymin: #player jno hecker_board er baire na jay
        player_coordinate[1]-=move
    
    #player rotation/gun rotation using a,d key
    if key==b'a':  
        if not cheat:
            gun_rotation_angle+=5   # rotate left, as x bame postivie
            steady_camera_theta = gun_rotation_angle #cheat mode e gun and camera er angle same thake
            
    elif key==b'd':
        if not cheat:
            gun_rotation_angle-=5   # rotate right, as x dane negative
           
            steady_camera_theta = gun_rotation_angle 

    # # cheat mod control=====================================================
    if key == b'c':
        cheat = not cheat
        if cheat:
            steady_camera_theta = gun_rotation_angle
            cheat_v_key = False
        else:
            gun_rotation_angle = steady_camera_theta

    # Toggle cheat V key===============================================
    if key == b'v':
        if cheat and first_person_perspective:
            cheat_v_key = not cheat_v_key

    # # Reset the game if we press R=======================================
    if key == b'r' and game_finishing_status:
        life = 5
        score = 0
        bullet_missed = 0
        go_screen_delay = 0
        create_enemy_pos()  #abar enemy create korar jonno enemy co_ordinate bananor func call
        game_finishing_status = False








##camera er up,down, left, right movement control using arrow key==========================================================================================

#############special key listener==========================================================================================
##camera er upper movement with up arrow key(z++)
##camera er down movement with down arrow key(z--)
#rcostheta diye camera movememnt aekta fixed r distance e circle er moto movement korbe, left er theta barbe, right e theta kome jabe

def specialKeyListener(key,x,y):
    """
    Handles special key inputs (arrow keys) for adjusting the camera angle and height.
    """
    global camera_pos,camera_angle
    x,y,z=camera_pos
    move_step=1
    rotation=5
    r=math.sqrt(x**2+y**2)
    
    #Move camera up (UP arrow key)
    if key==GLUT_KEY_UP:
        z+=move_step

    #Move camera down (DOWN arrow key)
    if key==GLUT_KEY_DOWN:
        z-=move_step

#############Camera rotation logic=========================================
    #moving camera left (LEFT arrow key)
    if key==GLUT_KEY_LEFT:
        camera_angle+=rotation

    #moving camera right (RIGHT arrow key)
    if key==GLUT_KEY_RIGHT:
        camera_angle-=rotation

    #update x,y based on camera_angle
    theta=math.radians(camera_angle)
    x=r*math.cos(theta)
    y=r*math.sin(theta)

    camera_pos=(x,y,z)




###Bullet fire and first person,third person perspective change
###mouse_listener function==========================================================================================
first_person_perspective=False
target=(0,0,0)
def mouseListener(button, state, x, y):
    """
    Handles mouse inputs for firing bullets (left click) and toggling camera mode (right click).
    """
    global bullets,player_coordinate,gun_rotation_angle,bullet_rotation_angle,first_person_perspective,camera_pos

    #bullet firing
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        
        angle_in_rad=math.radians(gun_rotation_angle)
        player_x,player_y,player_z=player_coordinate

        #Player jokhon move kore nai, tokhon gun er normal position
        gun_O_x = -30.0
        gun_O_y = 70.0
        gun_O_z = 40.0

        # angle_in_rad holo gun rotation angle er radian value
        #player ghure gele gun er rotation, rotation formula diye calculate korchi jeno bullet ta gun tip theke ber hoy
        #x prime=x cos theta - y sin theta
        #y prime=x sin theta + y cos theta
        rifel_x = player_x + (gun_O_x * math.cos(angle_in_rad) - gun_O_y * math.sin(angle_in_rad))
        rifel_y = player_y + (gun_O_x * math.sin(angle_in_rad) + gun_O_y * math.cos(angle_in_rad))
        rifel_z = player_z + gun_O_z

        total=gun_rotation_angle
        bullets+=((rifel_x,rifel_y,rifel_z,total),) #ekhan theke bullet er x,y,z peye gelam and idle function diye pore bullet move korabo
    
    #first person and third person perspective
    if button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN:
       first_person_perspective=not first_person_perspective
       if first_person_perspective:
        px,py,pz=player_coordinate
        camera_pos=(px,py,pz+140) #first person perspective e camera player er mathar upor, 140 holo head er center er ektu upor
       else:
        camera_pos=(0,500,500) #camera upore niye jay 3rd person perspective




###camera setup function==========================================================================================
up=[0,0,1]
##first_person nd 3rd person perspective er jonno camera setup handle
def setupCamera():
    global camera_pos, first_person_perspective, gun_rotation_angle, player_coordinate, up, cheat, cheat_v_key, steady_camera_theta

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fovY, 1.25, 0.1, 1500) #fovY, aspect ratio, near clip, far clip #fovY=field of view in y direction, fovY barale besi area dekhte parbo but obj choto dekhbo, komale kom area dekhte parbo
    #aspect ratio holo window er width/height ratio
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
  
    if first_person_perspective:
        
        px, py, pz = player_coordinate
        c_x = px
        c_y = py
        c_z = pz + 130   # head height cause head er upor theke camera
        #steady_cam_theta=cheat mode on korar age j dike takiye chilo camera
        if cheat and not cheat_v_key:
            angle = math.radians(steady_camera_theta) #cheat mode e camera steady thake
        else:
            angle = math.radians(gun_rotation_angle) ##player r camera ek e dike tak kora

        # forward direction change hoy camera er jodi player rotate kore
        direction_x = math.sin(angle) #sin0 mane 0, sin90 mane 1, so forward direction e x er value barbe
        direction_y = math.cos(angle) #cos0 mane 1, cos90 mane 0, so forward direction e y er value kome jabe
        direction_z = 0

        center_x = c_x + direction_x 
        center_y = c_y + direction_y
        center_z = c_z + direction_z

        up = [0, 0, 1]

        gluLookAt(c_x, c_y, c_z,
                  center_x, center_y, center_z,
                  up[0], up[1], up[2])
    else:
        # third‑person / top camera looking at the whole checkerboard
        x, y, z = camera_pos  
        center_x, center_y, center_z = 0, 0, 0
        up = [0, 0, 1]
        gluLookAt(x, y, z,
                  center_x, center_y, center_z,
                  up[0], up[1], up[2])

    # Position the camera and set its orientation
    # gluLookAt(x, y, z,  # Camera position
    #           0, 0, 0,  # Look-at target
    #           0, 0, 1)  # Up vector (z-axis)





##Idle/animate function==========================================================================================
gun_rotation_angle=0
fire_delay = 0
last_bullet_time=0
prevent_multiple_bullets=0
#animation
def idle():
    """
    Idle function that runs continuously:
    - Triggers screen redraw for real-time updates.
    """
    global enemy,player_coordinate, e_scaling, e_direction,bullets,cheat,gun_rotation_angle,fire_delay,first_person_angle,last_bullet_time,bullet_missed,score,game_finishing_status,life, game_finishing_status,prevent_multiple_bullets, go_screen_delay

    move=0.1
    updated_enemy_coordinate=[]
    distance=50 #sob enemy merge hoye jabe na

    ##game---over control
    if life <= 0:
        game_finishing_status = True
        first_person_perspective = False
        enemy = []        
        bullets = ()   
        glutPostRedisplay()   
        return    
    for(x,y,z) in enemy:
        e_p_x=player_coordinate[0]-x #enemy to player x distance
        e_p_y=player_coordinate[1]-y
        d=math.sqrt(e_p_x**2+e_p_y**2)

        #enemy player er dike movement controll
        slow_move=0.02#enemy's slow movememnt
        if d>distance: ##sob enemy merge hoye jabe na
            merge_control=slow_move/distance
            x+=e_p_x*merge_control
            y+=e_p_y*merge_control

         #########player life update   
        dx=x-player_coordinate[0]
        dy=y-player_coordinate[1]
        dist=math.sqrt(dx*dx+dy*dy)
        if dist<120:
            life-=1
            print("Life:",life)
            away=10  #so that score continuously na kome
            x+=dx/dist*away 
            y+=dy/dist*away

        updated_enemy_coordinate.append((x,y,z))
     #enemy player er dike movememnt er por position update
    enemy=updated_enemy_coordinate

    #enemy er boro choto howa animate
    e_scaling += 0.01 *e_direction
    if e_scaling >= 1.2: #max size reach korle abr choto korbo
        e_direction=-1
    elif e_scaling<=0.6: # min size
        e_direction= 1



    ################cheat mode e auto fire bullet=============================
    if fire_delay>0:
        fire_delay-=1
    if cheat:
        global prevent_multiple_bullets

        gun_rotation_angle += 0.5  # gun rotation

        if gun_rotation_angle >= 360:
            gun_rotation_angle = 0

        # reduce multiple bullet
        if prevent_multiple_bullets > 0:
            prevent_multiple_bullets -= 1

        for ex,ey,ez in enemy:
            dx = ex - player_coordinate[0]
            dy = ey - player_coordinate[1]
            #player er enemy er angular distance calculate atan2 diye
            target_angle = math.degrees(math.atan2(-dx, dy)) #atan2- 2 ta point er radian e angular distnce mape
            if target_angle < 0:
                target_angle += 360

            angle_diff = abs(target_angle - gun_rotation_angle)
            if angle_diff > 180:
                angle_diff = 360 - angle_diff


            # enemy nearly gun er shamne
            if angle_diff < 5:

                if prevent_multiple_bullets == 0:  # allow only 1 bullet
                    angle_in_rad = math.radians(gun_rotation_angle)
                    px,py,pz = player_coordinate

                    rifel_x = px - math.sin(angle_in_rad) * 90 #gun e rlength r rottion e circle er point, player theke minus
                    rifel_y = py + math.cos(angle_in_rad) * 90
                    rifel_z = ez

                    bullets+=((rifel_x,rifel_y,rifel_z, gun_rotation_angle),)

                    prevent_multiple_bullets= 30   # small delay -> prevents many bullets
                break

    new_bullets=()
   
#bullet er movement
    for k in bullets:
        kx,ky,kz,angle=k #bullet fire korar momement e guns rotation angle pabo
        kx -= math.sin(math.radians(angle)) * bullet_speed  #left dike bullet tak kora
        ky += math.cos(math.radians(angle)) * bullet_speed
        bullet_hit=False #bullet ekhono hit korenai
        updated_enemy=[]
        
        for ex,ey,ez in enemy:
            dist=math.sqrt((kx-ex)**2 + (ky-ey)**2 + (kz-ez)**2)
            if dist < 50:  # hit threshold
                score+=1
                bullet_hit=True
                updated_enemy.append(new_enemy_appear())
            else:
                updated_enemy.append((ex,ey,ez))
        
        enemy=updated_enemy

        # Only keep bullets that are still inside checkerboard and not hit
        if not bullet_hit:
            if (checkerboardxmin <= kx <= checkerboardxmax) and (checkerboardymin<=ky<=checkerboardymax):
                new_bullets+=(kx,ky,kz,angle),
            else:
                # Increment bullet_missed only if less than 10
                if bullet_missed < 10:
                    bullet_missed += 1  

    bullets=new_bullets

    # Check if bullet_missed reached 10
    if bullet_missed >= 10:
        go_screen_delay += 1
        if go_screen_delay < 100: #wait a bit so 9 na dekhay
            glutPostRedisplay()
            return

        game_finishing_status = True
        first_person_perspective = False
        bullets = ()  # remove all bullets
        enemy = []    # remove all enemies

    glutPostRedisplay()  # Trigger screen redraw






#===========================================----------------------------------------------
#wall+checkerboard========================================================================
def showScreen():
    """
    Display function to render the game scene:
    - Clears the screen and sets up the camera.
    - Draws everything of the screen
    """
    global game_finishing_status,life,score,bullet_missed
    # Clear color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset modelview matrix
    glViewport(0, 0, 1000, 800)  # Set viewport size

    setupCamera()  # Configure camera perspective
    

    # Draw the grid (game floor)
    square=13             
    step_size=80        
    total_grid=step_size*square #size of whole game_floor

    # Starting from upper-left corner
    starting_x_pos=-total_grid/2 #center(0,0,0) to left side e shift
    starting_y_pos=total_grid/2 #center(0,0,0) to top side e shift

    for i in range(square):
        x=starting_x_pos+i*step_size
        for j in range(square):
            y=starting_y_pos-j*step_size
            if (i+j)%2==0:
                glColor3f(0.7,0.5,0.95)
            else:
                glColor3f(1.0,1.0,1.0)
            # Drawing squares in clockwise order
            glBegin(GL_QUADS)
            glVertex3f(x,y,0)
            glVertex3f(x+step_size,y,0)
            glVertex3f(x+step_size,y-step_size,0)
            glVertex3f(x,y-step_size,0)
            glEnd()
 
    #Drawing the boundary walls
    x_min=-total_grid/2
    x_max=-x_min
    y_min=-total_grid/2
    y_max=-y_min
    height_z=150  # height of the walls vertically

    # Left wall 
    glColor3f(0,1,0)
    glBegin(GL_QUADS)
    glVertex3f(x_min,y_min,0)
    glVertex3f(x_min,y_max,0)
    glVertex3f(x_min,y_max,height_z)
    glVertex3f(x_min,y_min,height_z)
    glEnd()

    # Right wall 
    glColor3f(1,1,0)
    glBegin(GL_QUADS)
    glVertex3f(x_max,y_min,0)
    glVertex3f(x_max,y_max,0)
    glVertex3f(x_max,y_max,height_z)
    glVertex3f(x_max,y_min,height_z)
    glEnd()

    # Front wall along Y
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex3f(x_min,y_max,0)
    glVertex3f(x_max,y_max,0)
    glVertex3f(x_max,y_max,height_z)
    glVertex3f(x_min,y_max,height_z)
    glEnd()

    # Back wall along Y
    glColor3f(0,1,1)
    glBegin(GL_QUADS)
    glVertex3f(x_min,y_min,0)
    glVertex3f(x_max,y_min,0)
    glVertex3f(x_max,y_min,height_z)
    glVertex3f(x_min,y_min,height_z)
    glEnd()
  
    draw_shapes()
    
    if game_finishing_status:
        # LEFT SIDE text for Game Over
        draw_text(10, 700, "GAME OVER")
        draw_text(10, 670, 'Press "R" to restart.')
    else:
        draw_text(10, 700, f"Player Life Remaining: {life}")
        draw_text(10, 670, f"Game Score: {score}")
        draw_text(10, 640, f"Bullets Missed: {bullet_missed}")


    glutSwapBuffers()




# Main function to set up OpenGL window and loop
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Double buffering, RGB color, depth test
    glutInitWindowSize(1000, 800)  # Window size
    glutInitWindowPosition(0, 0)  # Window position
    wind = glutCreateWindow(b"3D OpenGL Intro")  # Create the window
    create_enemy_pos() 
    glutDisplayFunc(showScreen)  # Register display function
    glutKeyboardFunc(keyboardListener)  # Register keyboard listener
    glutSpecialFunc(specialKeyListener)
    glutMouseFunc(mouseListener)
    glutIdleFunc(idle)  # Register the idle function to move the bullet automatically

    glutMainLoop()  # Enter the GLUT main loop

if __name__ == "__main__":
    main()
