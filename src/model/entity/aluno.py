from .abstractAtleta import Atleta

class Aluno(Atleta):
    def __init__(self, cpf, senha, idade, peso, nivel='Iniciante'):
        super().__init__(cpf, senha, idade, peso)
        self._nivel = nivel

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel
