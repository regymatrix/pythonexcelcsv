import pandas as pd
from models import OverrideOrigem


class ImportarDados:
    def __init__(self, caminho: str, guia: str):
        self.caminho = caminho
        self.guia = guia

    def ler_dados(self) -> list:
        planilhas = pd.read_excel(self.caminho, sheet_name=self.guia)

        # se o usuário passou apenas UMA guia (ex: 'atacado')
        if isinstance(planilhas, pd.DataFrame):
            df_geral = planilhas
        else:
            frames = [df for df in planilhas.values()]
            df_geral = pd.concat(frames, ignore_index=True)

        registros = []
        for _, row in df_geral.iterrows():
            registro = OverrideOrigem(
                carteira=row["carteira"],
                valorcontabil=row["valorcontabil"],
                empresa=row["empresa"],
                produto=row["produto"]
            )
            registros.append(registro.to_dict())

        return registros