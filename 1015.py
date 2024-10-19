p_01 = input().split()
p_02 = input().split()

x1 = float(p_01[0])
y1 = float(p_01[1])
x2 = float(p_02[0])
y2 = float(p_02[1])


distancia = (((x2 - x1)**2) + ((y2 -y1)**2))**(1/2) #sqrt

print(f"{distancia:.4f}")