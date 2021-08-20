class Surfista:
    def __init__(self, nome, titulos, idade, cpf):
        self.__nome = nome
        self.__titulos = titulos
        self.__idade = idade
        self.__cpf = cpf
        self.__prox = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def titulos(self):
        return self.__titulos

    @titulos.setter
    def titulos(self, titulos):
        self.__titulos = titulos

    def incrementa_titulo(self):
        self.__titulos += 1

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, proximo):
        self.__prox = proximo

    def __str__(self):
        return f'{self.nome} - {self.titulos}'
