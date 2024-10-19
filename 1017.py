tempo_de_viagem = int(input()) #horas
velocidade_media = int(input()) #km/h


distancia = velocidade_media * tempo_de_viagem
litros = distancia / 12 #12km/l

print(f"{litros:.3f}")