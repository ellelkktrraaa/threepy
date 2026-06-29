def eq(a, b, c=0.0001) -> bool:
    """判断两个数值是否在一定误差内相等喵"""
    return abs(a - b) < c


class Vector:
    """向量基类，子类通过 super().__init__(*分量) 传数据喵"""
    def __init__(self, *components):
        self._data = list(components)

    def copy(self):
        return type(self)(*self._data)

    def __add__(self, other):
        return type(self)(*(a + b for a, b in zip(self._data, other._data)))

    def __sub__(self, other):
        return type(self)(*(a - b for a, b in zip(self._data, other._data)))

    def __mul__(self, other):
        """点乘喵"""
        return sum(a * b for a, b in zip(self._data, other._data))

    def __eq__(self, other):
        return all(eq(a, b) for a, b in zip(self._data, other._data))

    def getLen(self) -> float:
        """模长喵"""
        return sum(x ** 2 for x in self._data) ** 0.5

    def showInfo(self) -> list[float]:
        """以列表输出向量喵"""
        return self._data[:]

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(str(x) for x in self._data)})"


class Vector3(Vector):
    """三维向量喵"""
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    @property
    def x(self):
        return self._data[0]

    @x.setter
    def x(self, v):
        self._data[0] = v

    @property
    def y(self):
        return self._data[1]

    @y.setter
    def y(self, v):
        self._data[1] = v

    @property
    def z(self):
        return self._data[2]

    @z.setter
    def z(self, v):
        self._data[2] = v


class Matrix:
    def __init__(self, ini_list):
        self.x_len = len(ini_list[0])
        self.y_len = len(ini_list)
        self.data = [row[:] for row in ini_list]

    def getRow(self, i):
        """获取第 i 行喵"""
        return Vector(*self.data[i])

    def getCol(self, i):
        return Vector(*[r[i] for r in self.data])

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(str(x) for x in self.data)})"

    def swap_rows(self, i, j):
        """交换第 i 行和第 j 行喵"""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def gauss_elimination(self):
        """高斯消元，返回行阶梯形矩阵喵"""
        result = [row[:] for row in self.data]
        n, m = self.y_len, self.x_len
        r = 0
        for c in range(m):
            if r >= n:
                break
            max_row = max(range(r, n), key=lambda i: abs(result[i][c]))
            if abs(result[max_row][c]) < 1e-10:
                continue
            result[r], result[max_row] = result[max_row], result[r]
            pivot = result[r][c]
            for i in range(r + 1, n):
                factor = result[i][c] / pivot
                for j in range(c, m):
                    result[i][j] -= factor * result[r][j]
            r += 1
        return Matrix(result)

    def inverse(self):
        """高斯-若尔当消元求逆矩阵喵"""
        if self.x_len != self.y_len:
            raise ValueError("只有方阵才能求逆矩阵喵")
        n = self.y_len
        aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)]
               for i, row in enumerate(self.data)]

        for c in range(n):
            max_row = max(range(c, n), key=lambda i: abs(aug[i][c]))
            if abs(aug[max_row][c]) < 1e-10:
                raise ValueError("矩阵不可逆喵")
            aug[c], aug[max_row] = aug[max_row], aug[c]

            pivot = aug[c][c]
            for j in range(2 * n):
                aug[c][j] /= pivot

            for i in range(n):
                if i != c:
                    factor = aug[i][c]
                    for j in range(2 * n):
                        aug[i][j] -= factor * aug[c][j]

        inv_data = [row[n:] for row in aug]
        return Matrix(inv_data)



def cross(a: Vector3, b: Vector3) -> Vector3:
    """两个三维向量的叉乘喵"""
    return Vector3(
        a.y * b.z - a.z * b.y,
        a.z * b.x - a.x * b.z,
        a.x * b.y - a.y * b.x,
    )


def cross_mat(vectors: list[Vector3]) -> Vector3:
    """顺序叉乘多个三维向量，返回结果向量喵"""
    res = vectors[0]
    for i in range(1, len(vectors)):
        res = cross(res, vectors[i])
    return res


def time(a: Matrix, b: Matrix) -> Matrix:
    """矩阵乘法喵"""
    if a.x_len != b.y_len:
        raise Exception("attempt to time two Matrix which can't be done such operation.")

    c = [[0 for j in range(b.x_len)] for i in range(a.y_len)]

    for i in range(a.y_len):
        for j in range(b.x_len):
            c[i][j] = a.getRow(i) * b.getCol(j)
    return Matrix(c)


def time_mat(*matrixs: list[Matrix]) -> Matrix:
    """多矩阵乘法喵"""
    res = matrixs[0]
    for i in range(1, len(matrixs)):
        res = time(res, matrixs[i])
    return res


