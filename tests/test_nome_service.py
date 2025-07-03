import unittest
from models.pessoa import Pessoa

class TestPessoa(unittest.TestCase):

    def test_nome_normalizado(self):
        p = Pessoa("JOÃO DA SILVA", "email@test.com", "81987654321", "123.456.789-09", "50050-000", "interesse")
        self.assertEqual(p._Pessoa__nome_completo, "João da Silva")  # acesso direto à var privada para teste
        self.assertEqual(p._Pessoa__primeiro_nome, "João")
        self.assertEqual(p._Pessoa__segundo_nome, "da Silva")
        print("Nome normalizado:", repr(p._Pessoa__nome_completo))



if __name__ == "__main__":
    unittest.main()

# TESTADO TUDO OK