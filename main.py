
from RegrasStrategy import RegraAtacado, RegraAgro, RegraVarejo
from ProcessadorRegra import ProcessadorDeRegra
from CarregarDados import ImportarDados
import pandas as pd


caminho_arquivo = "overrideorigem.xlsx"
dadosIniciais = ImportarDados(caminho_arquivo)
dados = dadosIniciais.ler_dados()

estrategias = {
    "atacado": RegraAtacado(),
    "agro": RegraAgro(),
    "varejo": RegraVarejo()
}

df_parciais = []

for tipo, estrategia in estrategias.items():
    dados_tipo = [d for d in dados if d["carteira"].lower() == tipo]
    processador = ProcessadorDeRegra(estrategia)
    resultado = processador.executar(dados_tipo)
    df_parciais.append(pd.DataFrame(resultado))

df_final = pd.concat(df_parciais, ignore_index=True)

print(df_final)
df_final.to_csv("resultado.csv", index=False)
print("CSV gerado com sucesso: resultado.csv")

# dados_atacado = [d for d in dados if d["carteira"].lower() == "atacado"]

# processador = ProcessadorDeRegra(RegraAtacado())
# resultado = processador.executar(dados_atacado)
# dfatacado = pd.DataFrame(resultado)
# # print(dfatacado)


# dados_varejo = [d for d in dados if d["carteira"].lower() == "varejo"]
# processadorVarejo = ProcessadorDeRegra(RegraVarejo())
# resultadovarejo = processadorVarejo.executar(dados_varejo)
# dfvarejo = pd.DataFrame(resultadovarejo[:5])
# # print(dfvarejo)

# dados_agro = [d for d in dados if d["carteira"].lower() == "agro"]
# processadorAgro = ProcessadorDeRegra(RegraAgro())
# resultadoagro = processadorAgro.executar(dados_varejo)
# dfagro = pd.DataFrame(resultadoagro[:5])
# # print(dfagro)

# df_final = pd.concat([dfatacado, dfvarejo, dfagro], ignore_index=True)