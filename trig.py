from math import acos, asin, cos, degrees, radians, sin, sqrt

'''Notation:
a, b, c: sides
A, B, C: opposite angles, in degrees
'''

'''Trig functions using degree angles (default is radians)'''

def cosd(theta):
    return cos(radians(theta))

def acosd(x):
    return degrees(acos(x))

def sind(theta):
    return sin(radians(theta))

def asind(x):
    return degrees(asin(x))

'''Trig tools'''

def LoCSide(a, C, b):
    '''Law of Cosines: solve for side c'''
    return sqrt(a**2 + b**2 - 2*a*b*cosd(C))

def LoCAng(a, b, c):
    '''Law of Cosines: solve for angle C'''
    return acosd((a**2 + b**2 - c**2) / (2*a*b))

def LoSSide(A, b, B):
    '''Law of Sines: solve for side a'''
    return sind(A) / sind(B) * b

def LoSAng(a, B, b):
    '''Law of Sines: solve for angle A'''
    return asind(sind(B) * a / b)

def missingAng(A, B):
    '''Find the missing angle C'''
    return 180 - A - B

def isTriangle(a, b, c):
    '''Check the triangle inequality'''
    return c < a + b and a < b + c and b < c + a

'''Solvers'''

def SAS(a, C, b):
    c = LoCSide(a, C, b)
    A = LoSAng(a, C, c)
    B = LoSAng(b, C, c)
    return (a, b, c, A, B, C)

def ASA(A, c, B):
    C = missingAng(A, B)
    a = LoSSide(A, c, C)
    b = LoSSide(B, c, C)
    return (a, b, c, A, B, C)

def SSS(a, b, c):
    if isTriangle(a, b, c):
        C = LoCAng(a, b, c)
        A = LoCAng(b, c, a)
        B = missingAng(A, C)
        return (a, b, c, A, B, C)
    
    return None

'''Informal tests'''

def equilateral_demo():
    e = 1.0
    th = 60.0
    print(SAS(e, th, e))
    print(ASA(th, e, th))
    print(SSS(e, e, e))

def right_isos_demo():
    print(SAS(1.0, 90.0, 1.0))
    print(ASA(45.0, sqrt(2), 45.0))
    print(SSS(1.0, 1.0, sqrt(2)))