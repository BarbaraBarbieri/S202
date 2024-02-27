# Criando a classe professor

class Professor:
    def __init__(self, nome):
        self.nome = nome
    def ministrar_aula(self, assunto):
        return f'O professor {self.nome} está ministrando uma aula sobre {assunto}.'

# Criando a classe aluno

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def presenca(self):
        return f'O aluno {self.nome} está presente.'

# Criando a classe aula

class Aula:
    def __init__(self, professor, assunto, alunos = []):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    def listar_presenca(self):
        answer = f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:'
        for aluno in self.alunos:
            answer += f'\n{aluno.presenca()}'
        return answer

# Instanciando os objetos

professor = Professor("Lucas")
maria = Aluno("Maria")
pedro = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")

# Chamando os métodos

aula.adicionar_aluno(maria)
aula.adicionar_aluno(pedro)
print(aula.listar_presenca())
