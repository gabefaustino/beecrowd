entrada = input().split()

hora_a = int(entrada[0])
hora_b = int(entrada[1])

if (hora_a == hora_b):
    print(f"O JOGO DUROU 24 HORA(S)")
elif (hora_a < hora_b):
    duracao = hora_b - hora_a
    print(f"O JOGO DUROU {duracao} HORA(S)")
else:
    duracao = (24 - hora_a) + hora_b
    print(f"O JOGO DUROU {duracao} HORA(S)")