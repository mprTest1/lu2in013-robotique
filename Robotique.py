import pygame
import math
import time

resolution = (1400, 700)

screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
pygame.display.set_caption("Dexter")
pygame.init()


class Animation:
    def __init__(self):
        self.is_playing = False
        self.pressed = {}

        robot_image = pygame.image.load("black_dot.jpg").convert_alpha()
        self.robot = Robot(screen, robot_image)

    def start(self):
        self.is_playing = True

    def update(self):
        self.robot.tick()

        if self.pressed.get(pygame.K_UP):  # and self.robot.rect.y > 0 :
            self.robot.move_forward()

        # and self.robot.rect.y + self.robot.rect.height < screen.get_height() :
        elif self.pressed.get(pygame.K_DOWN):
            self.robot.move_backward()

        # and self.robot.rect.x + self.robot.rect.width < screen.get_width() :
        if self.pressed.get(pygame.K_RIGHT):
            self.robot.turn_right()

        elif self.pressed.get(pygame.K_LEFT):  # and self.robot.rect.x > 0 :
            self.robot.turn_left()


class Displayable:
    """
    A Displayable object is any object that can be drawn on the screen.
    """

    def __init__(self, screen, image):
        self.position = (0, 0)
        self.screen = screen
        self.image = image
        self.current_image = image
        self.current_image_rectangle = image.get_rect()

    def set_position(self, x, y):
        self.position = (x, y)

    def display(self):
        screen.blit(self.current_image, self.position)
    
    def set_rotation(self, angle):
        self.current_image = pygame.transform.rotate(self.image, angle)


class Movable(Displayable):
    """
    A Movable object is a Displayable object, with the added capability of doing movements.
    """

    def __init__(self, screen, image):
        super().__init__(screen, image)
        self.speed = 0.00001
        self.angle = 0

    def rotate(self, deg):
        """
        Fait une rotation de deg degres.

        Par exemple, si l'angle actuel est 90, et je fais une rotation de 20, l'angle devient 110.
        """
        self.angle = + deg
        super().set_rotation(self.angle)

    def changeSpeed(self, speedDelta):
        """
        Accelere / deccelere par un facteur de speedDelta.

        Par exemple, si la vitesse est 4, et speedDelta est -1, la vitesse devient 3.
        """
        self.speed += speedDelta
    
    def tick(self):
        """
        Une 'tick' du horloge interne du programme. Fait l'objet avancer selon sa vitesse, et affiche le changement.
        """
        oldX = self.position.x
        oldY = self.position.y
        newX = oldX + math.cos(math.radians(self.angle)) * self.speed
        newY = oldY + math.sin(math.radians(self.angle)) * self.speed
        self.set_position(newX, newY)

        self.display()


class Robot(Movable):
    def __init__(self, screen, image):
        super().__init__(screen, image)

    def turn_left(self):
        self.rotate(1)

    def turn_right(self):
        self.rotate(-1)

    def move_forward(self):
        self.changeSpeed(0.1)

    def move_backward(self):
        self.changeSpeed(-0.1)


animation = Animation()
screen.fill((89, 152, 255))
pygame.display.flip()


launched = True
while launched:

    screen.fill((89, 152, 255))

    if animation.is_playing:
        animation.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            launched = False

        elif event.type == pygame.KEYDOWN:
            animation.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                animation.start()

        elif event.type == pygame.KEYUP:
            animation.pressed[event.key] = False

    pygame.display.flip()

    time.sleep(0.01)

pygame.quit()
