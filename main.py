from Print_Class import *


"""
Testing Robot's movement
"""

robot0 = Robot(5,5,4)
arena0 = Arena(50, 15)

screen0 = Affichage(robot0, arena0)

screen0.afficher()

robot0.speed_up(1.5)
robot0.move_forward()
robot0.move_forward()
robot0.move_forward()

screen0.afficher()
robot0.rotate_left(45)
screen0.afficher()
robot0.move_forward()
robot0.move_forward()
robot0.move_forward()
screen0.afficher()


