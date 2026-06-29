from tkinter import Y


def eq(a, b, c= 0.0001)->bool:
    return abs(a-b)<c

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, vector3):
        dx = self.x + vector3.x
        dy = self.y + vector3.y
        dz = self.z + vector3.z
        return Vector3(dx, dy, dz)

    def __sub__(self, vector3):
        dx = self.x - vector3.x
        dy = self.y - vector3.y
        dz = self.z - vector3.z
        return Vector3(dx, dy, dz)

    def __mul__(self, vector3):
        dx = self.x * vector3.x
        dy = self.y * vector3.y
        dz = self.z * vector3.z
        return dx + dy + dz

    def __eq__(self, vector3):
        return eq(self.x, vector3.x) and eq(self.y, vector3.y) and eq(self.z, vector3.z)
    def __truediv__(self,vector3): 
        dx = self.y*vector3.z-self.z*vector3.y
        dy = self.z*vector3.x-self.x*vector3.z
        dz = self.x*vector3.y-self.y*vector3.x
        return Vector3(dx,dy,dz)   
    
    def getLen(self):
        return (self.x**2 + self.y**2 +self.z**2)**0.5

    def showInfo(self):
        return [self.x, self.y, self.z]


class Point:
    def __init__(self, vector3:Vector3):
        self.pos = vector3
    
    def setPos(vector3:Vector3):
        self.pos = vector3

    def getPos(self)->Vector3:
        return Vector3(self.x, self.y, self.z)

class StraightLine:
    def __init__(self, law_vector:Vector3, point:Point):
        if law_vector.getLen == 0:
            raise Exception("attmept to initialize a StraightLine with 0 law vector.")

        self.point:Point = point
        self.law_vector:Vector3 = law_vector
    
    def inLine(self,point2:Point)->bool:
        """
        判断点是否在直线上
        """
        d_vector = point2.getPos() - self.point.getPos()
        d_len = d_vector.getLen()
        law_len = self.law_vector.getLen()
        return eq(law_len*d_len, (d_vector*self.law_vector))
        
class Surface:
    def __init__(self, point_a:Point, point_b:Point, point_c:Point):
        
        if point_a.getPos() == point_b.getPos() or point_a.getPos() == point_b.getPos() or point_c.getPos() == point_a.getPos():
            raise Exception("attempt to initialize a Surface with points have the same value.")
        line = StraightLine(point_a.getPos()-point_b.getPos(), point_a)
        if line.inLine(point_c):
            raise Exception("attempt to initialize a Surface with points on the same line.")

        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c
    def getVector(self,point_a:Point,point_b:Point,point_c:Point):
        dv1=point_a.getPos()-point_b.getPos()
        dv2=point_b.getPos()-point_c.getPos()
        law_Vector=dv1/dv2
        return law_Vector
        
        

        
        
    
    def getLaw(self)->Vector3:
        self

        




            