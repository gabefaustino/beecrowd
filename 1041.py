entrada = input().split()

x = float(entrada[0])
y = float(entrada[1])

if (x == 0 == y):
    print("Origem")
elif ((x == 0) and (y != 0)):
    print("Eixo X")
elif ((y == 0) and (x != 0)):
    print("Eixo Y")
elif ((x > 0) and (y > 0)):
    print("Q1")
elif ((x > 0) and (y < 0)):
    print("Q4")
elif ((x < 0) and (y > 0)):
    print("Q2")
else:
    print("Q3")