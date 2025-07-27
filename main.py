
from RegrasStrategy import RegraAtacado, RegraAgro, RegraVarejo
from ProcessadorRegra import ProcessadorDeRegra
from CarregarDados import ImportarDados
import pandas as pd


caminho_arquivo = "overrideorigem.xlsx"
dadosIniciais = ImportarDados(caminho_arquivo)
dados = dadosIniciais.ler_dados()


dados_atacado = [d for d in dados if d["carteira"].lower() == "atacado"]

processador = ProcessadorDeRegra(RegraAtacado())
resultado = processador.executar(dados_atacado)
dfatacado = pd.DataFrame(resultado)
# print(dfatacado)


dados_varejo = [d for d in dados if d["carteira"].lower() == "varejo"]
dfvarejo = pd.DataFrame(dados_varejo[:5])
# print(dfvarejo)

dados_agro = [d for d in dados if d["carteira"].lower() == "agro"]
dfagro = pd.DataFrame(dados_agro[:5])
# print(dfagro)


df_final = pd.concat([dfatacado, dfvarejo, dfagro], ignore_index=True)
print(df_final)
# dados = [
#     {"nome": "Cliente A", "tipo": "atacado"},
#     {"nome": "Cliente B", "tipo": "agro"},
#     {"nome": "Cliente C", "tipo": "varejo"},
# ]

# processador = ProcessadorDeRegra(RegraAgro())
# resultado = processador.executar(dados)
# print(resultado)