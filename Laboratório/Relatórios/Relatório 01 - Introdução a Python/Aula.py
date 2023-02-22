# Criando a classe aula

class Aula:
    def __init__(self, professor, assunto, alunos=None):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    def listar_presenca(self):
        answer = f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:'
        for aluno in self.alunos:
            answer += f'\n{aluno.presenca()}'
        return answer