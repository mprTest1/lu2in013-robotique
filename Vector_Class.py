import math

class Vector1 :
    def __init__(self,x1i,y1i,x2i,y2i) :
        self.x1=x1i
        self.x2=x2i
        self.y1=y1i
        self.y2=y2i
    def getV(self) :
        return (self.x2-self.x1,self.y2-self.y1)

class Vector2 :
    """
    Initialize the vector of direction (|v|=1)
    - Suppose that 0 degrees in the positive direction of the x-axis(right)
    """
    def __init__(self, angle) :
        self.angle = angle
        self.x = math.cos(Vector2.rad(angle))
        self.y = math.sin(Vector2.rad(angle))
        
    """
    Convert an angle from degree to radius
    """
    def rad(angle) :
        return angle * math.pi / 180
    
    """
    Rotate couterclockwise with deltaAngle degree
    - Suppose deltaAngle is between -180 and 180
    Then refresh x and y
    """
    def rotate(self,deltaAngle) :
        self.angle += deltaAngle
        self.x = math.cos(Vector2.rad(self.angle))
        self.y = math.sin(Vector2.rad(self.angle))

class Utils :
    """

    """
    def prodV(v1,v2) :
        x1,y1=v1.getV()
        x2,y2=v2.getV()
        return x1*x2+y1*y2
    
    """
    Incomplete method
    """
    def verifyCollision() :
        return
    