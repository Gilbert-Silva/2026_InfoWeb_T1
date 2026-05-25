class Frete:
    def __init__(self, id: int, d : float, p : float):
        self.set_id(id)
        self.set_distancia(d)
        self.set_peso(p)
    def set_id(self, id : int):
        if id < 0: raise ValueError("O id não pode ser negativo")
        self.__id = id
    def set_distancia(self, d : float):
        if d < 0: raise ValueError("A distância não pode ser negativa")
        self.__distancia = d
    def set_peso(self, p : float):
        if p < 0: raise ValueError("O peso não pode ser negativo")
        self.__peso = p
    def get_id(self):
        return self.__id
    def get_distancia(self):
        return self.__distancia
    def get_peso(self):
        return self.__peso
    def calc_frete(self):
        return 0.01 * self.__distancia * self.__peso 
    def __str__(self):    
        #return str(self.__distancia) + " - " + str(self.__peso)
        return f"Frete: {self.__id} - {self.__distancia} km - {self.__peso} kg"
    
class UI:
    lista = []
    @staticmethod
    def main():
        op = 0 
        while op != 5:
            op = UI.menu()
            if op == 1: UI.inserir()   # C reate
            if op == 2: UI.listar()    # R ead
            if op == 3: UI.atualizar() # U pdate
            if op == 4: UI.excluir()   # D elete
    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-Fim")
        return int(input("Escolha um opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))  
        d = float(input("Qual a distância até o destino em km? "))
        p = float(input("Qual o peso do produto em kg? "))
        x = Frete(id, d, p)   
        cls.lista.append(x)
    @classmethod
    def listar(cls):
        for x in cls.lista:
            print(x)          
            print("Total em reais:", x.calc_frete())
    @classmethod
    def atualizar(cls):
        for x in cls.lista: print(x)
        id = int(input("Informe o id do frete a ser alterado: "))
        for x in cls.lista:
            if x.get_id() == id:
                d = float(input("Qual a nova distância até o destino em km? "))
                p = float(input("Qual o novo peso do produto em kg? "))
                x.set_distancia(d)
                x.set_peso(p)
    @classmethod
    def excluir(cls):
        for x in cls.lista: print(x)
        id = int(input("Informe o id do frete a ser excluído: "))
        for x in cls.lista:
            if x.get_id() == id:
                cls.lista.remove(x)


UI.main()





