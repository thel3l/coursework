import math

def surfaceAreaOfCylinder(r, h):
    return 2*math.pi*int(r)*(int(r) + int(h))

print(surfaceAreaOfCylinder(input("Enter radius of Cylinder"), input("Enter height of Cylinder")))