# estrategias.py
from IRegrasStrategy import RegraStrategy

class RegraAtacado(RegraStrategy):
     def aplicar(self, dados):
        for d in dados:
            d["overriderating"] = "overatacado"
            d["justificativa"] = "justatacado"
        return dados

class RegraAgro(RegraStrategy):
    def aplicar(self, dados):
        for d in dados:
            d["overriderating"] = "overaAGRO"
            d["justificativa"] = "justAGRO"
        return dados

class RegraVarejo(RegraStrategy):
    def aplicar(self, dados):
        for d in dados:
            d["overriderating"] = "overVAREJO"
            d["justificativa"] = "justVAREJO"
        return dados
    




# class RegraAtacado(RegraStrategy):
#     def aplicar(self, dados):
#         return [d for d in dados if d["tipo"] == "atacado"]

# class RegraAgro(RegraStrategy):
#     def aplicar(self, dados):
#         return [d for d in dados if d["tipo"] == "agro"]

# class RegraVarejo(RegraStrategy):
#     def aplicar(self, dados):
#         return [d for d in dados if d["tipo"] == "varejo"]

