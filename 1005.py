def calcular_mediaPD (A, peso_a, B, peso_b):
    # calcula media ponderada
    media = ((A * peso_a) + (B * peso_b)) / (peso_a + peso_b)
    return media

A = float(input())
B = float(input())

peso_a = 3.5
peso_b = 7.5

mediaPD = calcular_mediaPD (A, peso_a, B, peso_b)
print(f"MEDIA = {mediaPD:.5f}")