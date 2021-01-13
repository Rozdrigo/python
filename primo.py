n = int(input('[N] é igual a: '))
for x in range(n):
    if n % (x+1) == 0 & x != n & x != 1:
        print('portanto não é um numero primo')
        break
    elif (x+1) == n:
        print('portanto é um número primo')
