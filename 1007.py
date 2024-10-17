def calcula_prod_diferenca(A, B, C, D):
    diferenca = (A*B) - (C*D)
    return diferenca

A = int(input())
B = int(input())
C = int(input())
D = int(input())

diferenca = calcula_prod_diferenca(A, B, C, D)
print(f"DIFERENCA = {diferenca}")