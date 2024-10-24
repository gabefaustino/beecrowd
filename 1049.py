entrada_1 = str(input())

if (entrada_1 == "vertebrado"):
    entrada_2 = str(input())
    if (entrada_2 == "ave"):
        entrada_3 = str(input())
        if (entrada_3 == "carnivoro"):
            print("aguia")
        elif (entrada_3 == "onivoro"):
            print("pomba")
    elif (entrada_2 == "mamifero"):
        entrada_3 = str(input())
        if (entrada_3 == "onivoro"):
            print("homem")
        elif (entrada_3 == "herbivoro"):
            print("vaca")
elif (entrada_1 == "invertebrado"):
    entrada_2 = str(input())
    if (entrada_2 == "inseto"):
        entrada_3 = str(input())
        if (entrada_3 == "hematofago"):
            print("pulga")
        elif (entrada_3 == "herbivoro"):
            print("lagarta")
    elif (entrada_2 == "anelideo"):
        entrada_3 = str(input())
        if (entrada_3 == "hematofago"):
            print("sanguessuga")
        elif (entrada_3 == "onivoro"):
            print ("minhoca")