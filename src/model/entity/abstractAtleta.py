from abc import ABC, abstractmethod
from .abstractUsuario import Usuario

class Atleta(Usuario):
    def __init__(self, cpf, senha, idade, peso):
        super().__init__(cpf, senha)
        self._idade = idade
        self._peso = peso

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso
