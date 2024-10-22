entrada = input().split()

num_1 = int(entrada[0])
num_2 = int(entrada[1])

if (num_1 % num_2 == 0) or (num_2 % num_1 == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")