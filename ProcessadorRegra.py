class ProcessadorDeRegra:
    def __init__(self, strategy):
        self.strategy = strategy

    def executar(self, dados):
        return self.strategy.aplicar(dados)
