def calcular_soma(nota1, nota2):
    soma = nota1 + nota2
    return soma

nota1 = int(input())
nota2 = int(input())

soma = calcular_soma(nota1, nota2)
print(f"X = {soma}")