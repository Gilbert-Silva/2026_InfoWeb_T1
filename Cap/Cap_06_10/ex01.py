class Atleta:
    def __init__(self, id, nome, pais, num_gols):
        self.set_id(id)
        self.set_nome(nome)
        self.set_pais(pais)
        self.set_num_gols(num_gols)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo") 
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio") 
        self.__nome = nome
    def set_pais(self, pais):
        if pais == "": raise ValueError("País não pode ser vazio") 
        self.__pais = pais
    def set_num_gols(self, num_gols):
        if num_gols < 0: raise ValueError("Número de gols deve ser positivo") 
        self.__num_gols = num_gols
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_pais(self): return self.__pais
    def get_num_gols(self): return self.__num_gols
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__pais} - {self.__num_gols}"


class UI:
    atletas = []

    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.artilheiro()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Artilheiro, 4-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        pais = input("Informe o país: ")
        gols = int(input("Informe o número de gols: "))
        x = Atleta(id, nome, pais, gols)
        cls.atletas.append(x)

    @classmethod
    def listar(cls):
        for x in cls.atletas: print(x)

    @classmethod
    def artilheiro(cls):
        gols = 0
        for x in cls.atletas:
            if x.get_num_gols() > gols: gols = x.get_num_gols()
        print(f"Os artilheiros fizeram {gols} gols")
        for x in cls.atletas:
            if x.get_num_gols() == gols: print(x)

UI.main()    