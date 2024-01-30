import pygame as py
from pygame.locals import *

class KineticBody:

    def __init__(self,surf, x, y, width, height, health = None, img = None, dmgd_img = None):
        self.surf = surf
        self.x = x
        self.y = y
        if img != None:
            self.img =  py.transform.scale(py.image.load(img),(width,height))
        if dmgd_img != None:
            self.dmgd_img = py.transform.scale(py.image.load(dmgd_img),(width,height))
        else:
            self.dmgd_img = None
        self.height = height
        self.width = width
        self.health = health
        
    def draw(self):
        self.surf.blit(self.img, (self.x, self.y))

    def check_border(self, surf):
        self.x = max(0, min(self.x,surf.get_width()-self.width))
            
        self.y = max(0, min(self.y,surf.get_height()))
    
    def explode(self, frame_img):
        self.surf.blit(frame_img, (self.x, self.y))



class Player(KineticBody):
    def __init__(self, surf, x, y, width, height, img:str, lives):
        super().__init__(surf, x, y, width, height, img = img) 
        self.lives = lives
    def shoot(self):
        x_midpoint = self.x + self.width/2 + 4
        Shot.shots.append(Shot(self.surf, x_midpoint + 20, self.y, 0, -10, 1, 15, 50))
        Shot.shots.append(Shot(self.surf, x_midpoint - 30, self.y, 0, -10, 1, 15,  50))

    def key_input(self):

        x, y = py.mouse.get_pos()
        self.x = x - self.width/2
        if y < 450:
            self.y = 450
        else:
            self.y = y

    def check_collisions(self, objs):
        for obj in objs:
            if obj.y + obj.height >= self.y:
                if obj.x <= self.x <= obj.x + obj.width or obj.x <= self.x + self.width <= obj.x + obj.width:
                    return True, obj
        return False, None


class Shot(KineticBody):
    shots = []  
    def __init__(self, surf, x, y, v_x, v_y, width, height, dmg):
        super().__init__(surf, x, y, width, height)
        self.v_x = v_x
        self.v_y = v_y
        self.dmg = dmg

    def draw(self):
        py.draw.ellipse(self.surf, "red", py.Rect(self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.v_x
        self.y += self.v_y
        if self.y <= 0:
            Shot.shots.remove(self)

    def check_target(self, targets):##
        dead_target = None
        hit = False
        for target in targets:##
            if target.y + target.height >= self.y:
                if target.x <= self.x <= target.x + target.width or target.x <= self.x + self.width<= target.x + target.width:
                    target.health -= self.dmg
                    Shot.shots.remove(self)
                    if target.health <= 0: 
                        hit = True
                        dead_target = target
                    elif target.dmgd_img != None: 
                        target.img = target.dmgd_img

        return hit, dead_target


class Foe(KineticBody):
    def __init__(self, surf, x, y, v, width, height,health,):
        img = "pygame/spaceinvaders/vulture-droid.png"
        dmgd_img = "pygame/spaceinvaders/vulture_droid_damaged.png"
        super().__init__(surf, x, y, width, height, health, img = img, dmgd_img = dmgd_img)
        self.v = v

    def move(self):
        self.y += self.v





class Asteroid(KineticBody):
    asteroids = []
    imgs = []
    zeros = "00"
    for i in range(48):
        if i > 9:
            zeros = "0"
        imgs.append(py.image.load(f"pygame/spaceinvaders/asteroid_sheet/tile{zeros}{i}.png")) 
    def __init__(self, surf, x, y, width, height, health, value):
        super().__init__(surf, x, y, width, height, health)
        self.value = value
        self.frame = 0 
        self.v = 4

    def move(self):
        self.y += self.v
    
    def draw(self):
        if self.frame <= len(self.imgs) -2:
            self.frame += 1
        else:
            self.frame = 0
        self.surf.blit(py.transform.scale(self.imgs[self.frame], (self.width, self.height)),(self.x,self.y))
        
