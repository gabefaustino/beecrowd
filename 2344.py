def calculo_conceito (nota):
    if nota == 0:
        return"E"
    elif 1 <= nota <= 35:
        return "D"
    elif 36 <= nota <= 60:
        return "C"
    elif 61 <= nota <= 85:
        return "B"
    elif 86 <= nota <= 100:
        return "A"


nota = int(input())

print(calculo_conceito(nota))