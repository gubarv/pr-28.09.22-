n = int(input())
f, s = int(input()), int(input())
if s != 0:
    if n == f:
        print('Нет')
    else:
        if s<0:
            f, n = n, f
            s = abs(s)
        while f<n:
            f += s
        print('Да' if n == f else 'Нет')
else:
    print('Да' if n == f else 'Нет')