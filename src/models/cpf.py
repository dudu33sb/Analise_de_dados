import re

class CPF():
    """
    Classe para validação de números de CPF.
    """
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """
        Valida um número de CPF.

        Um CPF válido possui 11 dígitos numéricos, podendo ser formatado com pontos e traços.
        A validação é feita com base no cálculo dos dois dígitos verificadores.

        Args:
            cpf (str): O CPF a ser validado. Pode conter caracteres não numéricos (ex: pontos, traços).

        Returns:
            bool: True se o CPF for válido, False caso contrário.

        Raises:
            ValueError: Se o CPF não contiver exatamente 11 dígitos numéricos após a limpeza.
        """

        # Remove tudo que não for dígito do CPF
        cpf_tratado = re.sub(r'\D', '', cpf) 

        # Verifica se o CPF possui exatamente 11 dígitos
        if len(cpf_tratado) != 11:
            raise ValueError("CPF inválido: deve conter exatamente 11 dígitos.")


        # Verifica se todos os dígitos são iguais (CPFs assim são inválidos)
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
            
        # Verifica se os dígitos calculados correspondem aos dígitos informados no CPF
        if int(cpf_tratado[9]) == primeiro_digito and int(cpf_tratado[10]) == segundo_digito:
            return True

        return False
