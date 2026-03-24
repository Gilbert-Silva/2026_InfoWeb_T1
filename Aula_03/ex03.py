x = [1, 2, 3]
y = x
y.append(4)
print(x)
print(type(x), type(y))

class Triangulo:
    def __init__(self):
        self.b = 0        # atributos
        self.h = 0
    def calc_area(self):  # método
        return self.b * self.h / 2

# x é uma referência - alguém que armazena o endereço de um objeto
# Triangulo() cria um objeto (ou instância) da classe
x = Triangulo()
print(x)
y = x
print(y)
y.b = 10
print(x.b)

x = 0