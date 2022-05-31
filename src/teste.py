from model import *

aluno = Aluno('001', '123456', 30 , 85)

database = AlunoDAO()
database.adicionar_aluno(aluno)
database.remover_aluno('001')
database.listar()