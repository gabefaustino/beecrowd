def corretos (tipo_cha, respostas):
    soma = 0
    for i in range(len(respostas)):
        respostas[i] = int(respostas[i])
        if tipo_cha == respostas[i]:
            soma += 1
        else:
            continue
    return soma

tipo_cha = int(input())
respostas = input().split()

soma = corretos (tipo_cha, respostas)

print(soma)