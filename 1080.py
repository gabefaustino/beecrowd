rep = 100
posicao = 0
maior = 0

for i in range(rep):
    entrada = int(input())
    if (entrada > maior):
        maior = entrada
        posicao = i+1

print(maior)
print(posicao)