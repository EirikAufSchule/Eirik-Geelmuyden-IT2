
import pygame as py
from pygame.locals import *
import math

class Rectangle:

    def __init__(self, left, top, width, height, index, color = "white"):
        self.rect = py.rect.Rect(left,top, width, height)
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surf):
         py.draw.rect(surf, self.color,self.rect)
         
    def check_input(self,x,y):
        if self.left <= x <= (self.left + self.width) and self.top <= y <= (self.top + self.height):
            self.color = "red"


py.init()

surf_width = 1000
surf_height = 600
#mekke vindu
#surface
surf = py.display.set_mode((surf_width, surf_height))

lef_t = 0
top = 0
px_width = 10
px_height = 10

px_count_x = surf_width/px_width
px_count_y = surf_height/px_height

pixels = []

for i in range(math.floor(px_count_y)):
        for n in range(math.floor(px_count_y)):
            pixels.append(Rectangle(lef_t, top, px_height,px_width, len(pixels)))
            lef_t += px_width

        top += px_height
        lef_t = 0

    
while True:
    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            exit()

    for r in pixels:
        r.draw(surf)
        x,y = py.mouse.get_pos()
        if py.mouse.get_pressed()[0]:
            r.check_input(x,y)
        
    py.time.Clock().tick(24)
    py.display.update()

    """ red_px = []
    for p in pixels:
        if p.color == "red":
            red_px.append(p)


    def animate_fall(rect, end_y):
        left
        
        end_y

        for i in range(end_y-rect.top):
            pixels[rect.index]
 """
