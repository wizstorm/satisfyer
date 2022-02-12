"""
satisfiyer

Description:
"""

import pygame
import random
pygame.init()
w=pygame.display.set_mode([400,400])
w.fill((0,0,0))
a=True
xv=input("Enter x velocity (type R to randomize it): ")
yv=input("Enter y velocity (type R to randomize it): ")
if xv=="R":
    xv=random.randint(-5,5)
else:
    xv=int(xv)
if yv=="R":
   yv=random.randint(-5,5)
else:
    yv=int(yv)


print(xv)
print(yv)



yv=3
x=200
y=200
while a:
    
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    pygame.draw.circle(w,(r,g,b),(x,y),10)
    x=x+xv
    y=y+yv
    pygame.display.flip()
    if y<=10:
        yv-=yv*2
    if x<=10:
        xv-=xv*2
    if y>=390:
        yv-=yv*2
    if x>=390:
        xv-=xv*2
    if pygame.key.get_pressed()[pygame.K_a]:
        a=False
    
    
