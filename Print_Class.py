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
        res = " " + "-" * self.arenaSaved.xMax + "\n"
        for yi in range(self.arenaSaved.yMax-1,-1,-1) :
            res += str(yi)
            for xi in range(self.arenaSaved.xMax) :
                if (xi <= self.robotSaved.x and xi+1 > self.robotSaved.x and yi <= self.robotSaved.y and yi+1 > self.robotSaved.y) :
                    res += "O"
                else :
                    res += " "
            res += "|\n"
        res += " " + "-" * self.arenaSaved.xMax
        return res
