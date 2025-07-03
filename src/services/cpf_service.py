import re
from models.cpf import CPF

class CPFService:
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        return CPF.validar_cpf(CPFService.formatar_cpf(cpf))

    @staticmethod
    def formatar_cpf(cpf: str) -> str:
        return re.sub(r'\D', '', cpf)
