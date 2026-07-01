from typing import overload, Union
import surface as sf
from mt import *
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


class Mesh:
    def __init__(self, surfaces:list[sf.Surface]):
        self.surfces = surfaces
        self.center = center
    
    def getPos(self)->Vector3:
        return self.center.getPos()

    def shot(self)-> sf.Surface:
        return self.surfaces.copy()

class MateMesh:
    def __init__(self, mesh, material):
        self.mesh = mesh
        self.material = material


class Render:
    def __init__(self, x_size, y_size, camera):
        self.x_size = x_size
        self.y_size = y_size
        self.camera = camera
        self.matemeshs = []

        creatWindow(self.x_size, self.y_size)

    @overload
    def add(self, matemesh: list[MateMesh]):
        ...
    @overload
    def add(self, camera: Camera):
        ...
    def add(self, sth: Union[list[MateMesh], Camera]):
        if isinstance(sth, Camera):
            self.camera = sth
            return
        for i in sth:
            if not isinstance(i, MateMesh):
                raise Exception(f"add() require list[MateMesh] but got {i.__class__.__name__}")
            self.mate_meshs.append(i)
    
    
        

        



    def render(self):
        camera.shot()
        
        

