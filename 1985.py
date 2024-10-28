entrada = int(input())
pagar = 0

for i in range(entrada):
    valores = input().split()

    produto= float(valores[0])
    quantidade = float(valores[1])

    if (produto == 1001):
        pagar += 1.50 * quantidade
    elif (produto == 1002):
        pagar += 2.50 * quantidade
    elif (produto == 1003):
        pagar += 3.50 * quantidade
    elif (produto == 1004):
        pagar += 4.50 * quantidade
    elif (produto == 1005):
        pagar += 5.50 * quantidade

print(f"{pagar:.2f}")