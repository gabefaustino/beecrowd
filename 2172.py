def exp_monstro(multiplicador, xp_inicial):
    exp = multiplicador*xp_inicial
    return exp


while (True):
    entrada = input().split()
    multiplicador = int(entrada[0])
    xp_inicial = int(entrada[1])
    if (multiplicador == 0  and xp_inicial == 0):
        break
    else:
        print(exp_monstro(multiplicador, xp_inicial))