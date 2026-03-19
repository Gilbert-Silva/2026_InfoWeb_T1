print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
sp = 0   # soma dos pares
si = 0   # soma dos ímpares
if a % 2 == 0: sp += a 
else: si += a
if b % 2 == 0: sp += b 
else: si += b
if c % 2 == 0: sp += c 
else: si += c
if d % 2 == 0: sp += d 
else: si += d
print("Soma dos pares:", sp)
print("Soma dos ímpares:", si)
