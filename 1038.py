entrada = input().split()

codigo = int(entrada[0])
quantidade = int(entrada[1])

lista = [4.00, 4.50, 5.00, 2.00, 1.50]

total = quantidade*(lista[codigo-1])

print(f"Total: R$ {total:.2f}")