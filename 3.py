from tkinter import W


a, b = int ( input ()), int ( input ())
p = 0 
i = a 
while i <= b:
    p += i**2
    i += 1
print(p)