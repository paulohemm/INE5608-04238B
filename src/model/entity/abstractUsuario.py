from abc import ABC, abstractmethod

class Usuario(ABC):
    @abstractmethod
    def __init__(self, cpf, senha):
        self._cpf = cpf
        self._senha = senha

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha
