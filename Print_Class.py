from Robot_Class import *

class Affichage :
    """
    Initialize
    """
    def __init__(self, robotImport, arenaImport) :
        self.robotSaved:Robot = robotImport
        self.arenaSaved:Arena = arenaImport

    """
    Print arena and robot
    """
    def afficher(self) :
        print(self.robotSaved)
        res = "   " + "-" * self.arenaSaved.xMax + "\n"
        for yi in range(self.arenaSaved.yMax-1,-1,-1) :
            res += str(yi) + self.spaces(yi)
            for xi in range(self.arenaSaved.xMax) :
                if (xi <= self.robotSaved.x and xi+1 > self.robotSaved.x and yi <= self.robotSaved.y and yi+1 > self.robotSaved.y) :
                    res += "O"
                else :
                    res += " "
            res += "|\n"
        res += "   " + "-" * self.arenaSaved.xMax
        print(res)
        
    def spaces(self, i) :
        if self.arenaSaved.xMax >= 10 and i < 10 :
            return " |"
        return "|"

"""
Try this code in main.py :
---------------------------
from Import_Classes import *

robot = Robot(20, 5, 1)
arena = Arena(50, 10)
screen = Affichage(robot, arena)
screen.afficher()
---------------------------
"""

