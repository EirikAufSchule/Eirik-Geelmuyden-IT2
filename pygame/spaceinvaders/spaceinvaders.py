import pygame as py
from pygame.locals import *
import random as ran


class KineticBody:

    def __init__(self,surf, x, y, width, height, img = None):
        self.surf = surf
        self.x = x
        self.y = y
        if img != None:
            self.img =  py.transform.scale(py.image.load(img),(width,height)) 
        self.height = height
        self.width = width

    def draw(self):
        self.surf.blit(self.img, (self.x, self.y))

    def check_border(self, surf):
        self.x = max(0, min(self.x,surf.get_width()-self.width))
            
        self.y = max(0, min(self.y,surf.get_height()))

class Player(KineticBody):
    shots = []
    def __init__(self, surf, x, y, width, height, img:str):
        super().__init__(surf, x, y, width, height, img) 

    def shoot(self):
        x_midpoint = self.x + self.width/2 + 4
        self.shots.append(Shot(self.surf, x_midpoint + 20, self.y, 0, -10, 1, 15, 50))
        self.shots.append(Shot(self.surf, x_midpoint - 30, self.y, 0, -10, 1, 15,  50))

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
    def __init__(self, surf, x, y,v, img, health, width, height):
        
        super().__init__(surf, x, y, width, height, img)
        self.health = health
        self.v = v

    def move(self):
        self.y += self.v

    def explode(self, frame_img):
        self.surf.blit(frame_img, (self.x, self.y))



class Shot(KineticBody):

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

    def check_target(self, foes):##
        dead_foe = None
        hit = False
        for foe in foes:##
            if foe.y + foe.height >= self.y:
                if foe.x <= self.x <= foe.x + foe.width or foe.x <= self.x + self.width<= foe.x + foe.width:
                    foe.health -= shot.dmg
                    hit = True
                    if foe.health <= 0: 
                        dead_foe = foe
                    else:
                        foe.img = py.transform.scale(py.image.load("pygame/spaceinvaders/vulture_droid_damaged.png"),(foe.width,foe.height))

        return hit, dead_foe


def spawn_foes(foes, lvl, surf):
    for i in range(lvl):
        foes.append(Foe(surf, ran.randint(100, surf.get_width()-100), ran.randint(0, 100),i, "pygame/spaceinvaders/vulture-droid.png", 100, 30, 60))
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

layer_count = 3
star_count = 50
stars = get_stars(layer_count,star_count)


foes = []
foe_imgs = []

for i in range(9):
    foe_imgs.append(py.image.load(f"pygame/spaceinvaders/explosion_sheet/tile00{i}.png"))
hit_foes = []

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
        foes = spawn_foes(foes,lvl, surf)
        lvl += 1
        Player.shots.clear()

    for foe in foes:
        foe.move()
        foe.draw()
        if foe.y >= surf.get_height():
            py.quit()
    ship.key_input()
    ship.draw()



    for shot in Player.shots:
        hit, foe = shot.check_target(foes)
        if hit:
            Player.shots.remove(shot)
            if foe != None:
                foes.remove(foe)
                hit_foes.append([foe, 0])
        shot.draw()
        shot.move()
        if shot.y <= 0:
            Player.shots.remove(shot)

    if len(hit_foes) > 0:
        for foe in hit_foes:
            frame = foe[1]
            if frame < 9:
                foe[0].explode(foe_imgs[foe[1]])
                foe[1] += 1
            else:
                hit_foes.remove(foe)
            


    py.time.Clock().tick(24)
    py.display.update() 