from datetime import datetime

class Cliente:
    def __init__(self, id, nome, email, fone, data_ultima_compra):  # 5
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_data_ultima_compra(data_ultima_compra)
    
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

    def set_data_ultima_compra(self, data_ultima_compra):   # 5
        if data_ultima_compra > datetime.now(): raise ValueError("Data deve estar no passado")
        self.__data_ultima_compra = data_ultima_compra

    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_email(self) : return self.__email
    def get_fone(self) : return self.__fone
    def get_data_ultima_compra(self) : return self.__data_ultima_compra  # 2,5

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}\
         - {self.__data_ultima_compra.strftime('%d/%m/%Y')}"   # 2,5
    
    def to_json(self): # 5
        return { "id":self.__id, "nome":self.__nome, "email":self.__email,\
         "fone":self.__fone, "data_ultima_compra":self.__data_ultima_compra.strftime('%d/%m/%Y') }
    
    @staticmethod
    def from_json(dic): # 5
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], datetime.strptime(dic["data_ultima_compra"], '%d/%m/%Y'))
