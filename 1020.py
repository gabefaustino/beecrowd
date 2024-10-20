entrada_dias = int(input())


anos = entrada_dias // 365
entrada_dias = entrada_dias % 365

meses = entrada_dias // 30
entrada_dias = entrada_dias % 30

dias = entrada_dias

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")