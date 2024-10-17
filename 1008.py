funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora_trabalhada = float(input())

def calculo_salario(horas_trabalhadas, valor_hora_trabalhada):
    salario = horas_trabalhadas * valor_hora_trabalhada
    return salario

salario = calculo_salario(horas_trabalhadas, valor_hora_trabalhada)
print(f"NUMBER = {funcionario}\n" f"SALARY = U$ {salario:.2f}")