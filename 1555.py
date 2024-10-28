def rafael (x,y):
    r = ((3*x)**2) + (y**2)
    return r

def beto (x,y):
    b = (2*(x**2)) + ((5*y)**2)
    return b

def carlos (x,y):
    c = (-100*x) + (y**3)
    return c


entrada = int(input())

for i in range(entrada):
    valores = input().split()

    x = int(valores[0])
    y = int(valores[1])

    r = int(rafael(x,y))
    b = int(beto(x,y))
    c = int(carlos(x,y))

    if (b < r > c):
        print("Rafael ganhou")
    elif (r < b > c):
        print("Beto ganhou")
    elif (r < c > b):
        print("Carlos ganhou")