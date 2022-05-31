import pickle
from abc import ABC

class DAO(ABC):
    def __init__(self, datapath):
        self._datapath = 'src/model/database/' + datapath
        self._temp = {}
        try:
            self.__carrega()
        except FileNotFoundError:
            self.__salva()        

    def __salva(self):
        file = open(self._datapath, 'wb')
        pickle.dump(self._temp, file)
        file.close()
    
    def __carrega(self):
        file = open(self._datapath, 'rb')
        self._temp = pickle.load(file)

    def adicionar(self, chave, objeto):
        self._temp[chave] = objeto
        self.__salva()
        print(objeto.cpf) #apenas pra teste retirar apos

    def remover(self, chave):
        try:
            self._temp.pop(chave)
            self.__salva()
        except:
            raise KeyError

    def capturar(self, chave):
        try:
            print(self._temp[chave].cpf) #apenas pra teste retirar apos
            return self._temp[chave]
        except:
            raise KeyError

    def listar(self):
        print(self._temp.values()) #apenas pra teste retirar apos
        return self._temp.values()
