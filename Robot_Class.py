from Vector_Class import *

class Robot :
    """
    Initialize the robot
    x,y: robot's position (whole number)
    speed: speed (/tick)
    direction: direction(degree) initialized at 90
    """
    def __init__(self,xInit,yInit,lInit) :
        self.x = int(xInit)
        self.y = int(yInit)
        self.l = lInit
        self.speed = 0
        self.direction = Vector2(90)

    """
    Adjust the speed of the robot
    - deltaSpeed can be less than 0
    """
    def speed_up(self,deltaSpeed) :
        self.speed+=deltaSpeed

    """
    Rotate couterclockwise with deltaAngle degree
    """
    def rotate_left(self,deltaAngle) :
        self.direction.rotate(deltaAngle)
        
    """
    Rotate clockwise with deltaAngle degree
    """
    def rotate_right(self,deltaAngle) :
        self.direction.rotate(-deltaAngle)
        
    """
    Move the robot forward for 1 tick
    """
    def move_forward(self) :
        self.x += int(self.direction.x * self.speed)
        self.y += int(self.direction.y * self.speed)

    """
    Move the robot backward for 1 tick
    """
    def move_backward(self) :
        self.x -= int(self.direction.x * self.speed, ".2f")
        self.y -= int(self.direction.y * self.speed, ".2f")

    """
    Get vertex coordinates
    """
    def getVertexCoords(self) :
        return [(self.x+0.707*self.l*math.cos(Vector2.rad(45+self.direction.angle)),self.y+0.707*self.l*math.sin(Vector2.rad(45+self.direction.angle))),
        (self.x+0.707*self.l*math.cos(Vector2.rad(135+self.direction.angle)),self.y+0.707*self.l*math.sin(Vector2.rad(135+self.direction.angle))),
        (self.x+0.707*self.l*math.cos(Vector2.rad(225+self.direction.angle)),self.y+0.707*self.l*math.sin(Vector2.rad(225+self.direction.angle))),
        (self.x+0.707*self.l*math.cos(Vector2.rad(315+self.direction.angle)),self.y+0.707*self.l*math.sin(Vector2.rad(315+self.direction.angle)))]

    """
    !!! Incomplete method
    Activate while interact with barriers or borders
    Turn the normal(perpendicular) speed to 0
    """
    def collision(self):
        print("collision")
        
    """
    When printed, the console shows this
    """
    def __repr__(self) :
        return "<Robot x = " + str(self.x) + " y = " + str(self.y) + " l = " + str(self.l) + " speed = " + str(self.speed) + " direction = " + str(self.direction) + ">"

class Arena :
    """ We suppose that the position of the left-down corner is (0,0) """
    def __init__(self, xMax, yMax) :
        self.xMax = xMax
        self.yMax = yMax

"""
Try this code in main.py

---------------------------
from Import_Classes import *

# Move three steps forward
# with speed of 1.5

robot0.speed_up(1.5)
robot0.move_forward()
robot0.move_forward()
robot0.move_forward()

# rotate 45 degree to the left
# then move three steps backward

robot0.rotate_left(45)
robot0.move_backward()
robot0.move_backward()
robot0.move_backward()
---------------------------

"""