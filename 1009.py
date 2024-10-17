def salario_bonus(salario_fixo, vendas_mes):
    salario = salario_fixo + (vendas_mes * 0.15)    
    return salario

nome = str(input())
salario_fixo = float(input())
vendas_mes = float(input())

salario = salario_bonus(salario_fixo, vendas_mes)
print(f"TOTAL = R$ {salario:.2f}")