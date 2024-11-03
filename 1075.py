div = int(input())

for i in range(1, 10000+1):
    if (i % div == 2 and div < 10000):
        print(i)