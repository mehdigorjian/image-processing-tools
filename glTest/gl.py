from OpenGL import GLUT as glut
from OpenGL import GL as gl
from OpenGL import GLU as glu
import math
import typing as t
def init():
    gl.glClearColor(0.0,0.0,0.0,0.0)

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glPointSize(2)
    gl.glEnable(gl.GL_POINT_SMOOTH)

    # gl.glBegin(gl.GL_POINTS)
    # gl.glVertex2f(.2, .2)
    # gl.glEnd()

    # gl.glRectf(-4,-4,4,4)
    draw_ngon(6, 5)
    draw_circle()
    gl.glFlush()

def resize(w:int, h:int)->None:
    gl.glViewport(0, 0, w, h)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()

    glu.gluOrtho2D(-10, 10, -10, 10)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

def draw_ngon(n=6, r=5):
    gl.glBegin(gl.GL_LINE_LOOP)
    for i in range(n):
        x1 = r * math.cos(i * 2 * math.pi/n)
        y1 = r * math.sin(i * 2 * math.pi/n)
        if i == n: i = 0
        x2 = r * math.cos((i+1) * 2 * math.pi/n)
        y2 = r * math.sin((i+1) * 2 * math.pi/n)
        gl.glVertex2d(x1, y1)
        gl.glVertex2d(x2, y2)
    gl.glEnd()
    
def draw_circle(r=5, div=30):
    gl.glBegin(gl.GL_POINTS)
    for i in range(div):
        x = r * math.cos(i* 2 * math.pi/div)
        y = r * math.sin(i* 2 * math.pi/div)
        gl.glVertex2d(x, y)
    gl.glEnd()

    gl.glBegin(gl.GL_LINE_LOOP)
    for i in range(div):
        x1 = r * math.cos(i * 2 * math.pi/div)
        y1 = r * math.sin(i * 2 * math.pi/div)
        if i == div: i =0
        x2 = r * math.cos((i+1) * 2 * math.pi/div)
        y2 = r * math.sin((i+1) * 2 * math.pi/div)
        gl.glVertex2d(x1, y1)
        gl.glVertex2d(x2, y2)
    gl.glEnd()

def main():
    glut.glutInit()

    glut.glutInitWindowSize(100,100)
    glut.glutCreateWindow('Mehdi')

    init()
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(resize(100,100))

    glut.glutMainLoop()

if __name__ == '__main__':
    main()