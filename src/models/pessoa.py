import re
import requests
from .cpf import CPF
from models.endereco import Endereco
from services.cpf_service import CPFService
from services.gender_service import GenderService

class Pessoa():
    __LISTA_PREPOSICOES = ["da", "de", "do", "das", "dos", "e"]
    __MSG_CELULAR_INVALIDO = "Celular Invalido"

    def __init__(self, nome_completo, email, celular, cpf, cep, interesse):
        self.__obs = []
        self.__interesse = interesse
        self.__email = email

        # NOME
        self.__nome_completo = self.__convert_to_camel_case(nome_completo)
        splitted_name = self.__nome_completo.split(" ")
        self.__primeiro_nome = splitted_name[0]
        print(f"[DEBUG] Nome completo: {self.__nome_completo}")
        print(f"[DEBUG] Primeiro nome extraído: {self.__primeiro_nome}")    

        if len(splitted_name) > 1:
            self.__segundo_nome = splitted_name[1]
            if self.__segundo_nome.lower() in self.__LISTA_PREPOSICOES and len(splitted_name) > 2:
                self.__segundo_nome = f"{self.__segundo_nome} {splitted_name[2]}"
        else:
            self.__segundo_nome = ""
        
        # GENERO - inferir após definir primeiro nome
        self.__genero = GenderService.inferir_genero(self.__primeiro_nome)

        # CEP
        self.endereco = Endereco(cep)
        if not self.endereco.bairro or not self.endereco.cidade or not self.endereco.estado:
            self.__obs.append("CEP inválido")

        # Celular: normalizar, validar, e registrar observação se for inválido
        self.celular = self.__normalize_cellphone(celular, cep)
        if self.celular == "":
            self.__obs.append("Celular Vazio")
        elif self.celular and not re.match(r'^\d{2} 9\d{8}$', self.celular):
            self.__obs.append("Celular Invalido")

        # CPF: normalizar, validar, e registrar observação se for inválido
        cpf_formatado = CPFService.formatar_cpf(cpf)
        self.cpf = cpf_formatado

        if not CPFService.validar_cpf(self.cpf):
            self.__obs.append("CPF inválido")

    # Properties para acesso fácil
    @property
    def nome_completo(self):
        return self.__nome_completo.strip()

    @property
    def primeiro_nome(self):
        return self.__primeiro_nome.strip()

    @property
    def segundo_nome(self):
        return self.__segundo_nome.strip()

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, value):
        self.__genero = value

    @property
    def email(self):
        return self.__email.strip()

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, value):
        self.__celular = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def interesse(self):
        return self.__interesse.strip()

    def get_observacoes(self):
        return self.__obs

    # Normaliza o nome para Camel Case respeitando preposições
    def __convert_to_camel_case(self, value: str) -> str:
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


    # Normaliza o celular
    def __normalize_cellphone(self, value: str, cep: str):
        celular = re.sub(r'\D', '', value)

        if len(celular) == 0:
            self.__obs.append("Celular Vazio")
            return ""

        # Se tem DDD + 9 dígitos (11 dígitos)
        if re.match(r'^\d{11}$', celular):
            if celular[2] != "9":
                celular = celular[:2] + "9" + celular[2:]
            numero = celular[2:]
            return f"{celular[:2]} {numero}"

        # Se tem só 8 ou 9 dígitos → precisa adicionar DDD
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
