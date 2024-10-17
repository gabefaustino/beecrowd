pressao_desejada = int(input())
pressao_lida = int(input())

def calculo_dif_pressao (pressao_desejada, pressao_lida):
    diferenca = pressao_desejada - pressao_lida
    return diferenca

diferenca = calculo_dif_pressao(pressao_desejada, pressao_lida)
print(diferenca)