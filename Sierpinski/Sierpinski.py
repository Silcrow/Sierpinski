import numpy as np
import cv2
from random import randint

blank_image = np.zeros((500,500,3), np.uint8)

Ax = 250
Ay = 50
Bx = 50
By = 400
Cx = 400
Cy = 400

A = cv2.circle(blank_image,(Ax,Ay), 5, (0,0,300), -1)
B = cv2.circle(blank_image,(Bx,By), 5, (0,0,300), -1)
C = cv2.circle(blank_image,(Cx,Cy), 5, (0,0,300), -1)

# (Px,Py) point of origin ; itr=iterations
Px = 250
Py = 200
itr = 5000

def drawA():
    global Px
    global Py    
    #cv2.line(blank_image, (Px,Py), (((Px + Ax)/2),((Py + Ay)/2)), (255,0,0), 1)
    cv2.circle(blank_image, (((Px + Ax)/2),((Py + Ay)/2)), 1, (0,200,0), -1)
    #print 'drawA'
    Px = ((Px + Ax)/2)
    Py = ((Py + Ay)/2)
    return Px, Py
    
def drawB():
    global Px
    global Py
    #cv2.line(blank_image, (Px,Py), (((Px + Bx)/2),((Py + By)/2)), (255,0,0), 1)
    cv2.circle(blank_image, (((Px + Bx)/2),((Py + By)/2)), 1, (0,200,0), -1)
    #print 'drawB'
    Px = ((Px + Bx)/2)
    Py = ((Py + By)/2)
    return Px, Py
    
def drawC():
    global Px
    global Py
    #cv2.line(blank_image, (Px,Py), (((Px + Cx)/2),((Py + Cy)/2)), (255,0,0), 1)
    cv2.circle(blank_image, (((Px + Cx)/2),((Py + Cy)/2)), 1, (0,200,0), -1)
    #print 'drawC'
    Px = ((Px + Cx)/2)
    Py = ((Py + Cy)/2)
    return Px, Py
    
while itr > 0:
    r = randint(1,6)
    #print 'roll: ' + str(r)
    if r == 1 or r == 2 : drawA()
    elif r == 3 or r == 4: drawB()
    elif r == 5 or r == 6: drawC()
    #print '(' + str(Px) + ', ' + str(Py) + ')'
    #print 'itr: ' + str(itr)
    itr -= 1

cv2.imshow('Sierpinski',blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#took 4hrs, the code seems to work alright but it doesn't make me a Sierpinski
# learned about: cv2, img, line, circle, global
