import re
import requests

class Endereco:
    def __init__(self, cep: str):
        self.cep = self.__normalizar_cep(cep)
        self.bairro, self.cidade, self.estado = self.__get_info_por_cep()
    
    def __normalizar_cep(self, cep: str) -> str:
        """Remove pontos, traços e espaços do CEP"""
        return re.sub(r'\D', '', cep)
    
    def get_ddd(self) -> str:
        """Retorna o DDD com base no estado"""
        mapa_ddd = {
            "SP": "11", "RJ": "21", "MG": "31", "PE": "81",
            "BA": "71", "RS": "51", "PR": "41", "SC": "48",
            "DF": "61", "GO": "62", "CE": "85", "PA": "91"
        }
        return mapa_ddd.get(self.estado, "00")

    def __get_info_por_cep(self):
        """Consulta a API ViaCEP e retorna (bairro, cidade, estado)"""
        try:
            url = f"https://viacep.com.br/ws/{self.cep}/json/"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                dados = response.json()
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
