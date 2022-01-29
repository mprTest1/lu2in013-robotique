from Import_Classes import *

class Task :
    """
    Three tasks must be realised in this class
    """
    
    def __init__(self, robot, arena) :
        self.robot:Robot = robot
        if self.robot.speed == 0 :
            self.robot.speed_up(1)
        self.arena:Arena = arena
        self.screen = Affichage(self.robot, self.arena)
    
    """
    Move the robot so the square is formed 
    """
    def draw_square(self, lenght) :
        self.screen.afficher()
        for i in range(4) :
            for j in range(lenght) :
                self.robot.move_forward()
            self.robot.rotate_right(90)
            print(self.robot)
            self.screen.afficher()
    
    """
    !!! Incomplete method
    Detect the closest wall
    Find the middle point between the robot and the wall
    Move faster until reaching the middle point
    Then move slower until touching the wall
    """
    def approach_a_wall(self) :
        return
    
    """
    !!! Incomplete method
    Detect the position of the beacon
    Follow it (whatever the speed is) until touching it
    """
    def follow_a_beacon(self) :
        return
            
"""
Try this code in main.py : 
---------------------------
from Task_Class import *

robot = Robot(20, 5, 1)
arena = Arena(50, 10)
task = Task(robot, arena)
task.draw_square(3)
---------------------------

"""




