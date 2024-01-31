from classes import *
import random as ran
from spaceinvaders import surf

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

