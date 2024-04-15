class Motorista:
    def __init__(self, nome):
        self.nome = nome
        self.corridas = []

    def adicionar_corrida(self, corrida):
        self.corridas.append(corrida)

    def calcular_nota(self):
        if self.corridas:
            notas_corridas = [corrida.nota for corrida in self.corridas]
            nota_media = sum(notas_corridas) / len(notas_corridas)
            return nota_media
        else:
            return 0