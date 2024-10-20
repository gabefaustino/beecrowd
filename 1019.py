entrada_segundos = int(input())

horas = entrada_segundos // 3600
entrada_segundos = entrada_segundos % 3600

minutos = entrada_segundos //60
entrada_segundos = entrada_segundos % 60

segundos = entrada_segundos

print(f"{horas}:{minutos}:{segundos}")