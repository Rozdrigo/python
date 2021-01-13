res = 0
for x in range(1000):
    if x%5 == 0 and x%2 == 0 and x%6 != 0:
        res += 1
print("{NUM} são multiplos de 5 e de 2 mas não são multiplos de 6." .format(NUM = res))