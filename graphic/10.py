import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = [
    (0, -1, 0), (-1, -2, 1), (1, -2, 1), (-1, -2, -1), (1, -2, -1),
    (0, 0, 0), (-0.7, -1, 0.7), (0.7, -1, 0.7), (-0.7, -1, -0.7), (0.7, -1, -0.7),
    (0, 1, 0), (-0.4, 0, 0.4), (0.4, 0, 0.4), (-0.4, 0, -0.4), (0.4, 0, -0.4),
    (-0.1, -2.5, 0.1), (0.1, -2.5, 0.1), (0.1, -2.5, -0.1), (-0.1, -2.5, -0.1), (-0.1, -2, 0.1), (0.1, -2, 0.1), (0.1, -2, -0.1), (-0.1, -2, -0.1)
]

faces = [
    (0, 1, 2), (0, 2, 4), (0, 4, 3), (0, 3, 1),
    (5, 6, 7), (5, 7, 9), (5, 9, 8), (5, 8, 6),
    (10, 11, 12), (10, 12, 14), (10, 14, 13), (10, 13, 11),
    (15, 16, 17, 18), (19, 20, 21, 22), (15, 19, 20, 16), (16, 20, 21, 17), (17, 21, 22, 18), (18, 22, 19, 15)
]

colors = [(0, 1, 0),(0.5, 0.25, 0)]

def Tree():
    glBegin(GL_TRIANGLES)
    for i in range(12):
        glColor3fv(colors[0])  
        glVertex3fv(vertices[faces[i][0]])
        glVertex3fv(vertices[faces[i][1]])
        glVertex3fv(vertices[faces[i][2]])
    glEnd()

    glBegin(GL_QUADS)
    for i in range(12, 18):
        glColor3fv(colors[1])
        glVertex3fv(vertices[faces[i][0]])
        glVertex3fv(vertices[faces[i][1]])
        glVertex3fv(vertices[faces[i][2]])
        glVertex3fv(vertices[faces[i][3]])
    glEnd()

def main():
    pygame.init()
    display = (1000, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_DEPTH_TEST)

    rotation_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEMOTION:
                rotation_angle = event.rel[0]  

        glRotatef(rotation_angle, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Tree()
        pygame.display.flip()
        pygame.time.wait(10)

main()
