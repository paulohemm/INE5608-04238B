from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nivel_do_aluno):
        super().__init__()
        self._nivel_do_aluno = nivel_do_aluno
        self._tipo_de_conta = 'Aluno'

    @property
    def nivel_do_aluno(self):
        return self._nivel_do_aluno

    @nivel_do_aluno.setter
    def nivel(self, nivel_do_aluno):
        self._nivel_do_aluno = nivel_do_aluno
