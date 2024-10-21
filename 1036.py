def bhaskara (a, b, c):
    
    if (a == 0):
        return("Impossivel calcular")
    
    delta = (b**2) - (4*a*c)

    if (delta < 0):
        return("Impossivel calcular")
    
    r1 = (-b + (delta**0.5)) / (2*a)
    r2 = (-b - (delta**0.5)) / (2*a)
    return r1, r2


entrada = input().split()

a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])


resultado = bhaskara(a,b,c)


if isinstance(resultado, str):   #verifica se a variável resultado (tupla do return) é do tipo str
    print(resultado)
else:
    r1, r2 = resultado #python espera que resultado seja uma tupla ou uma sequencia de dois elementos
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")