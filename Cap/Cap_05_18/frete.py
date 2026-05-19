class Frete:
    def __init__(self, d : float, p : float):
        self.set_distancia(d)
        self.set_peso(p)
    def set_distancia(self, d : float):
        if d < 0: raise ValueError("A distância não pode ser negativa")
        self.__distancia = d
    def set_peso(self, p : float):
        if p < 0: raise ValueError("O peso não pode ser negativo")
        self.__peso = p
    def get_distancia(self):
        return self.__distancia
    def get_peso(self):
        return self.__peso
    def calc_frete(self):
        return 0.01 * self.__distancia * self.__peso 
    def __str__(self):    
        #return str(self.__distancia) + " - " + str(self.__peso)
        return f"Frete: {self.__distancia} km - {self.__peso} kg"
    
class UI:
    @staticmethod
    def main():  
        d = float(input("Qual a distância até o destino em km? "))
        p = float(input("Qual o peso do produto em kg? "))
        x = Frete(d, p)   # __init__
        print(x)          # __str__
        print("Total em reais:", x.calc_frete())
        print(x.get_distancia(), "km")
        print(x.get_peso(), "kg")
        p = float(input("Qual o peso correto em kg? "))
        x.set_peso(p)
        print("Total em reais:", x.calc_frete())

UI.main()





