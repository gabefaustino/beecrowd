entrada = input().split()

ordenada = []

for i in entrada:
    valor_float = float(i)
    ordenada.append(valor_float)

ordenada.sort()     #ordenada.sort(reverse=True) ordena inversamente

a = ordenada[2]
b = ordenada[1]
c = ordenada[0]

if (a >= (b+c)):
    print("NAO FORMA TRIANGULO")
else:
    if (a**2 == (b**2 + c**2)):
        print("TRIANGULO RETANGULO")
    if (a**2 > (b**2 + c**2)):
        print("TRIANGULO OBTUSANGULO")
    if (a**2 < (b**2 + c**2)):
        print("TRIANGULO ACUTANGULO")
    if (a == b == c):
        print("TRIANGULO EQUILATERO")
    elif (a == b or b == c or a == c):
        print("TRIANGULO ISOSCELES")