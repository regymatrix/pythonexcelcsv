# estrategias.py
from IRegrasStrategy import RegraStrategy

class RegraAtacado(RegraStrategy):
    def aplicar(self, dados):
        return [d for d in dados if d["tipo"] == "atacado"]

class RegraAgro(RegraStrategy):
    def aplicar(self, dados):
        return [d for d in dados if d["tipo"] == "agro"]

class RegraVarejo(RegraStrategy):
    def aplicar(self, dados):
        return [d for d in dados if d["tipo"] == "varejo"]
