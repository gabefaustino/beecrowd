positivos = 0
soma = 0

for i in range (6):
    entrada = float(input())
    if (entrada > 0):
        positivos += 1
        soma += entrada

media = soma/positivos

print(f"{positivos} valores positivos")
print(f'{media:.1f}')