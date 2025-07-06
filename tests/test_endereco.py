import unittest
from models.endereco import Endereco

class TestEndereco(unittest.TestCase):
    """
    Testes unitários para a classe Endereco, responsável por normalizar o CEP
    e buscar informações de endereço a partir da API ViaCEP.
    """

    def test_normalizacao_cep(self) -> None:
        """
        Verifica se o CEP é corretamente normalizado (remove traços e pontuação).
        """
        e = Endereco("51170-560")
        self.assertEqual(e.cep, "51170560")
        print("✅ test_normalizacao_cep passou — CEP normalizado:", e.cep)

    def test_busca_endereco_valido(self) -> None:
        """
        Verifica se o endereço é corretamente preenchido a partir de um CEP válido.
        """
        e = Endereco("90010000")
        self.assertIsNotNone(e.bairro)
        self.assertEqual(e.cidade, "Porto Alegre")
        self.assertEqual(e.estado, "RS")
        print(f"✅ test_busca_endereco_valido passou — {e.bairro}, {e.cidade}-{e.estado}")

    def test_busca_endereco_invalido(self) -> None:
        """
        Verifica se um CEP inválido retorna campos nulos (None).
        """
        e = Endereco("00000000")
        self.assertIsNone(e.bairro)
        self.assertIsNone(e.cidade)
        self.assertIsNone(e.estado)
        print("✅ test_busca_endereco_invalido passou — endereço não encontrado.")
    
    def test_dados_endereco_por_cep(self) -> None:
        """
        Teste informativo para exibir os dados retornados por um CEP real.
        Não contém assertivas, apenas demonstração.
        """
        e = Endereco("51170-560") # CEP de Recife/PE
        print(f"✅ test_dados_endereco_por_cep passou — {e.bairro}, {e.cidade}-{e.estado}")
        print(e.cep)       
        print(e.bairro)    
        print(e.cidade)    
        print(e.estado)    
        print(e.get_ddd())

if __name__ == "__main__":
    unittest.main()

# TESTADO E APROVADO