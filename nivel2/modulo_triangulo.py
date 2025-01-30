from math import sqrt


def formar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def perimetro_triangulo(a, b, c):
    return a + b + c

def area_triangulo(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))