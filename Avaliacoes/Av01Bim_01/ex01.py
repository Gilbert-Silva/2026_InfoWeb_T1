x = 5
y = 10
print(1 - 2 + 3 * x)               # 14:  multiplicação é feita primeiro
print(1 / 2 * 3 + x)               # 6.5: divisão, multiplicação, soma
print(x < y <= 2 * x)              # True: 5 < 10 <= 10
print(x > 5 and y > 10 or x == 10) # False 
#     5 > 5  e  10 > 10 ou 5 == 10
#     False  e   False ou False

x = 10
y = 5
print(2 - 4 + 3 * x)                 # 28: primeiro a multiplicação
print(2 / 4 * 3 + x)                 # 11.5: divisão, multiplicação, soma
print(x < y < 2 * x)                 # False: 10 < 5 < 20
print(x > 5 and y > 10 or x == 10)   # True
#     10 > 5 e 5 > 10 ou 10 == 10
#     True   e  False ou True



