from datetime import datetime

class Pais:
    def __init__(self, id, nome, sigla, grupo):
        self.set_id(id)
        self.set_nome(nome)
        self.set_sigla(sigla)
        self.set_grupo(grupo) 
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_sigla(self, sigla):
        if sigla == "": raise ValueError("Sigla não pode ser vazio")
        self.__sigla = sigla
    def set_grupo(self, grupo):
        if grupo == "": raise ValueError("Grupo não pode ser vazio")
        self.__grupo = grupo
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_sigla(self): return self.__sigla   
    def get_grupo(self): return self.__grupo
    def to_json(self):
        return { "id":self.__id, "nome":self.__nome, "sigla":self.__sigla, "grupo":self.__grupo }
    @staticmethod
    def from_json(dic):
        return Pais(dic["id"], dic["nome"], dic["sigla"], dic["grupo"])
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__sigla} - {self.__grupo}"
    
class Jogo:
    def __init__(self, id, id_pais1, id_pais2, gols1, gols2, fase, data_hora):
        self.set_id(id)
        self.set_id_pais1(id_pais1)
        self.set_id_pais2(id_pais2)
        self.set_gols1(gols1)
        self.set_gols2(gols2)
        self.set_fase(fase)
        self.set_data_hora(data_hora) 
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_id_pais1(self, id_pais1):
        if id_pais1 < 0: raise ValueError("Id_pais1 deve ser positivo")
        self.__id_pais1 = id_pais1
    def set_id_pais2(self, id_pais2):
        if id_pais2 < 0: raise ValueError("Id_pais2 deve ser positivo")
        self.__id_pais2 = id_pais2
    def set_gols1(self, gols1):
        if gols1 < 0: raise ValueError("Gols1 deve ser positivo")
        self.__gols1 = gols1
    def set_gols2(self, gols2):
        if gols2 < 0: raise ValueError("Gols2 deve ser positivo")
        self.__gols2 = gols2
    def set_fase(self, fase):
        if fase == "": raise ValueError("Fase não pode ser vazia")
        self.__fase = fase
    def set_data_hora(self, data_hora):
        if type(data_hora) != datetime: raise ValueError("Deve ser uma data")
        self.__data_hora = data_hora
    def get_id(self): return self.__id
    def get_id_pais1(self): return self.__id_pais1
    def get_id_pais2(self): return self.__id_pais2
    def get_gols1(self): return self.__gols1
    def get_gols2(self): return self.__gols2
    def get_fase(self): return self.__fase
    def get_data_hora(self): return self.__data_hora   
    def to_json(self):
        return { "id":self.__id, "id_pais1":self.__id_pais1, "id_pais2":self.__id_pais2, "gols1":self.__gols1, "gols2":self.__gols2, "fase":self.__fase, "data_hora":self.__data_hora.strftime('%d/%m/%Y %H:%M') }
    @staticmethod
    def from_json(dic):
        return Jogo(dic["id"], dic["id_pais1"], dic["id_pais2"], dic["gols1"], dic["gols2"], dic["fase"], datetime.strptime(dic["data_hora"], '%d/%m/%Y %H:%M'))
    def __str__(self):
        return f"{self.__id} - {self.__id_pais1} - {self.__id_pais2} - {self.__gols1} - {self.__gols2} - {self.__fase} - {self.__data_hora}"

class UI:
    paises = []
    jogos = []
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir_pais()
            if op == 2: UI.listar_pais()
            if op == 3: UI.inserir_jogo()
            if op == 4: UI.listar_jogo()

    @staticmethod
    def menu():
        print("1-Inserir país, 2-Listar países, 3-Inserir jogo, 4-Listar jogos, 9-Fim")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir_pais(cls):
        print("Insira os dados do país")
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        sigla = input("Informe a sigla: ")
        grupo = input("Informe o grupo: ")
        x = Pais(id, nome, sigla, grupo)
        cls.paises.append(x)

    @classmethod
    def listar_pais(cls):
        for x in cls.paises: print(x)

    @classmethod
    def inserir_jogo(cls):
        print("Insira os dados do jogo")
        id = int(input("Informe o id: "))
        id_pais1 = int(input("Informe o id do país 1: "))
        id_pais2 = int(input("Informe o id do país 2: "))
        gols1 = int(input("Informe os gols do país 1: "))
        gols2 = int(input("Informe os gols do país 2: "))
        fase = input("Informe a fase: ")
        data_hora = datetime.strptime(input("Informe a data e hora: "), "%d/%m/%Y %H:%M")
        x = Jogo(id, id_pais1, id_pais2, gols1, gols2, fase, data_hora)
        cls.jogos.append(x)

    @classmethod
    def listar_jogo(cls):
        for x in cls.jogos: print(x)

UI.main()





