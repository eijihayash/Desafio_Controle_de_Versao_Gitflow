import requests
import pandas as pd
from io import StringIO

class Pipeline:

    def __init__(self, url: str) -> None:
        self.url = url
        self.session = requests.Session()
        self.raw_data = None
        self.dados_tabular = None

    def extrair_url(self) -> bool:
        try:
            #Requisição com timeout.
            response = self.session.get(self.url, timeout=10)

            #Verificando se o status code é 200
            #Se for 400 ou 500 vai direto para o except
            response.raise_for_status()

            #retorna o texto bruto
            self.raw_data = response.text
            print("Extração bem-sucedida e salva em self.raw_data.")

            return True

        except requests.exceptions.HTTPError as errh:
            print(f'Erro HTTP: {errh}')
        except requests.exceptions.ConnectionError as errc:
            print(f'Erro de Conexão: {errc}')
        except requests.exceptions.Timeout as errt:
            print(f'Erro de Timeout: {errt}')
        except requests.exceptions.RequestException as err:
            print(f'Erro inesperado: {err}')

        return False

    def transformar_dados(self) -> bool:
        
        if self.raw_data is None:
            print("Erro: Não há dados para transformar. Execute extrair_url primeiro.")
            return False
        
        try:
            df = pd.read_csv(StringIO(self.raw_data))
            
            # Exemplo de transformação: Remover duplicatas e valores nulos
            df_limpo = df.drop_duplicates().dropna(how='all')
            
            print(f"Transformação concluída: {len(df_limpo)} linhas processadas.")
            print("Salva em self.dados_tabular.")
            self.dados_tabular = df_limpo
            return True
        
        except Exception as e:
            print(f"Erro ao processar DataFrame: {e}")
            return False
    
    def obter_estatisticas(self) -> dict:
        if self.dados_tabular is None:
            print("Erro: Dados não processado")
            return False
        
        resumo = {
            "total_linhas": len(self.dados_tabular),
            "colunas": list(self.dados_tabular.columns),
            "memorica_usada": f"{self.dados_tabular.memory_usage(deep=True).sum() / 1024:.2f} KB"
        }
        print(f"Resumo do Pipeline: {resumo['total_linhas']} registros processados.")
        return resumo
    
    def salvar_csv(self, nome_arquivo: str) -> bool:
        if self.dados_tabular is None:
            print("Aviso: DataFrame vazio. Nada será salvo.")
            return False
        
        nome_arquivo += '.csv'

        try:
            self.dados_tabular.to_csv(nome_arquivo, encoding='utf-8', index=False)
            print(f"Arquivo salvo com sucesso: {nome_arquivo}")
            return True
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")
            return False