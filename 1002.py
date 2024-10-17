pi = 3.14159

def calculo_area(raio):
    area = pi*(raio**2)
    return area

raio = float(input())
area = calculo_area(raio)

print(f"A={area:.4f}")