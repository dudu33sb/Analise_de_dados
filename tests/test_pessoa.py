import unittest
import re
from models.pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def test_nome_normalizacao_e_preposicoes(self):
        p = Pessoa("joão da silva e souza", "email@test.com", "51912345678", "123.456.789-09", "90010000", "Interesse")
        self.assertEqual(p.nome_completo, "João da Silva e Souza")
        self.assertEqual(p.primeiro_nome, "João")
        self.assertEqual(p.segundo_nome, "da Silva")
        print("✅ test_nome_normalizacao_e_preposicoes passou")

    def test_nome_com_um_unico_nome(self):
        p = Pessoa("João", "email@test.com", "51912345678", "123.456.789-09", "90010000", "Interesse")
        self.assertEqual(p.primeiro_nome, "João")
        self.assertEqual(p.segundo_nome, "")
        print("✅ test_nome_com_um_unico_nome passou")

    def test_celular_normalizado_com_ddd(self):
        p = Pessoa("Ana Maria", "email@test.com", "(51) 91234-5678", "123.456.789-09", "90010000", "Interesse")
        self.assertEqual(p.celular, "51 912345678")
        print("✅ test_celular_normalizado_com_ddd passou | Celular:", p.celular)

    def test_celular_sem_ddd_adiciona_ddd(self):
        p = Pessoa("Ana Maria", "email@test.com", "912345678", "123.456.789-09", "90010000", "Interesse")
        self.assertTrue(p.celular.startswith("51 "))
        print("✅ test_celular_sem_ddd_adiciona_ddd passou | Celular:", p.celular)

    def test_celular_invalido_registra_observacao(self):
        p = Pessoa("Ana Maria", "email@test.com", "123", "123.456.789-09", "90010000", "Interesse")
        self.assertIn("Celular Invalido", p.get_observacoes())
        print("✅ test_celular_invalido_registra_observacao passou | Celular:", p.celular)
    
    def test_celular_com_8_digitos_adiciona_nono_digito_e_ddd(self):
        p = Pessoa("Carlos", "email@test.com", "12345678", "123.456.789-09", "90010000", "Interesse")
        self.assertEqual(p.celular, "51 912345678")  # 51 = DDD de Porto Alegre (pelo CEP)
        print("✅ test_celular_com_8_digitos_adiciona_nono_digito_e_ddd passou | Celular:", p.celular)

    def test_celular_com_8_digitos_mais_ddd_adiciona_nono_digito(self):
        p = Pessoa("Carlos", "email@test.com", "5112345678", "123.456.789-09", "90010000", "Interesse")
        self.assertEqual(p.celular, "51 912345678")
        print("✅ test_celular_com_8_digitos_mais_ddd_adiciona_nono_digito passou | Celular:", p.celular)


    def test_cpf_valido_e_invalido(self):
        valido = Pessoa("Ana Maria", "email@test.com", "51912345678", "529.982.247-25", "90010000", "Interesse")
        invalido = Pessoa("João", "email@test.com", "51912345678", "111.111.111-11", "90010000", "Interesse")
        self.assertNotIn("CPF inválido", valido.get_observacoes())
        self.assertIn("CPF inválido", invalido.get_observacoes())
        print("✅ test_cpf_valido_e_invalido passou")

    def test_observacoes_cep_invalido(self):
        p = Pessoa("Ana Maria", "email@test.com", "51912345678", "529.982.247-25", "00000000", "Interesse")
        self.assertIn("CEP inválido", p.get_observacoes())
        print("✅ test_observacoes_cep_invalido passou")

    def test_celular_adiciona_ddd_conforme_cep(self):
        # Exemplo: Porto Alegre - RS (CEP conhecido e válido)
        p = Pessoa("Ana Maria", "email@test.com", "912345678", "123.456.789-09", "51170-560", "Interesse")
        
        print("📱 Celular formatado:", p.celular)
        print("📍 Estado detectado via CEP:", p.endereco.estado)
      

if __name__ == "__main__":
    unittest.main()

# TESTADO E PASSOU