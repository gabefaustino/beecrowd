x = int(input())
y = int(input())

soma = 0

if (x < y): #crescente
    for i in range(x+1, y):
        if (i % 2 != 0):
            soma += i
    print(soma)

elif (x > y): #decrescente
    for i in range(y+1, x):
        if (i % 2 != 0):
            soma += i
    print(soma)

else:
    print(0)