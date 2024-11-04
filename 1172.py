vetor = []

for i in range(10):
    valor = int(input())
    if (valor > 0):
        vetor.append(valor)
    else:
        vetor.append(1)

for i in range(len(vetor)):
    print(f"X[{i}] = {vetor[i]}")