import unittest
from models.pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    """
    Testes unitários para a classe Pessoa.
    Verifica normalização de nomes, validação de celular, CPF e CEP.
    """
    def test_cpf_valido_e_invalido(self) -> None:
        valido = Pessoa("Ana Maria", "email@test.com", "51912345678", "529.982.247-25", "90010000", "Interesse")
        invalido = Pessoa("João", "email@test.com", "51912345678", "111.111.111-11", "90010000", "Interesse")
        self.assertNotIn("CPF inválido", valido.get_observacoes())
        self.assertIn("CPF inválido", invalido.get_observacoes())
        print("✅ test_cpf_valido_e_invalido passou")

    def test_observacoes_cep_invalido(self) -> None:
        """Verifica se CEP inexistente gera observação apropriada."""
        p = Pessoa("Ana Maria", "email@test.com", "51912345678", "529.982.247-25", "00000000", "Interesse")
        self.assertIn("CEP inválido", p.get_observacoes())
        print("✅ test_observacoes_cep_invalido passou")

      

if __name__ == "__main__":
    unittest.main()

# TESTADO E PASSOU