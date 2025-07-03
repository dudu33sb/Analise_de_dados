import requests

class GenderService:
    # Substitua pela sua chave ou deixe vazio se quiser usar o modo gratuito
    API_KEY = ""  # Ex: "4052cb2ea666970dacde2fb25785f415"

    @staticmethod
    def inferir_genero(nome: str) -> str:
        try:
            primeiro_nome = nome.strip().split()[0].lower()

            if GenderService.API_KEY:
                url = f"https://api.genderize.io/?name={primeiro_nome}&apikey={GenderService.API_KEY}"
            else:
                url = f"https://api.genderize.io/?name={primeiro_nome}"

            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                dados = response.json()
                genero = dados.get("gender")
                return genero if genero else "indefinido"
            else:
                print(f"[ERRO] Status {response.status_code} ao acessar Genderize API")
                print(f"Detalhes: {response.text}")
        except Exception as e:
            print(f"[ERRO] Falha ao inferir gênero: {e}")

        return "indefinido"
