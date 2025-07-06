import re
from models.cpf import CPF

class CPFService:
    """
    Serviço para formatação e validação de CPF.
    Utiliza a lógica da classe CPF para verificar validade após normalização.
    """
    @staticmethod
    def formatar_cpf(cpf: str) -> str:
        """
        Remove todos os caracteres não numéricos do CPF.

        Args:
            cpf (str): CPF com ou sem formatação (ex: '123.456.789-00').

        Returns:
            str: CPF apenas com os dígitos numéricos (ex: '12345678900').
        """
        return re.sub(r'\D', '', cpf)        
        
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """
        Valida um CPF após formatá-lo (remover caracteres não numéricos).

        Args:
            cpf (str): CPF a ser validado.

        Returns:
            bool: True se o CPF for válido, False caso contrário.
        """
        cpf_formatado = CPFService.formatar_cpf(cpf)
        return CPF.validar_cpf(cpf_formatado)

    
