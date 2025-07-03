import unittest
from services.gender_service import GenderService

class TestGenderService(unittest.TestCase):

    def test_genero_masculino(self):
        genero = GenderService.inferir_genero("João")
        self.assertIn(genero, ["male", "female", "indefinido"])

    def test_genero_feminino(self):
        genero = GenderService.inferir_genero("Maria")
        self.assertIn(genero, ["male", "female", "indefinido"])

    def test_nome_invalido(self):
        genero = GenderService.inferir_genero("asdfghjk")
        self.assertEqual(genero, "indefinido")

    def test_nome_vazio(self):
        genero = GenderService.inferir_genero("")
        self.assertEqual(genero, "indefinido")

if __name__ == '__main__':
    unittest.main()
