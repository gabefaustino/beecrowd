entrada = input().split()
numero1 = int(entrada[0])
numero2 = int(entrada[1])

while (numero1 != numero2):
    if (numero1 < numero2):
        print("Crescente")
    else:
        print("Decrescente")
    entrada = input().split()
    numero1 = int(entrada[0])
    numero2 = int(entrada[1])
