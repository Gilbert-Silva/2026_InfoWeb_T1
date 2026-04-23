# Entidade
class Triangulo:
    def __init__(self, b, h):
        #self.__b = 0.0
        #self.__h = 0.0
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_altura(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2
    def __str__(self):
        return f"Eu sou um triângulo, minha base é {self.__b} e minha altura é {self.__h}"

class Circulo:
    pass


# Interface com usuário (User Interface) - prints, inputs
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()

    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def triangulo():
        print("Cálculo da área do triângulo")
        b = float(input("Informe o valor da base: "))
        h = float(input("Informe o valor da altura: "))
        x = Triangulo(b, h)
        area = x.calc_area()
        print(x)
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")

    @staticmethod
    def circulo():
        print("Em construção")

UI.main()