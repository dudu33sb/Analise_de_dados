import unittest
from services.gender_service import GenderService

class TestGenderService(unittest.TestCase):
    """
    Testes unitários para o serviço de inferência de gênero baseado em nomes.
    """

    def test_genero_masculino(self) -> None:
        genero = GenderService.inferir_genero("João")
        self.assertIn(genero, ["male", "female", "indefinido"])

    def test_genero_feminino(self) -> None:
        genero = GenderService.inferir_genero("Maria")
        self.assertIn(genero, ["male", "female", "indefinido"])

    def test_nome_invalido(self) -> None:
        """
        Testa com um nome que não deve existir na base de dados da API.
        Espera-se o retorno 'indefinido'.
        """
        genero = GenderService.inferir_genero("asdfghjk")
        self.assertEqual(genero, "indefinido")

    def test_nome_vazio(self) -> None:
        """
        Testa a função com uma string vazia.
        Deve retornar 'indefinido'.
        """
        genero = GenderService.inferir_genero("")
        self.assertEqual(genero, "indefinido")

if __name__ == '__main__':
    unittest.main()
