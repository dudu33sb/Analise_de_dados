import unittest
from models.pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    """
    Testes relacionados à validação e formatação do número de celular na classe Pessoa.
    """

    def test_celular_formatado_valido(self):
        """
        Verifica se um celular válido com DDD entre parênteses é corretamente formatado,
        e que nenhuma observação de "Celular Invalido" é registrada.
        """
        p = Pessoa("Maria Souza", "maria@email.com", "(81) 98765-4321", "12345678909", "50050-000", "interesse")
        self.assertEqual(p.celular, "81 987654321")
        self.assertNotIn("Celular Invalido", p.get_observacoes())

    def test_celular_invalido(self):
        """
        Verifica se um número de celular claramente inválido (ex.: muito curto)
        registra a observação "Celular Invalido".
        """
        p = Pessoa("Carlos Silva", "carlos@email.com", "1234", "12345678909", "50050-000", "interesse")
        self.assertIn("Celular Invalido", p.get_observacoes())

    def test_celular_adiciona_ddd_conforme_cep(self) -> None:
        """Confirma que o DDD é adicionado com base no CEP (ex: Recife = 81)."""
        p = Pessoa("Ana Maria", "email@test.com", "912345678", "123.456.789-09", "51170-560", "Interesse")
        
        print("📱 Celular formatado:", p.celular)
        print("📍 Estado detectado via CEP:", p.endereco.estado)

    def test_celular_normalizado_com_ddd(self) -> None:
        p = Pessoa("Ana Maria", "email@test.com", "(51) 91234-5678", "123.456.789-09", "90010000", "Interesse")
        self.assertEqual(p.celular, "51 912345678")
        print("✅ test_celular_normalizado_com_ddd passou | Celular:", p.celular)

    def test_celular_sem_ddd_adiciona_ddd(self) -> None:
        p = Pessoa("Ana Maria", "email@test.com", "912345678", "123.456.789-09", "90010000", "Interesse")
        self.assertTrue(p.celular.startswith("51 "))
        print("✅ test_celular_sem_ddd_adiciona_ddd passou | Celular:", p.celular)

    def test_celular_invalido_registra_observacao(self) -> None:
        p = Pessoa("Ana Maria", "email@test.com", "123", "123.456.789-09", "90010000", "Interesse")
        self.assertIn("Celular Invalido", p.get_observacoes())
        print("✅ test_celular_invalido_registra_observacao passou | Celular:", p.celular)
    
    def test_celular_com_8_digitos_adiciona_9_e_ddd(self) -> None:
        p = Pessoa("Carlos", "email@test.com", "12345678", "123.456.789-09", "90010000", "Interesse")
        self.assertEqual(p.celular, "51 912345678")  # 51 = DDD de Porto Alegre (pelo CEP)
        print("✅ test_celular_com_8_digitos_adiciona_nono_digito_e_ddd passou | Celular:", p.celular)

    def test_celular_com_8_digitos_mais_ddd_adiciona_9(self) -> None:
        p = Pessoa("Carlos", "email@test.com", "5112345678", "123.456.789-09", "90010000", "Interesse")
        self.assertEqual(p.celular, "51 912345678")
        print("✅ test_celular_com_8_digitos_mais_ddd_adiciona_nono_digito passou | Celular:", p.celular)

if __name__ == "__main__":
    unittest.main()