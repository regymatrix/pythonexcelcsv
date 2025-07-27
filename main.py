
from RegrasStrategy import RegraAtacado, RegraAgro, RegraVarejo
from ProcessadorRegra import ProcessadorDeRegra
from CarregarDados import ImportarDados
import pandas as pd


caminho_arquivo = "overrideorigem.xlsx"
dadosIniciais = ImportarDados(caminho_arquivo,'atacado')
dados = dadosIniciais.ler_dados()


df = pd.DataFrame(dados[:5])
print(df)

processador = ProcessadorDeRegra(RegraAtacado())
resultado = processador.executar(dados)
dfresultado = pd.DataFrame(resultado)
print(dfresultado)

# dados = [
#     {"nome": "Cliente A", "tipo": "atacado"},
#     {"nome": "Cliente B", "tipo": "agro"},
#     {"nome": "Cliente C", "tipo": "varejo"},
# ]

# processador = ProcessadorDeRegra(RegraAgro())
# resultado = processador.executar(dados)
# print(resultado)