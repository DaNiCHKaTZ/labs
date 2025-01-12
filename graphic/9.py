from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 500, 500                               # window size

def drawTree():
    glColor3f(0.0,1.0,0.0)                             # set color to green
    glBegin(GL_TRIANGLES)                               # start drawing a pyramid
    glVertex3f(-1.0, -1.0, -1.0)                       # bottom left of pyramid
    glVertex3f(1.0, -1.0, -1.0)                        # bottom right of pyramid
    glVertex3f(0.0, 1.0, 0.0)                          # top of pyramid

    glVertex3f(1.0, -1.0, -1.0)                        # bottom right of pyramid
    glVertex3f(1.0, -1.0, 1.0)                         # bottom front of pyramid
    glVertex3f(0.0, 1.0, 0.0)                          # top of pyramid

    glVertex3f(1.0, -1.0, 1.0)                         # bottom front of pyramid
    glVertex3f(-1.0, -1.0, 1.0)                        # bottom left of pyramid
    glVertex3f(0.0, 1.0, 0.0)                          # top of pyramid

    glVertex3f(-1.0,-1.0, 1.0)                         # bottom left of pyramid
    glVertex3f(-1.0,-1.0, -1.0)                        # bottom back of pyramid
    glVertex3f(0.0, 1.0, 0.0)                          # top of pyramid
    glEnd()

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position
    refresh2d(width, height)                           # set mode to 2d

    drawTree()                                         # draw the tree
    glutSwapBuffers()                                  # important for double buffering

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("noobtuts.com")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything
