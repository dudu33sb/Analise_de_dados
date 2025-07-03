import unittest
from models.cpf import CPF

class TestCPFValidator(unittest.TestCase):
    def test_cpf_valido(self):
        self.assertTrue(CPF.validar_cpf("529.982.247-25"))
        print("✅ test_cpf_valido passou.")

    def test_cpf_invalido_digito_errado(self):
        self.assertFalse(CPF.validar_cpf("529.982.247-24"))
        print("✅ test_cpf_invalido_digito_errado passou.")

    def test_cpf_com_todos_digitos_iguais(self):
        self.assertFalse(CPF.validar_cpf("111.111.111-11"))
        print("✅ test_cpf_com_todos_digitos_iguais passou.")

        # Menos de 11 dígitos
    def test_cpf_com_tamanho_invalido(self):
        with self.assertRaises(ValueError) as context:
            CPF.validar_cpf("123.456.789")
            # Agora podemos usar o contexto para fazer asserções e prints
            print("Erro capturado:", context.exception)
            self.assertEqual(str(context.exception), "CPF inválido: deve conter exatamente 11 dígitos.")


    def test_cpf_somente_numeros_valido(self):
        self.assertTrue(CPF.validar_cpf("52998224725"))  # Sem pontuação
        print("✅ test_cpf_somente_numeros_valido passou.")

    def test_cpf_somente_numeros_invalido(self):
        self.assertFalse(CPF.validar_cpf("52998224726"))  # Dígito errado
        print("✅ test_cpf_somente_numeros_invalido passou.")

if __name__ == '__main__':
    unittest.main()

#TESTADO TUDO OK