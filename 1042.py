entrada = input().split()

ordenados = []

for i in entrada:
    valor_int = int(i)
    ordenados.append(valor_int)

ordenados.sort()

for i in ordenados:
    print(i)
print()
for i in entrada:
    print(i)