from urllib import robotparser
from Import_Classes import *

class Task :
    """
    Three tasks must be realised in this class
    """
    
    def __init__(self, robot, arena) :
        self.robot:Robot = robot
        self.arena:Arena = arena
        self.screen = Affichage(self.robot, self.arena)
    
    def draw_square(self, lenght) :
        """
        Move the robot so the square is formed 
        And prints the arena with informations
        `lenght` : lenght of one of the square's sides
        """
        if self.robot.speed == 0 :
            self.robot.speed_up(1)
        self.screen.afficher()
        for i in range(4) :
            for j in range(lenght) :
                self.robot.move_forward()
            self.robot.rotate_right(90)
            print(self.robot)
            self.screen.afficher()
    
    def approach_a_wall(self) :
        """
        !!! Incomplete method
        We suppose we're in a rectangle so we have to choose between four walls
        Detect the closest wall (Done !)
        Find the middle point between the robot and the wall
        Move faster until reaching the middle point
        Then move slower until touching the wall
        """
        dist = {
            "left":abs(0-self.robot.x),
            "right":abs(self.arena.xMax - self.robot.x),
            "up":abs(self.arena.yMax - self.robot.y),
            "down":abs(0 - self.robot.y)
        }
        
        wall = {
            "left":(0, self.robot.y),
            "right":(self.arena.xMax-1, self.robot.y),
            "up":(self.robot.x, self.arena.yMax-1),
            "down":(self.robot.x, 0)
        }
        
        closest_wall = wall["left"]
        min_dist = min([dist[i] for i in dist])
        
        for i in dist :
            if dist[i] == min_dist :
                print("wall :", i)
                closest_wall = wall[i]
                break
        
        x, y = closest_wall
        i = 0
        
        print("min :", min_dist)
        print("tuple :", closest_wall)
        
        if self.robot.speed == 0 :
            self.robot.speed_up(1)
        while self.robot.x != x or self.robot.y != y :
            if Vector2.scalar_product((self.robot.direction.x, self.robot.direction.y), Vector2.vector_dest_from_coords(self.robot.x, self.robot.y, x, y)) >= 0 :
                self.robot.rotate_right(Vector2.two_coords_to_angle(self.robot.x, self.robot.y, x, y, (self.robot.direction.x, self.robot.direction.y)))
            else :
                self.robot.rotate_left(Vector2.two_coords_to_angle(self.robot.x, self.robot.y, x, y, (self.robot.direction.x, self.robot.direction.y)))
            self.robot.move_forward()
            self.screen.afficher()
            # In case of infinite loop
            i += 1
            if i > 20 :
                break
            
    def follow_a_beacon(self) :
        """
        !!! Incomplete method
        Detect the position of the beacon
        Follow it (whatever the speed is) until touching it
        """
        return
            
"""
Try these code in main.py : 
---------------------------
from Task_Class import *

robot = Robot(20, 5, 1)
arena = Arena(50, 10)
task = Task(robot, arena)
task.draw_square(3)
---------------------------
from Task_Class import *

robot = Robot(5, 5, 1)
arena = Arena(50, 10)
task = Task(robot, arena)
task.approach_a_wall()
---------------------------

"""





