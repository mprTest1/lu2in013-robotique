from Vector_Class import *

class Robot :
    
    def __init__(self,xInit,yInit,lInit) :
        """
        Initialize the robot
        `x` and `y` : robot's position (whole number)
        `l` : square's side lenght
        `speed` : speed (/tick)
        `direction` : direction(degree) initialized at 90
        """
        
        self.x = int(xInit)
        self.y = int(yInit)
        self.l = lInit
        self.speed = 0
        self.direction = Vector2(90)

    def speed_up(self,deltaSpeed) :
        """
        Adjust the speed of the robot
        `deltaSpeed` : amount of speed added to the original speed.
        Can be less than 0, to remove some speed.
        """
        self.speed+=deltaSpeed

    def rotate_left(self,deltaAngle) :
        """
        Rotate couterclockwise with `deltaAngle` degree
        """
        self.direction.rotate(deltaAngle)
        
    def rotate_right(self,deltaAngle) :
        """
        Rotate clockwise with `deltaAngle` degree
        """
        self.direction.rotate(-deltaAngle)
        
    def move_forward(self) :
        """
        Move the robot forward for 1 tick
        """
        self.x += int(self.direction.x * self.speed)
        self.y += int(self.direction.y * self.speed)

    def move_backward(self) :
        """
        Move the robot backward for 1 tick
        """
        self.x -= int(self.direction.x * self.speed, ".2f")
        self.y -= int(self.direction.y * self.speed, ".2f")

    def getVertexCoords(self) :
        """
        Get vertex coordinates
        """
        return [(self.x+0.707*self.l*math.cos(Vector2.rad(45+self.direction.angle)),self.y+0.707*self.l*math.sin(Vector2.rad(45+self.direction.angle))),
        (self.x+0.707*self.l*math.cos(Vector2.rad(135+self.direction.angle)),self.y+0.707*self.l*math.sin(Vector2.rad(135+self.direction.angle))),
        (self.x+0.707*self.l*math.cos(Vector2.rad(225+self.direction.angle)),self.y+0.707*self.l*math.sin(Vector2.rad(225+self.direction.angle))),
        (self.x+0.707*self.l*math.cos(Vector2.rad(315+self.direction.angle)),self.y+0.707*self.l*math.sin(Vector2.rad(315+self.direction.angle)))]

    def collision(self):
        """
        !!! Incomplete method
        Activate while interact with barriers or borders
        Turn the normal(perpendicular) speed to 0
        """
        print("collision")
        
    def __repr__(self) :
        """
        When printed, the console shows this
        """
        return "<Robot x = " + str(self.x) + " y = " + str(self.y) + " l = " + str(self.l) + " speed = " + str(self.speed) + " direction = " + str(self.direction) + ">"

"""
Try this code in main.py

---------------------------
from Import_Classes import *

robot = Robot(5,5,4)
arena = Arena(50, 15)

# Move three steps forward
# with speed of 1.5

robot.speed_up(1.5)
robot.move_forward()
robot.move_forward()
robot.move_forward()

# rotate 45 degree to the left
# then move three steps backward

robot.rotate_left(45)
robot.move_backward()
robot.move_backward()
robot.move_backward()
---------------------------

"""