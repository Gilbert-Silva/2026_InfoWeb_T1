from datetime import datetime
import json

class Contato:
    def __init__(self, id, nome, email, fone, nasc):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_nasc(nasc)
 
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError("E-mail deve ser informado")
        self.__email = email
    def set_fone(self, fone):
        if fone == "": raise ValueError("Fone deve ser informado")
        self.__fone = fone
    def set_nasc(self, nasc):
        if nasc > datetime.now(): raise ValueError("Data deve estar no passado")
        self.__nasc = nasc
 
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc

    def __str__(self): 
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc.strftime('%d/%m/%Y')}"
    
    def to_json(self):
        dic = {}
        dic["id"] = self.__id
        dic["nome"] = self.__nome
        dic["email"] = self.__email
        dic["fone"] = self.__fone
        dic["nasc"] = self.__nasc.strftime('%d/%m/%Y')
        return dic
    
    @staticmethod
    def from_json(dic):
        id = dic["id"]
        nome = dic["nome"]
        email = dic["email"]
        fone = dic["fone"]
        nasc = datetime.strptime(dic["nasc"], '%d/%m/%Y')
        return Contato(id, nome, email, fone, nasc)

class ContatoUI:
    contatos = []

    @staticmethod
    def main():
        ContatoUI.abrir()
        op = 0
        while op != 9:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.aniversariantes()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Aniversariantes, 9-Fim")
        return int(input("Informe uma opção: ")) 

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ") 
        fone = input("Informe o fone: ")
        nasc = datetime.strptime(input("Informe o nascimento: "), "%d/%m/%Y")
        x = Contato(id, nome, email, fone, nasc)
        cls.contatos.append(x)
        ContatoUI.salvar()

    @classmethod
    def listar(cls):
        for x in cls.contatos: print(x)

    @classmethod
    def aniversariantes(cls):
        mes = int(input("Informe o mês do aniversário: "))
        for x in cls.contatos:
            if x.get_nasc().month == mes:
                print(x)

    @classmethod
    def salvar(cls):
        arquivo = open("agenda.json", mode = "w")
        json.dump(cls.contatos, arquivo, default = Contato.to_json, indent = 2)
        arquivo.close()

    @classmethod
    def abrir(cls):
        try:
            cls.contatos = []
            arquivo = open("agenda.json", mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            for dic in list_dic:
                cls.contatos.append(Contato.from_json(dic))
        except Exception as erro:
            print(erro)        

ContatoUI.main()



        