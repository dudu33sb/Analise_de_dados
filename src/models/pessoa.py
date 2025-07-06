import re
import requests
from .cpf import CPF
from models.endereco import Endereco
from services.cpf_service import CPFService
from services.gender_service import GenderService

class Pessoa():
    """
    Representa uma pessoa com dados pessoais, endereço, CPF, celular e gênero.
    Realiza normalização e validação de dados como CPF e número de celular.
    """

    __LISTA_PREPOSICOES = ["da", "de", "do", "das", "dos", "e"]
    __MSG_CELULAR_INVALIDO = "Celular Invalido"

    def __init__(self, nome_completo: str, email: str, celular: str, cpf: str, cep: str, interesse: str):
        """
        Inicializa a classe Pessoa, realizando normalização de nome, 
        validação de CPF, celular e consulta de endereço por CEP.

        Args:
            nome_completo (str): Nome completo da pessoa.
            email (str): E-mail da pessoa.
            celular (str): Número de celular da pessoa.
            cpf (str): CPF da pessoa.
            cep (str): CEP para consulta de endereço.
            interesse (str): Área ou tipo de interesse da pessoa.
        """

        self.__obs = []
        self.__interesse = interesse
        self.__email = email

        # Nome Completo
        self.__nome_completo = self.__convert_to_camel_case(nome_completo)
        splitted_name = self.__nome_completo.split(" ")
        self.__primeiro_nome = splitted_name[0]
        print(f"[DEBUG] Nome completo: {self.__nome_completo}")
        print(f"[DEBUG] Primeiro nome extraído: {self.__primeiro_nome}")    

        # Segundo Nome (verifica preposições como "de", "da", etc.)
        if len(splitted_name) > 1:
            self.__segundo_nome = splitted_name[1]
            if self.__segundo_nome.lower() in self.__LISTA_PREPOSICOES and len(splitted_name) > 2:
                self.__segundo_nome = f"{self.__segundo_nome} {splitted_name[2]}"
        else:
            self.__segundo_nome = ""
        
        # Gênero - Verificar após definir primeiro nome
        self.__genero = GenderService.inferir_genero(self.__primeiro_nome)

        # Endereço
        self.endereco = Endereco(cep)
        if not self.endereco.bairro or not self.endereco.cidade or not self.endereco.estado:
            self.__obs.append("CEP inválido")

        # Celular: Validar e registra observação se for inválido
        self.celular = self.__normalize_cellphone(celular, cep)
        if self.celular == "":
            self.__obs.append("Celular Vazio")
        elif self.celular and not re.match(r'^\d{2} 9\d{8}$', self.celular):
            self.__obs.append("Celular Invalido")

        # CPF: Validar e registra observação se for inválido
        cpf_formatado = CPFService.formatar_cpf(cpf)
        self.cpf = cpf_formatado
        if not CPFService.validar_cpf(self.cpf):
            self.__obs.append("CPF inválido")
    
    
    def __convert_to_camel_case(self, value: str) -> str:
        """
        Converte uma string de nome para Camel Case,
        respeitando preposições comuns em nomes.

        Args:
            value (str): Nome completo original.

        Returns:
            str: Nome em Camel Case com preposições minúsculas.
        """
        final_name = ""
        value_ = value.lower()
        names = value_.split(" ")
        for name in names:
            if name in self.__LISTA_PREPOSICOES:
                final_name = f"{final_name}{name} "
            else:
                name = f"{name[0]}".upper() + name[1:]
                final_name = f"{final_name}{name} "
        return final_name.strip()


    def __normalize_cellphone(self, value: str, cep: str) -> str:
        """
        Normaliza o número de celular para o formato 'DDD 9XXXXXXXX'.
        Adiciona DDD com base no CEP se necessário.

        Args:
            value (str): Número de celular original.
            cep (str): CEP para determinar o DDD (se aplicável).

        Returns:
            str: Número normalizado ou None se inválido.
        """

        # Revome tudo que não for dígito do número de celular
        celular = re.sub(r'\D', '', value) 

        # Se o celular foi preenchido
        if len(celular) == 0:
            self.__obs.append("Celular Vazio")
            return ""

        # Se tem DDD + 9 dígitos (11 dígitos)
        if re.match(r'^\d{11}$', celular):
            if celular[2] != "9":
                celular = celular[:2] + "9" + celular[2:]
            numero = celular[2:]
            return f"{celular[:2]} {numero}"

        # Se tem só 8 ou 9 dígitos → precisa adicionar DDD ou DDD + 9
        if len(celular) == 8 or len(celular) == 9:
            ddd = self.endereco.get_ddd()
            if len(celular) == 8:
                celular = "9" + celular
            return f"{ddd} {celular}"

        # Se tem DDD + 8 dígitos → adicionar o 9
        if len(celular) == 10:
            ddd = celular[:2]
            numero = celular[2:]
            if numero[0] != "9":
                numero = "9" + numero
            return f"{ddd} {numero}"

        # Número inválido
        self.__obs.append("Celular Invalido")
        return None

    # ---------- PROPERTIES DE FÁCIL ACESSO ----------
    @property
    def nome_completo(self) -> str:
        return self.__nome_completo.strip()

    @property
    def primeiro_nome(self) -> str:
        return self.__primeiro_nome.strip()

    @property
    def segundo_nome(self) -> str:
        return self.__segundo_nome.strip()

    @property
    def genero(self) -> str:
        return self.__genero

    @genero.setter
    def genero(self, value: str):
        self.__genero = value

    @property
    def email(self) -> str:
        return self.__email.strip()

    @property
    def celular(self) -> str:
        return self.__celular

    @celular.setter
    def celular(self, value: str):
        self.__celular = value

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, value: str):
        self.__cpf = value

    @property
    def interesse(self) -> str:
        return self.__interesse.strip()

    def get_observacoes(self) -> str:
        """Retorna a lista de observações registradas para a pessoa."""
        return self.__obs
