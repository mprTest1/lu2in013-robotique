import pygame

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

class Robot :
    def __init__(self) :
        self.image = pygame.image.load("black_dot.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.velocity = 1
        
        
        
        self.vect = pygame.Vector2(0, -1)
        
    def move_forward(self) :
        self.rect.x += self.vect.x
        self.rect.y += self.vect.y
    
    def move_backward(self) :
        self.rect.x -= self.vect.x
        self.rect.y -= self.vect.y
    
    # def turn_right(self) :
    #     self.forward_x += 0.1
    #     self.forward_y -= 0.1
    #     self.backward_x -= 0.1
    #     self.backward_y += 0.1
    
    # def turn_left(self) :
    #     return


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