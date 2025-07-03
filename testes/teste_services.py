import unittest
from unittest.mock import patch
from services.cpf_service import CPFService
from services.gender_service import GenderService

class TestServices(unittest.TestCase):

    def test_cpf_formatar_e_validar(self):
        cpf = "529.982.247-25"
        cpf_formatado = CPFService.formatar_cpf(cpf)
        print(f"CPF formatado: {cpf_formatado}")
        self.assertEqual(cpf_formatado, "52998224725")

        is_valid = CPFService.validar_cpf(cpf)
        print(f"CPF {cpf} é válido? {is_valid}")
        self.assertTrue(is_valid)

        invalido = "11111111111"
        is_invalid = CPFService.validar_cpf(invalido)
        print(f"CPF {invalido} é válido? {is_invalid}")
        self.assertFalse(is_invalid)


    @patch("services.gender_service.requests.get")
    def test_gender_service_mock(self, mock_get):
        # Primeiro teste: resposta com gênero "male"
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"gender": "male"}
        genero = GenderService.inferir_genero("joao")
        print(f"Gênero inferido para 'joao': {genero}")
        self.assertEqual(genero, "male")

        #resposta com gênero "female"
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"gender": "female"}
        genero = GenderService.inferir_genero("maria")
        print(f"Gênero inferido para 'joao': {genero}")
        self.assertEqual(genero, "female")

        # Segundo teste: sem gênero identificado
        mock_get.return_value.json.return_value = {"gender": None}
        genero = GenderService.inferir_genero("xyz")
        print(f"Gênero inferido para 'xyz': {genero}")
        self.assertEqual(genero, "indefinido")

if __name__ == "__main__":
    unittest.main()

#TESTADO E OK