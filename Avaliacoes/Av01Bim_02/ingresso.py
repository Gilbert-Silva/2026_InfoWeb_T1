class Ingresso:
    def __init__(self, id, evento, data, valor):
        self.set_id(id)
        self.set_evento(evento)
        self.set_data(data)
        self.set_valor(valor)
    def __str__(self):
        return f"{self.__id} - {self.__evento} - {self.__data} - {self.__valor}"
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_evento(self, evento):
        if evento == "": raise ValueError("Evento não pode ser vazio")
        self.__evento = evento
    def set_data(self, data):
        self.__data = data
    def set_valor(self, valor): 
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__valor = valor
    def get_id(self): return self.__id
    def get_evento(self): return self.__evento
    def get_data(self): return self.__data
    def get_valor(self): return self.__valor

class UI:
    lista = []
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.total()
    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Total 4-Sair")
        return int(input("Escolha uma opção: "))        
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        evento = input("Informe o evento: ")
        data = input("Informe a data: ")
        valor = float(input("Informe o valor: "))
        x = Ingresso(id, evento, data, valor)
        cls.lista.append(x)
    @classmethod
    def listar(cls):
        for x in cls.lista: print(x)
    @classmethod
    def total(cls):
        soma = 0
        for x in cls.lista: 
            soma += x.get_valor()
        print(soma)

UI.main()            


# Q1 - Atributo  - 6
#    - Init      - 6
#    - Validação - 6
#    - Get/Set   - 6
#    - Str       - 6
# Q2 - Main+Atributo - 8
#    - Menu          - 8
#    - Inserir       - 8
#    - Listar        - 8
#    - Total         - 8
# Q3 - Atributos - 3
#    - Métodos   - 3
#    - Parâmetros- 3
#    - Retorno   - 3
#    - Visibilidade - 3

