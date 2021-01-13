n = int(input('Dado [N] igual a: '))
for x in range(n):
    if (x+1) * (x+1) == n:
        print('[N] é um quadrado perfeito')
        break
    elif x+1 == n:
        print('[N] não é um quadrado perfeito')
