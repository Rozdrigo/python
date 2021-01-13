n = int(input('Dada a posição: '))
res = 1
for x in range(n):
    pow = 1
    for y in range(x+1):
        pow *= 2
    res += pow
print('O número retornado é: {NUM}' .format(NUM = res))