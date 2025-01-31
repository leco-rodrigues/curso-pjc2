from math import sqrt


def comprimento_triangulo(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    c = a ** 2 + b ** 2
    return a, b, sqrt(c)

def formar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def perimetro_triangulo(a, b, c):
    return a + b + c

def area_triangulo(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

def area_triangulo_vertice(x1, y1, x2, y2, x3, y3):
    area = (((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))) / 2)
    if area > 0:
        return area
    else:
        return area * -1
# ---------------------- [Exercício] Aula 12