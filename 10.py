n = input('Введите число:')
nl = list(n)
 
Maxn=max(nl) 
Minn=min(nl) 
 
print('Максимальная цифра =', Maxn)
print('Минимальная цифра =', Minn)
 
Poz1 = nl.index(Maxn) 
Poz2 = nl.index(Minn) 
 
if Poz1 < Poz2:
    print('Левее находится максимальная цифра =', Maxn)
else:
    print('Левее находится минимальная цифра =', Minn)
