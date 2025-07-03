import re

class CPF():
    @staticmethod
    def validar_cpf(cpf):
        cpf_tratado = re.sub(r'\D', '', cpf) # Remove tudo que não for dígito

        if len(cpf_tratado) != 11:
            raise ValueError("CPF inválido: deve conter exatamente 11 dígitos.") #verifica se o cps é valido


        # Verifica se todos os dígitos são iguais
        if cpf_tratado == cpf_tratado[0] * 11:
            return False

        # Cálculo do primeiro dígito verificador
        soma = sum(int(cpf_tratado[i]) * (10 - i) for i in range(9))
        primeiro_digito = (soma * 10) % 11
        if primeiro_digito == 10:
            primeiro_digito = 0

        # Cálculo do segundo dígito verificador
        soma = sum(int(cpf_tratado[i]) * (11 - i) for i in range(9))
        soma += primeiro_digito * 2
        segundo_digito = (soma * 10) % 11
        if segundo_digito == 10:
            segundo_digito = 0
            
        # Verificação
        if int(cpf_tratado[9]) == primeiro_digito and int(cpf_tratado[10]) == segundo_digito:
            return True

        return False
