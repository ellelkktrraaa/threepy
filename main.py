from surface import *

def main():
    p1 = Point(Vector3(1, 1, 1))
    law = Vector3(2, 2, 2)
    p = Point(Vector3(0, 0, 1))
    line = StraightLine(law, p)

    print(line.inLine(p1))
    print((Vector3(1, 2, 3)+Vector3(0, 1, 2)).showInfo())
    print(Vector3(1, 2, 3)==Vector3(1, 2, 3))

    Surface(Point(Vector3(1, 2, 3)), Point(Vector3(1, 2, 3)), Point(Vector3(2, 3, 4)))


if __name__=='__main__':
    main()