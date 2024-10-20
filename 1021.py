valor = float(input())

# Convertendo para centavos para evitar problemas com ponto flutuante
centavos = int(round(valor * 100))

# Cálculo das notas
nota_100 = centavos // 10000
centavos %= 10000

nota_50 = centavos // 5000
centavos %= 5000

nota_20 = centavos // 2000
centavos %= 2000

nota_10 = centavos // 1000
centavos %= 1000

nota_5 = centavos // 500
centavos %= 500

nota_2 = centavos // 200
centavos %= 200

# Cálculo das moedas
moeda_1 = centavos // 100
centavos %= 100

moeda_50 = centavos // 50
centavos %= 50

moeda_25 = centavos // 25
centavos %= 25

moeda_10 = centavos // 10
centavos %= 10

moeda_5 = centavos // 5
centavos %= 5

moeda_1c = centavos // 1

# Saída
print("NOTAS:")
print(f"{nota_100} nota(s) de R$ 100.00")
print(f"{nota_50} nota(s) de R$ 50.00")
print(f"{nota_20} nota(s) de R$ 20.00")
print(f"{nota_10} nota(s) de R$ 10.00")
print(f"{nota_5} nota(s) de R$ 5.00")
print(f"{nota_2} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moeda_1} moeda(s) de R$ 1.00")
print(f"{moeda_50} moeda(s) de R$ 0.50")
print(f"{moeda_25} moeda(s) de R$ 0.25")
print(f"{moeda_10} moeda(s) de R$ 0.10")
print(f"{moeda_5} moeda(s) de R$ 0.05")
print(f"{moeda_1c} moeda(s) de R$ 0.01")