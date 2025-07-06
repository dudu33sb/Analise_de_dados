import unittest
from models.cpf import CPF

class TestCPFValidator(unittest.TestCase):
    """
    Testes unitários para a classe CPF que valida números de CPF (Cadastro de Pessoa Física).
    """
    
    def test_cpf_valido(self) -> None:
        self.assertTrue(CPF.validar_cpf("529.982.247-25"))
        print("✅ test_cpf_valido passou.")

    def test_cpf_invalido_digito_errado(self) -> None:
        self.assertFalse(CPF.validar_cpf("529.982.247-24"))
        print("✅ test_cpf_invalido_digito_errado passou.")

    def test_cpf_com_todos_digitos_iguais(self) -> None:
        self.assertFalse(CPF.validar_cpf("111.111.111-11"))
        print("✅ test_cpf_com_todos_digitos_iguais passou.")

    def test_cpf_com_tamanho_invalido(self) -> None:
        """
        Testa um CPF com quantidade de dígitos menor que 11.
        Espera-se que levante um ValueError.
        """
        with self.assertRaises(ValueError) as context:
            CPF.validar_cpf("123.456.789")

        # Verifica se a mensagem de erro está correta
        self.assertEqual(str(context.exception), "CPF inválido: deve conter exatamente 11 dígitos.")
        print("Erro capturado:", context.exception)
            
    def test_cpf_somente_numeros_valido(self) -> None:
        self.assertTrue(CPF.validar_cpf("52998224725"))  # Sem pontuação
        print("✅ test_cpf_somente_numeros_valido passou.")

    def test_cpf_somente_numeros_invalido(self) -> None:
        self.assertFalse(CPF.validar_cpf("52998224726"))  # Dígito errado
        print("✅ test_cpf_somente_numeros_invalido passou.")

    def test_cpf_com_caracteres_invalidos(self) -> None:
        """
        Testa um CPF com letras e símbolos misturados.
        Deve levantar ValueError se o resultado tiver menos de 11 dígitos após limpeza.
        """
        with self.assertRaises(ValueError) as context:
            CPF.validar_cpf("abc.529@982#247$25")

        self.assertEqual(str(context.exception), "CPF inválido: deve conter exatamente 11 dígitos.")
        print("✅ test_cpf_com_caracteres_invalidos passou.")

    def test_cpf_com_mais_de_11_digitos(self) -> None:
        """
        Testa um CPF com mais de 11 dígitos numéricos após limpeza.
        Deve levantar ValueError.
        """
        with self.assertRaises(ValueError) as context:
            CPF.validar_cpf("529982247251234")

        self.assertEqual(str(context.exception), "CPF inválido: deve conter exatamente 11 dígitos.")
        print("✅ test_cpf_com_mais_de_11_digitos passou.")

if __name__ == '__main__':
    unittest.main()

#TESTADO TUDO OK