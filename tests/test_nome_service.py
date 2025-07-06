import unittest
from models.pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    """
    Testes unitários para a classe Pessoa — foco na normalização de nome completo.
    """

    def test_nome_normalizado(self):
        """
        Verifica se o nome completo é corretamente convertido para camel case
        e se os primeiros nomes são corretamente extraídos.
        """
        pessoa = Pessoa(
                    nome_completo="JOÃO DA SILVA",
                    email="email@test.com",
                    celular="81987654321",
                    cpf="123.456.789-09",
                    cep="50050-000",
                    interesse="interesse"
                )
        
        # Testa nome completo formatado corretamente
        self.assertEqual(p._Pessoa__nome_completo, "João da Silva")

        # Testa extração correta do primeiro nome
        self.assertEqual(p._Pessoa__primeiro_nome, "João")

        # Testa se o segundo nome inclui preposição + sobrenome
        self.assertEqual(p._Pessoa__segundo_nome, "da Silva")

        print("✅ test_nome_normalizado passou — Nome:", repr(p._Pessoa__nome_completo))

    def test_nome_normalizacao_e_preposicoes(self) -> None:
        """Verifica se o nome é formatado em CamelCase com preposições preservadas."""
        p = Pessoa("joão da silva e souza", "email@test.com", "51912345678", "123.456.789-09", "90010000", "Interesse")
        self.assertEqual(p.nome_completo, "João da Silva e Souza")
        self.assertEqual(p.primeiro_nome, "João")
        self.assertEqual(p.segundo_nome, "da Silva")
        print("✅ test_nome_normalizacao_e_preposicoes passou")

    def test_nome_com_um_unico_nome(self) -> None:
        p = Pessoa("João", "email@test.com", "51912345678", "123.456.789-09", "90010000", "Interesse")
        self.assertEqual(p.primeiro_nome, "João")
        self.assertEqual(p.segundo_nome, "")
        print("✅ test_nome_com_um_unico_nome passou")
        

if __name__ == "__main__":
    unittest.main()

# TESTADO TUDO OK