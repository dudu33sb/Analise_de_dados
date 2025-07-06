import re
import requests

class Endereco:

    """
    Classe que representa um endereço baseado em um CEP brasileiro.

    Ao ser instanciada com um CEP, consulta a API ViaCEP para obter
    o bairro, cidade e estado correspondentes.
    """

    def __init__(self, cep: str):
        """
        Inicializa a instância do endereço com base em um CEP.

        Args:
            cep (str): O CEP (pode conter pontos, traços ou espaços).
        """
        self.cep: str = self.__normalizar_cep(cep)
        self.bairro, self.cidade, self.estado = self.__get_info_por_cep()
    
    def __normalizar_cep(self, cep: str) -> str:
        """
        Remove todos os caracteres não numéricos do CEP.

        Args:
            cep (str): CEP original com ou sem formatação.

        Returns:
            str: CEP contendo apenas dígitos.
        """
        return re.sub(r'\D', '', cep)
    
    def get_ddd(self) -> str:
        """
        Retorna o DDD com base na sigla do estado (UF).

        Returns:
            str: DDD correspondente ao estado, ou "00" se não encontrado.
        """
        mapa_ddd = {
            "SP": "11", "RJ": "21", "MG": "31", "PE": "81",
            "BA": "71", "RS": "51", "PR": "41", "SC": "48",
            "DF": "61", "GO": "62", "CE": "85", "PA": "91"
        }
        return mapa_ddd.get(self.estado, "00")

    def __get_info_por_cep(self) -> str:
        """
        Consulta a API ViaCEP para obter dados do endereço.

        Returns:
            str: bairro, cidade, estado
        """
        try:
            url = f"https://viacep.com.br/ws/{self.cep}/json/"
            response = requests.get(url, timeout=5)

            # Verifica se a requisição foi bem-sucedida
            if response.status_code == 200:
                dados = response.json()

                # Verifica se a resposta contém erro (CEP inválido)
                if dados.get("erro"):
                    return None, None, None

                return (
                    dados.get("bairro"),
                    dados.get("localidade"),
                    dados.get("uf")
                )
        except requests.RequestException as e:
            print(f"Erro na consulta do CEP: {e}")
        return None, None, None
