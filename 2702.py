refeicoes = input().split()
escolhas = input().split()

passageiros_sem_escolha = 0

for i in range (len(refeicoes)):
    refeicoes[i] = int(refeicoes[i])
    escolhas[i] = int(escolhas[i])
    if (escolhas[i] > refeicoes[i]):
        passageiros_sem_escolha += escolhas[i] - refeicoes[i]

print(passageiros_sem_escolha)