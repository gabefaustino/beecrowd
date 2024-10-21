entrada = float(input())

if (entrada >= 0 and entrada <= 25):
    print(f"Intervalo [0,25]")
elif (entrada > 25 and entrada <= 50):
    print(f"Intervalo (25,50]")
elif (entrada > 50 and entrada <= 75):
    print(f"Intervalo (50,75]")
elif (entrada > 75 and entrada <= 100):
    print(f"Intervalo (75,100]")
else:
    print("Fora de intervalo")