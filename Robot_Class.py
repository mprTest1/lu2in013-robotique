import math

class Vector2 :
    def __init__(self, angle) :
        self.angle = angle
        self.x = 0
        self.y = 1
        self.x = self.x * math.cos(angle) - self.y * math.sin(angle)
        self.y = self.x * math.sin(angle) + self.y * math.cos(angle)
        
    def angle_to_radius(self, angle) :
        return angle * math.pi / 180

    def angle_to_vector(self, angle) :
        # rad = self.angle_to_radius(angle)
        self.x = self.x * math.cos(angle) - self.y * math.sin(angle)
        self.y = - (self.x * math.sin(angle) + self.y * math.cos(angle))
        
    def turn_right(self) :
        self.angle += 1
        self.angle_to_vector(self.angle)
        
    def turn_left(self) :
        self.angle -= 1
        self.angle_to_vector(self.angle)
        
    
class Robot :
    def __init__(self) :
        self.x = 5
        self.y = 5
        self.cote = 5
        self.vitesse = 1
        self.direction = Vector2(90)
        
    def move_forward(self) :
        self.x += self.vitesse * int(self.direction.x)
        self.y += self.vitesse * int(self.direction.y)
        
    def move_backward(self) :
        self.x -= self.vitesse * int(self.direction.x)
        self.y -= self.vitesse * int(self.direction.x)
        
    def turn_right(self) :
        self.direction.turn_right()
        
    def turn_left(self) :
        self.direction.turn_left()
        
    
class Arena :
    def __init__(self, longueur, largeur) :
        self.longueur = longueur
        self.largeur = largeur
    