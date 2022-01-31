import math

from matplotlib.pyplot import sca
from numpy import rad2deg

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
        self.x = float(format(math.cos(Vector2.rad(angle)), ".2f"))
        self.y = float(format(math.sin(Vector2.rad(angle)), ".2f"))
    
    @staticmethod
    def rad(angle) :
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
    
    @staticmethod
    def vector_dest_from_coords(xA, yA, xB, yB) :
        """Get Tuple[x, y] from two coordinates.\n
        Calculate the vector of AB

        Args:
            `xA` (int): x of A
            `yA` (int): y of A
            `xB` (int): x of B
            `yB` (int): y of B

        Returns:
            Tuple[int, int]
        """
        return xB - xA, yB - yA
    
    @staticmethod
    def scalar_product(vA, vB) :
        ax, ay = vA
        bx, by = vB
        return ax * bx + ay * by
    
    @staticmethod
    def norme(vA) :
        ax, ay = vA
        return math.sqrt(ax**2 + ay**2)
        
    @staticmethod
    def two_vectors_to_angle(vA, vB) :
        """!!! Method takes too long time

        Args:
            vA (Tuple[int, int]): First Vector
            vB (Tuple[int, int]): Second Vector

        Returns:
            float: returns angle in degree
        """
        scalar = Vector2.scalar_product(vA, vB)
        normeA = Vector2.norme(vA)
        normeB = Vector2.norme(vB)
        res = scalar / (normeA * normeB)
        return float(format(rad2deg(math.acos(res)), ".2f"))
    
    @staticmethod
    def two_coords_to_angle(xA, yA, xB, yB, vA) :
        vB = Vector2.vector_dest_from_coords(xA, yA, xB, yB)
        return Vector2.two_vectors_to_angle(vA, vB)
    
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

print(Vector2.two_vectors_to_angle((5, 7), (5, 3)))