PI = 3.14159

def triangulo_area(a, c):
    #A por base e C por altura
    triangulo = (a*c) / 2
    return triangulo


def circulo_area(c):
    circulo = PI * (c**2)
    return circulo


def trapezio_area(a, b, c):
    trapezio = ((a + b) * c) / 2
    return trapezio


def quadrado_area(b):
    quadrado = (b**2)
    return quadrado


def retangulo_area(a, b):
    retangulo = (a * b)
    return retangulo


valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

print(f"TRIANGULO: {triangulo_area(a, c):.3f}")
print(f"CIRCULO: {circulo_area(c):.3f}")
print(f"TRAPEZIO: {trapezio_area(a, b, c):.3f}")
print(f"QUADRADO: {quadrado_area(b):.3f}")
print(f"RETANGULO: {retangulo_area(a, b):.3f}")