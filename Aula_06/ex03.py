x = [1, 2, 3, 4]
y = x      # x e y são a mesma lista
y.append(5)
print(x)
z = x[:]   # z é uma nova lista que inicia com os mesmos valores de x
z.append(6)
print(x)
print(z)