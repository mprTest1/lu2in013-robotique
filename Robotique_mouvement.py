import pygame

class Actor(pygame.sprite.Sprite):
    def __init__(self, pos, *grps):
        super().__init__(*grps)
        self.image = pygame.image.load('char.png').convert_alpha()
        self.image_org = self.image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.direction = pygame.Vector2((0, -1))
        
    def update(self, dt):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]: self.direction.rotate_ip(dt * -360) 
        if pressed[pygame.K_RIGHT]: self.direction.rotate_ip(dt *  360)
        
        movement = 0
        if pressed[pygame.K_UP]: movement =  1
        if pressed[pygame.K_DOWN]: movement = -1
        movement_v = self.direction * movement
        
        if movement_v.length() > 0:
            movement_v.normalize_ip()
            self.pos += movement_v * dt * 100
        
        self.image = pygame.transform.rotate(self.image_org, self.direction.angle_to((0, -1)))
        self.rect = self.image.get_rect(center=self.pos)
        

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((600, 480))
    sprites = pygame.sprite.Group()
    Actor((100, 100), sprites)
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('grey')
        sprites.draw(screen)
        sprites.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
main()