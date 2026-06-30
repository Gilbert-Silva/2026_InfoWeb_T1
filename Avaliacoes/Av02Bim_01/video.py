from datetime import timedelta
class Video:
    def __init__(self, id, nome, canal, duracao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_canal(canal)
        self.set_duracao(duracao)
    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError()
        self.__nome = nome
    def set_canal(self, canal):
        if canal == "": raise ValueError()
        self.__canal = canal
    def set_duracao(self, duracao):
        if duracao > timedelta(hours = 2): raise ValueError()
        self.__duracao = duracao
    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_canal(self) : return self.__canal
    def get_duracao(self) : return self.__duracao
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__canal} - {self.__duracao}"

class UI:
    objetos = []

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.tempo_total()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Tempo total, 9-Fim")
        return int(input("Informe uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: ")) 
        nome = input("Informe um nome: ")
        canal = input("Informe um canal: ")
        duracao = input("Informe a duração em hh:mm:ss :")
        h,m,s = duracao.split(":")
        d = timedelta(hours = int(h), minutes = int(m), seconds = int(s))
        x = Video(id, nome, canal, d)
        cls.objetos.append(x) 

    @classmethod
    def listar(cls):
        for x in cls.objetos: print(x)

    @classmethod
    def tempo_total(cls):  
        t = timedelta(seconds = 0)              
        for x in cls.objetos: 
            t += x.get_duracao()
        print(t)

UI.main()