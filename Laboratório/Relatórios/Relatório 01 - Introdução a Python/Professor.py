# Criando a classe professor

class Professor:
    def __init__(self, nome):
        self.nome = nome
    def ministrar_aula(self, assunto):
        return f'O professor {self.nome} está ministrando uma aula sobre {assunto}.'