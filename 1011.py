PI = 3.14159

def calcular_volume_esfera(volume):
    volume = ((4/3) * PI * raio**3)
    return volume

raio = int(input())
print(f"VOLUME = {calcular_volume_esfera(raio):.3f}")