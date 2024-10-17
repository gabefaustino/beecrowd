def calcular_mediaPD (A, peso_a, B, peso_b, C, peso_c):
    # calcula media ponderada
    media = ((A * peso_a) + (B * peso_b) + (C * peso_c)) / (peso_a + peso_b + peso_c)
    return media

A = float(input())
B = float(input())
C = float(input())

peso_a = 2
peso_b = 3
peso_c = 5

mediaPD = calcular_mediaPD (A, peso_a, B, peso_b, C, peso_c)
print(f"MEDIA = {mediaPD:.1f}")