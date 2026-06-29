from mt import Vector3, eq, cross, cross_mat


class Point:
    def __init__(self, vector3: Vector3):
        self.pos = vector3
        self.children: list[Point] = []

    def add(self, point: Point):
        self.children.append(point)

    def setPos(self, vector3: Vector3):
        self.pos = vector3

    def getPos(self) -> Vector3:
        return self.pos.copy()


class StraightLine:
    def __init__(self, law_vector: Vector3, point: Point):
        if law_vector.getLen == 0:
            raise Exception("attmept to initialize a StraightLine with 0 law vector.")

        self.point: Point = point
        self.law_vector: Vector3 = law_vector

    def inLine(self, point2: Point) -> bool:
        """判断点是否在直线上喵"""
        d_vector = point2.getPos() - self.point.getPos()
        d_len = d_vector.getLen()
        law_len = self.law_vector.getLen()
        return eq(law_len * d_len, (d_vector * self.law_vector))


class Surface:
    def __init__(self, point_a: Point, point_b: Point, point_c: Point):
        if point_a.getPos() == point_b.getPos() or point_a.getPos() == point_b.getPos() or point_c.getPos() == point_a.getPos():
            raise Exception("attempt to initialize a Surface with points have the same value.")
        line = StraightLine(point_a.getPos() - point_b.getPos(), point_a)
        if line.inLine(point_c):
            raise Exception("attempt to initialize a Surface with points on the same line.")

        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def getLaw(self) -> Vector3:
        dv1 = self.point_a.getPos() - self.point_b.getPos()
        dv2 = self.point_b.getPos() - self.point_c.getPos()
        return cross(dv1, dv2)
