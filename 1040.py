def calcular_mediaPD (n1, p1, n2, p2, n3, p3, n4, p4):
    media = ((n1 * p1) + (n2 * p2) + (n3 * p3) + (n4 * p4)) / (p1 + p2 + p3 + p4)
    return media


notas = input().split()

nota_1 = float(notas[0])
nota_2 = float(notas[1])
nota_3 = float(notas[2])
nota_4 = float(notas[3])

peso_1 = 2
peso_2 = 3
peso_3 = 4
peso_4 = 1

mediaPD = calcular_mediaPD (nota_1, peso_1, 
                            nota_2, peso_2, 
                            nota_3, peso_3, 
                            nota_4, peso_4)


if (mediaPD >= 7.0):
    print(f"Media: {mediaPD:.1f}")
    print(f"Aluno aprovado.")

elif (5.0 <= mediaPD < 7.0):
    print(f"Media: {mediaPD:.1f}")
    print("Aluno em exame.")
    nota_final = float(input())
    print(f"Nota do exame: {nota_final:.1f}")
    nova_media = (mediaPD + nota_final) / 2

    if (nova_media >= 5.0):
        print("Aluno aprovado.")
        print(f"Media final: {nova_media:.1f}")
    else:
        print("Aluno reprovado.")
        print(f"Media final: {nova_media:.1f}")

else:
    print(f"Media: {mediaPD:.1f}")
    print(f"Aluno reprovado.")