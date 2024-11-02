entrada = int(input())
cont = 0
flag = False

while (flag == False):
    if (entrada % 2 != 0):
        cont+=1
        print(entrada)
    entrada+=1
    if (cont==6):
        flag = True