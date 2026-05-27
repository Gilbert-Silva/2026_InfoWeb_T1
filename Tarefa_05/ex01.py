from datetime import datetime, timedelta
class Treino:
    def __init__(self, id, data, distancia, tempo):
        self.set_id(id)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    def set_id(self, id):
        if id < 0: raise ValueError("Id não pode ser negativo")
        self.__id = id
    def set_data(self, data):
        if data > datetime.now(): raise ValueError("Data não pode estar no futuro")
        self.__data = data
    def set_distancia(self, distancia):
        if distancia < 0: raise ValueError("Distância não pode ser negativa")
        self.__distancia = distancia
    def set_tempo(self, tempo):
        if tempo < timedelta(0): raise ValueError("Tempo não pode ser negativo")
        self.__tempo = tempo
    def get_id(self) : return self.__id
    def get_data(self): return self.__data
    def get_distancia(self): return self.__distancia
    def get_tempo(self): return self.__tempo
    def __str__(self): 
        return f"{self.__id} - {self.__data} - {self.__distancia} - {self.__tempo}"

class TreinoUI:
    treinos = []
    @classmethod
    def main(cls):
        op = 0
        while op != 9:
            op = cls.menu()
            if op == 1: cls.inserir()
            if op == 2: cls.listar()

    @classmethod
    def menu(cls):
        print("1-Inserir 2-Listar 9-Fim")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: ")) 
        data = datetime.strptime(input("Informe a data no formato dd/mm/aaaa: "), "%d/%m/%Y")
        distancia = float(input("Informe a distância em km: "))
        tempo = input("Informe o tempo hh:mm:ss: ")
        h, m, s = map(int, tempo.split(":"))
        t = timedelta(hours=h, minutes=m, seconds=s)
        x = Treino(id, data, distancia, t)
        cls.treinos.append(x)
    
    @classmethod
    def listar(cls):
        for x in cls.treinos: print(x)

TreinoUI.main()