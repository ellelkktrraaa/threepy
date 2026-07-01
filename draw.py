from typing import Self

import surface as sf
import math
import mt


class Camera(sf.Point):
    def __init__(self, vector3:mt.Vector3, x_th, y_th):
        """
        x_th 是相机z轴沿x的半角，y_th 是相机z轴沿y的半角
        一开始朝向(0, 0, 1)
        """
        super().__init__(vector3)
        #等价于 sf.Point.__init__(self, vector3)
        self.x_th = x_th
        self.y_th = y_th

        self.z_d = mt.Vector3(0, 0, 1)
        self.x_d = mt.Vector3(1, 0, 0)
        self.y_d = mt.Vector3(0, 1, 0)

    def flat(self, vector3:mt.Vector3)->mt.Vector2:
        """将3d的坐标翻译成平面的百分比：vector2.ele --> [0, 1]"""
        th_x=math.atan(vector3.x/vector3.z)
        d_x=th_x/self.x_th
        if d_x>=1:
            return None
        th_y=math.atan(vector3.y/vector3.z)
        d_y=th_y/self.y_th
        if d_y>=1:
            return None
        return mt.Vector2(d_x,d_y)
    def flatSurface(self,surface:sf.Surface):
        surface.

        







class render(sf.Point):
    