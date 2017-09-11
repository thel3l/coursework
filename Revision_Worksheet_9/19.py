import math

def surfaceAreaOfSphere(r):
    return 4*math.pi*pow(int(r),2)

print(surfaceAreaOfSphere(input("Enter radius of Sphere")))