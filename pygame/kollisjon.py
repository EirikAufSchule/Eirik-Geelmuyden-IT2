from random import randint, uniform
import pygame as py
from pygame.locals import *
import numpy as np
import math as m

ball_ball_restitution = uniform(0.92, 0.98)
ball_wall_restitution = 0.85
class Ball:

    def __init__(self, x, y, radius, v_x, v_y, mass, color = "red"):
        #pos
        self.x = x
        self.y = y
        #bevegelse
        self.v_x = v_x
        self.v_y = v_y
        self.v = m.sqrt(v_x**2 + v_y**2)
        #utseende
        self.radius = radius
        self.color = color
        self.mass = mass

    def adjust_position(self,surf):
        # Juster posisjon for å unngå at ballen går utenfor vinduet
        self.x = max(self.radius, min(self.x, surf.get_width()  - self.radius))
        self.y = max(self.radius, min(self.y, surf.get_height() - self.radius))

    def draw(self,surf):
        py.draw.circle(surf, self.color, (int(self.x), int(self.y)),self.radius)

    def squish():
        pass

    def check_wall_collision(self,surf_width,surf_height):
        if (self.x - self.radius) <= 0 or (self.x + self.radius) >= surf_width:
            self.v_x = - self.v_x*ball_wall_restitution
            self.v_y = self.v_y*ball_wall_restitution
            self.adjust_position(surf)

        elif (self.y - self.radius) <= 0 or (self.y + self.radius) >= surf_height:
            self.v_x = self.v_x*ball_wall_restitution
            self.v_y = - self.v_y*ball_wall_restitution
            self.adjust_position(surf)

        return
    def animate(self):
        self.check_wall_collision(surf.get_width(), surf.get_height())
        self.x += self.v_x
        self.y += self.v_y  #pluss på y for tyngdekraft


def resolve_collision(ball1, ball2, distance):
#https://williamecraver.wixsite.com/elastic-equations
    overlap = (ball1.radius + ball2.radius) - distance
    angle = np.arctan2(ball2.y - ball1.y, ball2.x - ball1.x)

    # Juster posisjoner for å unngå overlapp
    ball1.x -= overlap * np.cos(angle)
    ball1.y -= overlap * np.sin(angle)
    ball2.x += overlap * np.cos(angle)
    ball2.y += overlap * np.sin(angle)
    # Beregn nye hastigheter (elastisk kollisjon)
    relative_v_x = ball2.v_x - ball1.v_x
    relative_v_y = ball2.v_y - ball1.v_y
    normal_vector = [ball1.x - ball2.x, ball1.y - ball2.y]
    magnitude = np.sqrt(normal_vector[0] ** 2 + normal_vector[1] ** 2)
    normal_vector[0] /= magnitude
    normal_vector[1] /= magnitude

    impulse = (relative_v_x * normal_vector[0] + relative_v_y * normal_vector[1])

    ball1.v_x += impulse * normal_vector[0]*ball_ball_restitution
    ball1.v_y += impulse * normal_vector[1]*ball_ball_restitution
    ball2.v_x -= impulse * normal_vector[0]*ball_ball_restitution
    ball2.v_y -= impulse * normal_vector[1]*ball_ball_restitution

py.init()

surf_height = 700
surf_width = 800
surf = py.display.set_mode((surf_width,surf_height))
balls = []
balls.append(Ball(200, 300, 50, randint(-5,5), randint(-5,5), 10, color = "red"))
balls.append(Ball(500,500, 50, randint(-5,5), randint(-5,5), 10, color="blue"))
while True:
    surf.fill("Gray")
    
    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            exit()
    
    for ball in balls:
        ball.animate()
        ball.draw(surf)

    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            #finner hypotenus, sjekker om mindre enn summen av radii
            d_x = abs(balls[i].x - balls[j].x)
            d_y = abs(balls[i].y - balls[j].y)
            distance = m.sqrt(d_x**2 + d_y**2)
            if distance <= balls[i].radius + balls[j].radius:
                resolve_collision(balls[i], balls[j], distance)


    py.time.Clock().tick(1000)
    py.display.flip()
