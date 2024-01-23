import pygame as py
from pygame.locals import *
import random as ran


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
    def __init__(self, surf, x, y, width, height, img:str):
        super().__init__(surf, x, y, width, height, img = img) 

    def shoot(self):
        x_midpoint = self.x + self.width/2 + 4
        Shot.shots.append(Shot(self.surf, x_midpoint + 20, self.y, 0, -10, 1, 15, 50))
        Shot.shots.append(Shot(self.surf, x_midpoint - 30, self.y, 0, -10, 1, 15,  50))

    def key_input(self):

        x, y = py.mouse.get_pos()
        self.x = x
        if y < 450:
            self.y = 450
        else:
            self.y = y
"""     key = py.key.get_pressed()
        if key[K_LEFT]:
            self.x -= 10
            self.check_border(surf)

        elif key[K_RIGHT]:
            self.x += 10
            self.check_border(surf)"""



class Foe(KineticBody):
    def __init__(self, surf, x, y, v, width, height,health,):
        img = "pygame/spaceinvaders/vulture-droid.png"
        dmgd_img = "pygame/spaceinvaders/vulture_droid_damaged.png"
        super().__init__(surf, x, y, width, height, health, img = img, dmgd_img = dmgd_img)
        self.v = v

    def move(self):
        self.y += self.v



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

        if shot.y <= 0:
            Shot.shots.remove(shot)

    def check_target(self, targets):##
        dead_target = None
        hit = False
        for target in targets:##
            if target.y + target.height >= self.y:
                if target.x <= self.x <= target.x + target.width or target.x <= self.x + self.width<= target.x + target.width:
                    target.health -= shot.dmg
                    self.shots.remove(shot)
                    if target.health <= 0: 
                        hit = True
                        dead_target = target
                    elif target.dmgd_img != None: 
                        target.img = target.dmgd_img

        return hit, dead_target


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
        self.surf.blit(self.imgs[self.frame],(self.x,self.y))
        

def spawn_asteroids(amount,surf):
    for i in range(amount):
        Asteroid.asteroids.append(Asteroid(surf,ran.randint(100, surf.get_width()-100), ran.randint(0, 100),40,40,200,amount*10))

def spawn_foes(foes, lvl, surf):
    for i in range(lvl):
        foes.append(Foe(surf, ran.randint(100, surf.get_width()-100), ran.randint(0, 100),i, 30, 60,100))
    return foes    


def draw_stars(stars):
    for i in range(len(stars)):
        side = i + 1
        speed = i + 2
        for star in stars[i]:
            star[1] += speed
            if star[1] >= surf.get_height()+5:
                star[1] = 0
            py.draw.rect(surf,(255,255,255), py.Rect(star[0],star[1], side, side))

        
def get_stars(layers, star_count):
    stars = []
    for i in range(layers):
        current_stars = []
        for j in range(star_count):
            vector = []
            vector.append(ran.randint(0,surf.get_width()))
            vector.append(ran.randint(0,surf.get_height())+10)
            current_stars.append(vector)

        stars.append(current_stars)
    return stars



py.init()
surf_width = 1000
surf_height = 700
surf = py.display.set_mode((surf_width, surf_height))

lvl = 0

stars = get_stars(3,50)


foes = []
explosion_imgs = []

for i in range(9):
    explosion_imgs.append(py.image.load(f"pygame/spaceinvaders/explosion_sheet/tile00{i}.png"))

hit_objs = []

ship = Player(surf, surf_width/2, 550, 100, 140, "pygame/spaceinvaders/naboo-starfighter.png")


while True:
    surf.fill("black")
    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            exit()
        elif e.type == py.KEYDOWN:
            if e.key == K_SPACE:
                ship.shoot()
    
    draw_stars(stars)

    if len(foes) == 0: 
        spawn_asteroids(lvl, surf)
        foes = spawn_foes(foes,lvl, surf)
        lvl += 1
        Shot.shots.clear()

    for asteroid in Asteroid.asteroids:
        asteroid.draw()
        asteroid.move()

    for foe in foes:
        foe.move()
        foe.draw()
        if foe.y >= surf.get_height():
            py.quit()

    for shot in Shot.shots:
        for objs in [Asteroid.asteroids,foes]:
            hit, obj = shot.check_target(objs)
            if hit:
                frame = 0
                hit_objs.append([obj, frame])
                objs.remove(obj)
               

        shot.draw()
        shot.move()

    if len(hit_objs) > 0:
        for obj in hit_objs:
            obj[0].move()
            frame_nr = obj[1]
            if frame_nr < 9:
                obj[0].explode(explosion_imgs[frame_nr])
                obj[1] += 1
            else:
                hit_objs.remove(obj)

    ship.key_input()
    ship.draw()        


    py.time.Clock().tick(24)
    py.display.update() 