n = int(input())
n1 = 0
n2 = 0
m = 10000
while n > 0:
    n2 = n % 10
    n1 += n2 * m
    n -= n2
    n /= 10
    m /= 10
print(int(n1))
    
