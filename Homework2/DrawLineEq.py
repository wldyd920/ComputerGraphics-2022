"""
Modified on Feb 20 2020
@author: lbg@dongseo.ac.kr
"""

import pygame
from sys import exit
import numpy as np
import math


pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption("Implementation of Line Equation")
  
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

pts = [] 
knots = []
count = 0
#screen.blit(background, (0,0))
screen.fill(WHITE)

# https://kite.com/python/docs/pygame.Surface.blit
clock= pygame.time.Clock()


def drawPoint(pt, color='GREEN', thick=3):
    # pygame.draw.line(screen, color, pt, pt)
    pygame.draw.circle(screen, color, pt, thick)

def drawPolylines(color='GREEN', thick=3):
    if(len(pts) < 2): return
    for i in range(len(pts)-1):
        # drawLine(pts[i], pts[i+1], color)
        pygame.draw.line(screen, color, pts[i], pts[i+1], thick)

################################################# Added ##################################################

def drawLineEq(pt0, pt1, color='GREEN', thick=3):
    drawPoint(pt0, color, thick)
    drawPoint(pt1, color, thick)
    x0 = pt0[0]
    y0 = pt0[1]
    x1 = pt1[0]
    y1 = pt1[1]

    # Coordinate-free System (with constraint, a0 = 1-a1 , a1 >= 0)
    for a in range(100):
        a = a/100
        c = (1-a)*pt0 + a*pt1
        drawPoint(c, color, thick=1)
    
    # # Euclidean Coordinate System (without constraint)
    # for x in range(1000):
    #     y = (y1-y0)/(x1-x0)*(x-x0)+y0
    #     xy = np.array([x,y])
    #     drawPoint(xy, color, thick=1)


#HW2 implement drawLine with drawPoint
def drawLine(pts, color='GREEN', thick=3):
    for i in range(len(pts)):
        for j in range(len(pts)):
            if i == j :
                pass
            else :
                pt0 = pts[i]
                pt1 = pts[j]
                drawLineEq(pt0, pt1)

################################################# Added ##################################################

class Pt():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pt = np.array([self.x, self.y])
        self.pts = pts
        self.button1 = button1
        self.button2 = button2
        self.button3 = button3
        self.pressed = pressed
        
        print("({0},{1})".format(self.x, self.y))
    
    def coordinate(self):
        return self.pt

    def create(self):
        pygame.draw.circle(screen, BLUE, self.pt, 5)
        pygame.draw.circle(screen, WHITE, self.pt, 1)
        
    def move(self, x, y):
        if (x,y) in "boundary of point" :
            self.x = x
            self.y = y
        elif (x,y) not in "boundary of point":
            pass

    def remove(self):
        pts.remove(self)
        del(self)
    
################################################ Editted ##################################################

#Loop until the user clicks the close button.
done = False
pressed = 0
margin = 6
old_pressed = 0
old_button1 = 0
old_button3 = 0
Points = []

while not done:   
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    time_passed = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pressed = -1            
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pressed = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            pressed = -3
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            pressed = 3           
        elif event.type == pygame.QUIT:
            done = True
        else:
            pressed = 0

    button1, button2, button3 = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()
    pt = np.array([x, y])

    # Left click
    if old_button1 == 0 and button1 == 1:
        # if len(pts) < 3 :
        Point = Pt(x, y)
        Point.create()
        Points.append(Point)
        pts.append(Point.coordinate())
        print(pts)
        print("len:"+repr(len(pts))
        +" mouse x:"+repr(x)
        +" y:"+repr(y)
        +" button1:"+repr(button1)
        +" button3:"+repr(button3)
        +" pressed:"+repr(pressed)
        +" add pts ...")
        # elif len(pts) >= 3 :
        #     print("3 points is the maximum")
        #     pass

    # Right click
    if old_button3 == 0 and button3 == 1 :
        Points = []
        pts = [] 
        knots = []
        count = 0
        screen.fill(WHITE)
        print("len:"+repr(len(pts))
             +" mouse x:"+repr(x)
             +" y:"+repr(y)
             +" button1:"+repr(button1)
             +" button3:"+repr(button3)
             +" pressed:"+repr(pressed)
             +" erase")

    # Nothing
    else:
        print("len:"+repr(len(pts))
             +" mouse x:"+repr(x)
             +" y:"+repr(y)
             +" button1:"+repr(button1)
             +" button3:"+repr(button3)
             +" pressed:"+repr(pressed))

    # DrawLines subject to the points
    if len(pts)>1:
        # drawPolylines(GREEN, 1)
        # drawLagrangePolylines(BLUE, 10, 3)
        drawLine(pts)


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.update()
    old_button1 = button1
    old_button3 = button3
    old_pressed = pressed

pygame.quit()

