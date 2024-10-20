entrada = input().split()

dias = int(entrada[0])
saldo = int(entrada[1])

menor_saldo = saldo

for i in range(dias):
    movimentacao = int(input())

    if (movimentacao > 0):
        saldo += movimentacao
        if (saldo < menor_saldo):
            menor_saldo = saldo

    elif (movimentacao < 0):
        saldo += movimentacao #movimentação já é negativa ( - com - = +)
        if (saldo < menor_saldo):
            menor_saldo = saldo


print(menor_saldo)