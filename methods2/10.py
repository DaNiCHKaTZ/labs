import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU
from OpenGL.GLUT import glutInit
import math

def draw_triangle(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    glBegin(GL_TRIANGLES)
    glVertex3f(x1, y1, z1)
    glVertex3f(x2, y2, z2)
    glVertex3f(x3, y3, z3)
    glEnd()

def draw_pyramid():
    glColor3f(0.0, 1.0, 0.0)  
    draw_triangle(0, 0, 1, -1, -1, 0, 1, -1, 0)  
    draw_triangle(0, 0, 1, 1, -1, 0, 1, 1, 0)  
    draw_triangle(0, 0, 1, 1, 1, 0, -1, 1, 0)  
    draw_triangle(0, 0, 1, -1, 1, 0, -1, -1, 0)

def draw_tree():
    glTranslatef(0, 0, -0.5)
    draw_pyramid()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(2, 2, 2, 0, 0, 0, 0, 0, 1)
    
    draw_tree()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutCreateWindow(b"3D Tree")
glutDisplayFunc(draw)
glEnable(GL_DEPTH_TEST)
glClearColor(0.0, 0.0, 0.0, 1.0)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, 1, 0.1, 100)
glMatrixMode(GL_MODELVIEW)
glutMainLoop()