import pygame
import math
from pygame import Vector2

resolution = (1400, 700)

screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
pygame.display.set_caption("Dexter")
pygame.init()

class Animation :
    def __init__(self) :
        self.is_playing = False
        self.pressed = {}
        self.robot = Robot()
        
    def start(self) :
        self.is_playing = True
        
    def update(self) :
        screen.blit(self.robot.image, self.robot.rect)
        
        if self.pressed.get(pygame.K_UP) : # and self.robot.rect.y > 0 :
            self.robot.move_forward()
                
        elif self.pressed.get(pygame.K_DOWN) : # and self.robot.rect.y + self.robot.rect.height < screen.get_height() :
            self.robot.move_backward()
            
        if self.pressed.get(pygame.K_RIGHT) : # and self.robot.rect.x + self.robot.rect.width < screen.get_width() :
            self.robot.turn_right()

        elif self.pressed.get(pygame.K_LEFT) : # and self.robot.rect.x > 0 :
            self.robot.turn_left()

class Displayable:
    vector: Vector2

    def __init__(self, screen):
        self.vector = Vector2(0,0)
        self.screen = screen

    def display(self):
        return


class Robot :
    def __init__(self) :
        self.image = pygame.image.load("black_dot.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        # self.center = self.rect.x, self.rect.y
        self.velocity = 0.1
        self.angle = 0
        
        self.vect = pygame.Vector2(0, -1)
        
    def rotate(self, change_angle):
        self.angle += change_angle
        self.image = pygame.transform.rotate(self.image, self.angle)
        # self.rect = self.img.get_rect(center = self.rect.center)
    
    def move(self, distance):
        self.rect.x += distance * math.cos(math.radians(self.angle + 90))
        self.rect.y -= distance * math.sin(math.radians(self.angle + 90))
        #self.rect.center = round(self.rect.x), round(self.rect.y)
    
    def turn_left(self):
        self.rotate(0.1)
        
    def turn_right(self):
        self.rotate(-0.1)
    
    def move_forward(self):
        self.move(self.velocity)
        
    def move_backward(self):
        self.move(-self.velocity)


animation = Animation()
screen.fill((89, 152, 255))
pygame.display.flip()


launched = True
while launched :
    
    screen.fill((89, 152, 255))
    
    if animation.is_playing :
        animation.update()
    
    for event in pygame.event.get() :
        
        if event.type == pygame.QUIT :
            launched = False
            
        elif event.type == pygame.KEYDOWN:
            animation.pressed[event.key] = True
            
            if event.key == pygame.K_SPACE:
                animation.start()
            
        elif event.type == pygame.KEYUP:
                animation.pressed[event.key] = False
            
    pygame.display.flip()
    
pygame.quit()