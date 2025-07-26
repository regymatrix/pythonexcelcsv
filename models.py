from dataclasses import dataclass

@dataclass
class OverrideOrigem:
    carteira: str
    valorcontabil: float
    empresa: str
    produto: str
    overriderating: str = ""
    justificativa: str = ""

    def to_dict(self):
        return {
            "carteira": self.carteira,
            "valorcontabil": self.valorcontabil,
            "empresa": self.empresa,
            "produto": self.produto,
            "overriderating": self.overriderating,
            "justificativa": self.justificativa,
        }
