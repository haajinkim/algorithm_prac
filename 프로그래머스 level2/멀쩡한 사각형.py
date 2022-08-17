import math
def solurion(w,h):
    return w*h - (w+h-math.gcd(w,h))