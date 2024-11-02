entrada = int(input())

for i in range(entrada):
    valor = int(input())
    if (valor % 2 == 0) and (valor > 0):
        print("EVEN POSITIVE")
    elif (valor % 2 == 0) and (valor < 0):
        print("EVEN NEGATIVE")
    
    elif (valor % 2 != 0) and (valor > 0):
        print("ODD POSITIVE")
    elif (valor % 2 != 0) and (valor < 0):
        print("ODD NEGATIVE")
        
    else:
        print("NULL")