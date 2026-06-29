import surface as sf
import math

class Camera(sf.Point):
    def __init__(self, vector3, x_th, y_th):
        """
        x_th 是相机x轴
        """
        super().__init__(vector3)
        #等价于 sf.Point.__init__(self, vector3)
        self.x_th = x_th
        self.y_th = y_th

        self.z_d = sf.Vector3(0, 0, 1)
        self.x_d = sf.Vector3(1, 0, 0)
        self.y_d = sf.Vector3(0, 1, 0)

class render(sf.Point):