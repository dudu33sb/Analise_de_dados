import requests

class GenderService:
    """
    Serviço para definir o gênero a partir do primeiro nome usando a API Genderize.io.
    
    A API pode ser usada com ou sem chave (API_KEY).
    """
    # Chave da API Genderize.io (deixe vazia para usar modo gratuito)
    API_KEY: str = ""  # Ex: "4052cb2ea666970dacde2fb25785f415"

    @staticmethod
    def inferir_genero(nome: str) -> str:
        """
        Define o gênero a partir do primeiro nome utilizando a API Genderize.io.

        Args:
            nome (str): Nome completo ou primeiro nome da pessoa.

        Returns:
            str: Retorna 'male', 'female' ou 'indefinido' caso não seja possível identificar.
        """
        try:
            # Extrai o primeiro nome em minúsculo para consulta
            primeiro_nome = nome.strip().split()[0].lower()

            # Monta a URL da API com ou sem chave
            if GenderService.API_KEY:
                url = f"https://api.genderize.io/?name={primeiro_nome}&apikey={GenderService.API_KEY}"
            else:
                url = f"https://api.genderize.io/?name={primeiro_nome}"

            # Requisição GET com timeout de 5 segundos
            response = requests.get(url, timeout=5)

            # Se sucesso, tenta extrair o gênero da resposta JSON
            if response.status_code == 200:
                dados = response.json()
                genero = dados.get("gender")
                return genero if genero else "indefinido"
            else:
                print(f"[ERRO] Status {response.status_code} ao acessar Genderize API")
                print(f"Detalhes: {response.text}")

        except Exception as e:
            print(f"[ERRO] Falha ao inferir gênero: {e}")

        # Retorna 'indefinido' se ocorrer erro ou se a API não retornar gênero
        return "indefinido"
