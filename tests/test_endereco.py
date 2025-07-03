import unittest
from models.endereco import Endereco

class TestEndereco(unittest.TestCase):
    def test_normalizacao_cep(self):
        e = Endereco("51170-560")
        self.assertEqual(e.cep, "51170560")
        print("✅ test_normalizacao_cep passou — CEP normalizado:", e.cep)

    def test_busca_endereco_valido(self):
        e = Endereco("90010000")
        self.assertIsNotNone(e.bairro)
        self.assertEqual(e.cidade, "Porto Alegre")
        self.assertEqual(e.estado, "RS")
        print(f"✅ test_busca_endereco_valido passou — {e.bairro}, {e.cidade}-{e.estado}")

    def test_busca_endereco_invalido(self):
        e = Endereco("00000000")
        self.assertIsNone(e.bairro)
        self.assertIsNone(e.cidade)
        self.assertIsNone(e.estado)
        print("✅ test_busca_endereco_invalido passou — endereço não encontrado.")
    
    def test_dados_endereco_por_cep(self):
        # Exemplo com CEP real de São Paulo
        e = Endereco("51170-560")  # Avenida Paulista
        print(f"✅ test_dados_endereco_por_cep passou — {e.bairro}, {e.cidade}-{e.estado}")
        print(e.cep)       
        print(e.bairro)    
        print(e.cidade)    
        print(e.estado)    
        print(e.get_ddd())

if __name__ == "__main__":
    unittest.main()

# TESTADO E APROVADO