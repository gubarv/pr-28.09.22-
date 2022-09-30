d = int(input())
k = 128
while 1 <= (k := k // 2):
    n, d = divmod(d, k)
    if n > 0:
        print(k, n)
