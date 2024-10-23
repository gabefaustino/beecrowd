entrada = input().split()

ordenados = []

for i in entrada:
    valor_float = float(i)
    ordenados.append(valor_float)

ordenados.sort()

perimetro_triangulo = ordenados[0] + ordenados[1] + ordenados[2]

if (ordenados[0] + ordenados[1] > ordenados[2]):
    print(f"Perimetro = {perimetro_triangulo:.1f}")
else:
    a = float(entrada[0])
    b = float(entrada[1])
    c = float(entrada[2])
    area_trapezio = ((a+b)*c)/2
    print(f"Area = {area_trapezio:.1f}")