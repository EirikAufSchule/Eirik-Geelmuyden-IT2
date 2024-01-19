from ctypes.wintypes import PINT
import math as m

class Ball:

    def __init__(self, x:int, y:int, radius:int, ball_nr , color:str) -> any:
       self.x = x
       self.y = y
       self.color = color
       self.radius = radius
       self.nr = ball_nr

    def check_wall_collision(self,surf):
        
        if (self.x - self.radius) <= 0 or (self.x + self.radius) >= surf.get_width():
            self.v_x = -self.v_x
            self.adjust_position(surf)

        elif (self.y - self.radius) <= 0 or (self.y + self.radius) >= surf.get_height():
            self.v_y = -self.v_y
            self.adjust_position(surf)

    def adjust_position(self,surf):
        # Juster posisjon for å unngå at ballen går utenfor vinduet
        self.x = max(self.radius, min(self.x, surf.get_width()  - self.radius))
        self.y = max(self.radius, min(self.y, surf.get_height() - self.radius))

    def check_point(self, holes, balls1,balls2):
        
        for hole in holes:

            if m.sqrt((hole.x-self.x)**2 + (hole.y - self.y)**2) <= hole.radius:
                
                if 0 < self.nr < 8:
                    balls1.remove(self)
                    return "point"
                     #1 - full color
                elif 8 < self.nr < 16:
                    balls2.remove(self)
                    return "point"
                else:
                    return "loss" #8-ball oppi hull, tap
        
        self.check_wall_collision()

        #hvis ball treffer ball, legg til ball i liste, kjør sjekker på listen

    
    



