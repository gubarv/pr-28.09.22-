import math
n = int(input())
i = 0
while True:
    if math.factorial(i) == n:
        print('Число:', i)
        break
    i += 1
    
    
