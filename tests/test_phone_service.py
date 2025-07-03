import unittest
from models.pessoa import Pessoa

class TestPessoa(unittest.TestCase):

    def test_celular_formatado_valido(self):
        p = Pessoa("Maria Souza", "maria@email.com", "(81) 98765-4321", "12345678909", "50050-000", "interesse")
        self.assertEqual(p.celular, "81 987654321")
        self.assertNotIn("Celular Invalido", p.get_observacoes())

    def test_celular_invalido(self):
        p = Pessoa("Carlos Silva", "carlos@email.com", "1234", "12345678909", "50050-000", "interesse")
        self.assertIn("Celular Invalido", p.get_observacoes())

if __name__ == "__main__":
    unittest.main()