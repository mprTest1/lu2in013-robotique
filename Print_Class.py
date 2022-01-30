from Robot_Class import *
from Arena_Class import *

class Affichage :
    
    def __init__(self, robotImport, arenaImport) :
        """
        Initialize
        `robotImport` : Robot type variable
        `arenaImport` : Arena type variable
        """
        self.robotSaved:Robot = robotImport
        self.arenaSaved:Arena = arenaImport

    def afficher(self) :
        """
        Print arena and robot
        """
        print(self.robotSaved)
        res = "   " + "-" * self.arenaSaved.xMax + "\n"
        for yi in range(self.arenaSaved.yMax-1,-1,-1) :
            res += str(yi) + self.add_spaces(self.arenaSaved.xMax, yi)
            for xi in range(self.arenaSaved.xMax) :
                if (xi <= self.robotSaved.x and xi+1 > self.robotSaved.x and yi <= self.robotSaved.y and yi+1 > self.robotSaved.y) :
                    res += "O"
                else :
                    res += " "
            res += "|\n"
        res += "   " + "-" * self.arenaSaved.xMax
        print(res)
        
    def add_spaces(self, max_num, i) :
        """
        Additionnal spaces to separate y coordinates from the arena
        `max_num` : [int] helps count the max number of digits
        `i` : [int] additionnal spaces is added when the i have less digits than `max_num`
        """
        return " " * (len(str(max_num)) - len(str(i))) + "|"

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

