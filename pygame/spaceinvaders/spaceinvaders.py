from turtle import width
import pygame as py
from pygame.locals import *
import random as ran
import math
from classes import *
import json

#spawns asteroids in relation to amount, here the level
def spawn_asteroids(lvl,surf):
    amount = 1 + math.floor(lvl/3)
    for i in range(amount):
        Asteroid.asteroids.append(Asteroid(surf,ran.randint(100, surf.get_width()-100), ran.randint(0, 100),80,80 ,200,amount*10))

#spawns asteroids in relation to level
def spawn_foes(foes, lvl, surf):
    for i in range(lvl):
        foes.append(Foe(surf, ran.randint(100, surf.get_width()-100), ran.randint(0, 100),i, 30, 60,100))
    return foes    

#draws each layer of the stars, each of its own index in "stars"
def draw_stars(stars):
    for i in range(len(stars)):
        #each layer has its own size on and speed for the stars, giving a parallax effect
        side = i + 1
        speed = i + 2
        for star in stars[i]:
            star[1] += speed
            if star[1] >= surf.get_height()+5:
                star[1] = 0
            py.draw.rect(surf,(255,255,255), py.Rect(star[0],star[1], side, side))

#makes "layers" amount of stars, with "star_count" -amount of stars per layer
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

#draw text on the screen
def draw_text(fontsize, name, counter, pos, color1, color2):
    font = py.font.Font('freesansbold.ttf', fontsize)

    text = font.render(f'{name}: {counter}', True, color1, color2)
    
    text_rect = text.get_rect()

    text_rect.center = pos

    surf.blit(text, text_rect)


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

kills = 0
cash = 0

ship = Player(surf, surf_width/2, 550, 100, 140, "pygame/spaceinvaders/naboo-starfighter.png", 1)
 
game_over = False

gamemode = "gameloop"

while True:
    
    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            exit()
        elif e.type == py.KEYDOWN:
            if e.key == K_SPACE and gamemode == "gameloop":
                ship.shoot()

    match gamemode:
        case "gameloop":
            surf.fill("black")

            draw_stars(stars)

            if len(foes + hit_objs + Asteroid.asteroids) == 0: 
                lvl += 1
                gamemode = "level change"
                lvl_change_frames = 0
                spawn_asteroids(lvl, surf)
                foes = spawn_foes(foes,lvl, surf)
                Shot.shots.clear()

            for asteroid in Asteroid.asteroids:
                asteroid.draw()
                asteroid.move()
                if asteroid.y >= surf.get_height():
                    Asteroid.asteroids.remove(asteroid)


            ship.key_input()
            ship.draw()
            
            for foe in foes:
                foe.move()
                foe.draw()
                if foe.y >= surf.get_height():
                    ship.lives -= 1
                    foes.remove(foe)
                if ship.lives <= 0:
                    gamemode = "game over"

            for objs in [Asteroid.asteroids,foes]:
                #hit, obj =
                hit, obj = ship.check_collisions(objs)
                if hit:
                    hit_objs.append([obj, 0])
                    ship.lives -= 1
                    objs.remove(obj)

                for shot in Shot.shots:
                    hit, obj = shot.check_target(objs)
                    if hit:
                        #explosion frame
                        frame_nr = 0
                        hit_objs.append([obj, 0])
                        objs.remove(obj)
                        if isinstance(obj, Asteroid):
                            cash += obj.value
                        else:
                            kills += 1  
            
            for shot in Shot.shots:
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

            draw_text(16, "KILLS", kills, (surf.get_width()-100, 20))
            draw_text(16, "CASH", cash, (surf.get_width()-100, 40))
            draw_text(16, "LIVES", ship.lives, (surf.get_width()-100, 60))
            draw_text(16, "LEVEL", lvl, (surf.get_width()-100, 80))

        case "level change":
            lvl_str = str(lvl)
            number_imgs = []
            width_sum = 0
            if lvl_change_frames == 0:
                for i in range(len(lvl_str)):
                    img = py.image.load(f"pygame/spaceinvaders/level_imgs/BulkResizePhotos.com/{lvl_str[i]}.png")
                    number_imgs.append(img)
                    width_sum += img.get_width()

            """  s = py.Surface((1000,750))  # the size of your rect
                s.set_alpha(2) 
                s.fill((000,255,255))  
 """
            x = (surf.get_width() - width_sum)/2
            for img in number_imgs:
                surf.blit(img, (x, 200))
                x += img.get_width()

            #surf.blit(s, (0,0))         

            lvl_change_frames += 1
            if lvl_change_frames > 24:
                gamemode = "gameloop"

        case "game over":
            game_over_img = py.transform.scale(py.image.load("pygame/spaceinvaders/game_over.png"),(1000,800))
            surf.blit(game_over_img, ((surf.get_width()- 1000)/2, (surf.get_height() - 800)/2))
           


    py.time.Clock().tick(24)
    py.display.update() 