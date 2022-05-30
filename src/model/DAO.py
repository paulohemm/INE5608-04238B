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

    def remover(self, key):
        try:
            self._temp.pop(key)
            self.__salva()
        except:
            raise KeyError

    def capturar(self, chave):
        try:
            return self._temp[chave]
        except:
            raise KeyError