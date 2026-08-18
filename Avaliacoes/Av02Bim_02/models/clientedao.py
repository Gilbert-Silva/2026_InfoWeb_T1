from models.cliente import Cliente
import json

class ClienteDAO:
    def __init__(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        # av1: percorre a lista procurando um id já existente
        for aux in self.__objetos:                # laço - 5
            if aux.get_id() == obj.get_id():      # teste - 5
                raise ValueError("Id já existe")  # raise - 5

        # av2: gerar um novo id com o maior valor existente mais 1
        id = 0
        if len(self.__objetos) > 0:
            for aux in self.__objetos:                  # laço - 5
                if aux.get_id() > id: id = aux.get_id() # teste - 5
        obj.set_id(id + 1)                              # novo id - 5

        self.__objetos.append(obj) # adicionar - 5
        self.__salvar()            # salvar - 5

    def listar(self):                
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id: return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):  
        try:  
            arquivo = open(self.__arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self.__objetos = []
            for dic in list_dic:
                obj = Cliente.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass

    def __salvar(self):    
        arquivo = open(self.__arquivo, mode = "w")
        json.dump(self.__objetos, arquivo, default = Cliente.to_json, indent = 2)
        arquivo.close()
        
