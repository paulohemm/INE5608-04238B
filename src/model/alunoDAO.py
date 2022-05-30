from .DAO import DAO
from .entity import Aluno

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('lista_alunos.pkl')

    def adicionar_aluno(self, aluno: Aluno):
        super().adicionar(aluno.cpf, aluno)

    def capturar_aluno(self, aluno: Aluno):
        return super().capturar(aluno.cpf)

    def remover_aluno(self, aluno: Aluno):
        return super().remover(aluno.cpf)
