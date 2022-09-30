fib1 = fib2 = 1
n = int(input())
while True:
    fib1, fib2 = fib2, fib1 + fib2
    if fib2 > n:
        print(fib2)
        break
