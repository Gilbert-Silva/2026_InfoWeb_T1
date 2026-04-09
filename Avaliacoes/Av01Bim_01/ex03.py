# 3
class Retangulo:
    def __init__(self):
        self.base = 0     # 5 pontos
        self.altura = 0   # 5 pontos
    def diagonal(self):    
        return (self.base ** 2 + self.altura ** 2) ** 0.5  # 10 pontos

# 4    
x = Retangulo()           # 6 pontos
x.base = float(input("Entre o valor da base: "))   
x.altura = float(input("Entre o valor da altura: "))
diagonal = x.diagonal()
print(diagonal)


