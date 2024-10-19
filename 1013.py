def maior_abs(a, b, c):
    maior = int((a + b + (abs(a-b))) / 2)
    if (c > maior):
        maior = c
    return maior

entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

print(f"{maior_abs(a,b,c)} eh o maior")