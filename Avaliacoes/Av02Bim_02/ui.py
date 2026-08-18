from service import Service
from datetime import datetime

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.servico_inserir()
            if op == 6: UI.servico_listar()
            if op == 7: UI.servico_atualizar()
            if op == 8: UI.servico_excluir()
            if op == 9: UI.clientes_sem_compras_recentes()

    @staticmethod
    def menu():
        print("----------- Cadastro de Clientes ----------")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print("----------- Cadastro de Serviços ----------")
        print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print("----------- Outras opções -----------------")
        print("9-Clientes sem compras recentes, 10-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def cliente_inserir():
        id = int(input("Informe o id: "))   # inputs - 5
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ") # strptime - 5
        data = datetime.strptime(input("Informe a data da última compra: "), "%d/%m/%Y")
        Service.cliente_inserir(id, nome, email, fone, data) # inserir - 5

    @staticmethod
    def cliente_listar():  # laço - 5
        for obj in Service.cliente_listar(): print(obj) # service - 5

    @staticmethod
    def clientes_sem_compras_recentes():
        for obj in Service.clientes_sem_compras_recentes(): print(obj)

    @staticmethod
    def cliente_atualizar():
        for obj in Service().cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo telefone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        for obj in Service().cliente_listar(): print(obj)
        id = int(input("Informe o id do cliente a ser excluído: "))
        Service.cliente_excluir(id)

    @staticmethod
    def servico_inserir():
        id = int(input("Informe o id: "))
        descricao = input("Informe a descrição: ")
        valor = float(input("Informe o valor: "))
        Service.servico_inserir(id, descricao, valor)

    @staticmethod
    def servico_listar():
        for obj in Service.servico_listar(): print(obj)

    @staticmethod
    def servico_atualizar():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        valor = float(input("Informe o novo valor: "))
        Service.servico_atualizar(id, descricao, valor)

    @staticmethod
    def servico_excluir():
        for obj in Service().servico_listar(): print(obj)
        id = int(input("Informe o id do serviço a ser excluído: "))
        Service.servico_excluir(id)

UI.main()
