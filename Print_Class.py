from traceback import print_tb
from Robot_Class import *

class Affichage :
    def __init__(self, robot, arena) :
        self.robot:Robot = robot
        self.arena:Arena = arena
        
    def afficher(self) :
        res = " " + "-" * self.arena.largeur + "\n"
        for i in range(self.arena.longueur) :
            res += "|"
            for j in range(self.arena.largeur) :
                if i == self.robot.x and j == self.robot.y:
                    res += "O"
                else :
                    res += " "
            res += "|\n"
        res += " " + "-" * self.arena.largeur
        return res
            
robot = Robot()
arena = Arena(10, 50)

affichage = Affichage(robot, arena)

print(affichage.afficher())

robot.move_backward()
robot.move_backward()
robot.move_backward()
robot.move_backward()

print(affichage.afficher())