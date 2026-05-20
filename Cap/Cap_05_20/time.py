class Time:
    def __init__(self, i, n, e):  # faz o set de todos os atributos
        self.set_id(i)
        self.set_nome(n)
        self.set_estado(e)
    def __str__(self):   # faz o get de todos os atributos
        return f"{self.__id} - {self.__nome} - {self.__estado}"
        #return f"{self.get_id()} - {self.get_nome()} - {self.get_estado()}"
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_estado(self, estado): 
        estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",\
                   "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",\
                    "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        if estado not in estados: raise ValueError("Estado inválido")
        self.__estado = estado
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_estado(self): return self.__estado              

#x = Time(1, "América", "RN")
#y = Time(2, "ABC", "RN")
#print(x)
#print(y)

class UI:
    times = []  # Lista de times
    def main():
        op = 0
        while op != 9:
            op = UI.menu()  # Lê a opção do usuário
            if op == 1: UI.inserir_time()
            if op == 2: UI.listar_time()
            if op == 3: UI.atualizar_time()
            if op == 4: UI.excluir_time()
    def menu():
        print("1-Inserir time, 2-Listar times, 3-Atualizar time, 4-Excluir time, 9-Sair")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir_time(cls):   # Create
        id = int(input("Informe o id: "))  # Lê os dados do time
        nome = input("Informe o nome: ")
        estado = input("Informe o estado: ")
        x = Time(id, nome, estado)         # Cria o objeto Time
        cls.times.append(x)                # Insere o time na lista
    @classmethod
    def listar_time(cls):    # Read
        for x in cls.times: print(x)       # Percorre a lista e mostra cada time
    @classmethod
    def atualizar_time(cls): # Update
        UI.listar_time()
        id = int(input("Informe o id do time a atualizar: "))
        for x in cls.times:
            if x.get_id() == id:
                nome = input("Informe o novo nome: ")
                estado = input("Informe o novo estado: ")
                x.set_nome(nome)
                x.set_estado(estado)
                print("Time atualizado com sucesso!")
    @classmethod
    def excluir_time(cls):   # Delete         
        id = int(input("Informe o id do time a excluir: "))
        for x in cls.times:
            if x.get_id() == id:
                cls.times.remove(x)
                print("Time excluído com sucesso!")

UI.main()    