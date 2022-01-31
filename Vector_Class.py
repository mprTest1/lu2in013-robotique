import math

from matplotlib.pyplot import sca
from numpy import rad2deg

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
            Tuple[int, int]: vector tuple
        """
        return xB - xA, yB - yA
    
    @staticmethod
    def scalar_product(vA, vB) :
        """Returns scalar product of two Vectors

        Args:
            `vA` (Tuple[int, int]): first Vector
            `vB` (Tuple[int, int]): second Vector

        Returns:
            float: scalar product of vA and vB
        """
        ax, ay = vA
        bx, by = vB
        return ax * bx + ay * by
    
    @staticmethod
    def norme(v) :
        """Returns magnitude of a vector v

        Args:
            `v` (Tuple[int, int]): Vector

        Returns:
            float: magnitude of v
        """
        x, y = v
        return math.sqrt(x**2 + y**2)
        
    @staticmethod
    def two_vectors_to_angle(vA, vB) :
        """!!! Method takes too long time

        Args:
            `vA` (Tuple[int, int]): First Vector
            `vB` (Tuple[int, int]): Second Vector

        Returns:
            float: angle in degrees
        """
        scalar = Vector2.scalar_product(vA, vB)
        normeA = Vector2.norme(vA)
        normeB = Vector2.norme(vB)
        res = scalar / (normeA * normeB)
        return float(format(rad2deg(math.acos(res)), ".2f"))
    
    @staticmethod
    def two_coords_to_angle(xA, yA, xB, yB, vA) :
        """from two coordinates and the first Vector, angle is returned

        Args:
            `xA` (int): x of A
            `yA` (int): y of A
            `xB` (int): x of B
            `yB` (int): y of B
            `vA` (Tuple[int, int]): Vector of A

        Returns:
            float: angle in degrees
        """
        vB = Vector2.vector_dest_from_coords(xA, yA, xB, yB)
        return Vector2.two_vectors_to_angle(vA, vB)
    
    def __repr__(self) :
        """
        When printed, the console shows this
        """
        return "<Vector x = " + str(self.x) + " y = " + str(self.y) + " angle = " + str(self.angle) + ">"

class Utils :
    
    def verify_collision_two_vector(xA,yA,xB,yB,xC,yC,xD,yD) :
        """Get Tuple[x, y] from four coordinates.
        Verify whether vector AB and vector CD collide.
        
        Args:
            `xA` (int): x of A
            `yA` (int): y of A
            `xB` (int): x of B
            `yB` (int): y of B
            `xC` (int): x of C
            `yC` (int): y of C
            `xD` (int): x of D
            `yD` (int): y of D
            
        Returns:
            Boolean: whether the collide happens
        """
        
        vecAB=Vector2.vector_dest_from_coords(xA,yA,xB,yB)
        vecAC=Vector2.vector_dest_from_coords(xA,yA,xC,yC)
        vecAD=Vector2.vector_dest_from_coords(xA,yA,xD,yD)
        vecCD=Vector2.vector_dest_from_coords(xC,yC,xD,yD)
        vecCA=Vector2.vector_dest_from_coords(xC,yC,xA,yA)
        vecCB=Vector2.vector_dest_from_coords(xC,yC,xB,yB)
        case1=Vector2.scalar_product(vecAB,vecAC)*Vector2.scalar_product(vecAB,vecAD)
        case2=Vector2.scalar_product(vecCD,vecCA)*Vector2.scalar_product(vecCD,vecCB)
        return case1<0 and case2<0
    
"""
These classes don't need to be used
in main.py tests
"""