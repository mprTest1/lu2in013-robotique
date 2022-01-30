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
    
    def __init__(self, angle) :
        """
        Initialize the vector of direction (|v|=1)\n
        `angle` :
        - Suppose that 0 degree in the positive direction of the x-axis (right)
        - Precision of two values after the decimal
        """
        self.angle = angle
        self.x = float(format(math.cos(Vector2.rad(angle)), ".2f")) # Pourquoi pas self.rad(angle) ?
        self.y = float(format(math.sin(Vector2.rad(angle)), ".2f"))
        
    def rad(angle) : # Pourquoi pas rad(self, angle) ?
        """
        Convert an `angle` from degree to radius
        """
        return angle * math.pi / 180
    
    def rotate(self,deltaAngle) :
        """
        Rotate couterclockwise with `deltaAngle` degree
        - Suppose `deltaAngle` is between -180 and 180
        Then refresh x and y
        """
        self.angle += deltaAngle
        self.x = float(format(math.cos(Vector2.rad(self.angle)), ".2f"))
        self.y = float(format(math.sin(Vector2.rad(self.angle)), ".2f"))
    
    def __repr__(self) :
        """
        When printed, the console shows this
        """
        return "<Vector x = " + str(self.x) + " y = " + str(self.y) + " angle = " + str(self.angle) + ">"

class Utils :
    
    def prodV(v1,v2) :
        """
        !!! Documentation Missing
        """
        x1,y1=v1.getV()
        x2,y2=v2.getV()
        return x1*x2+y1*y2
    
    def verifyCollision() :
        """
        !!! Incomplete method
        """
        return
    
"""
These classes don't need to be used
in main.py tests
"""