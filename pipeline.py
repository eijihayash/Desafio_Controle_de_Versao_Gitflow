import requests

class Pipeline:

    def __init__(self, url) -> None:
        self.url = url
        self.session = requests.Session()
    
    def extrair_url(self) -> str:
        try:
            #Requisição com timeout.
            response = self.session.get(self.url, timeout=10)

            #Verificando se o status code é 200
            #Se for 400 ou 500 vai direto para o except
            response.raise_for_status()

            #retorna o texto bruto
            return response.text

        except requests.exceptions.HTTPError as errh:
            print(f'Erro HTTP: {errh}')
        except requests.exceptions.ConnectionError as errc:
            print(f'Erro de Conexão: {errc}')
        except requests.exceptions.Timeout as errt:
            print(f'Erro de Timeout: {errt}')
        except requests.exceptions.RequestException as err:
            print(f'Erro inesperado: {err}')

        return ""

