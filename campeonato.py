from lista import ListaEncadeada
from fila import FilaEncadeada
from pilha import PilhaEncadeada


class Campeonato:
    def __init__(self, nome_do_campeonato):
        self._nome_do_campeonato = nome_do_campeonato
        self._surfistasL = ListaEncadeada()
        self._surfistasF = FilaEncadeada()
        self._surfistasP = PilhaEncadeada()

    @property
    def nome_do_campeonato(self):
        return self._nome_do_campeonato

    @nome_do_campeonato.setter
    def nome_do_campeonato(self, nome):
        self._nome_do_campeonato = nome

    @property
    def surfistasL(self):
        return self._surfistasL

    @property
    def surfistasP(self):
        return self._surfistasP

    @property
    def surfistasF(self):
        return self._surfistasF

    def menor_idade(self):
        if self.surfistasL.vazio():
            raise CampeonatoException('Campeonato ainda não tem surfistas')

        surfista_mais_novo = self.surfistasL.inicio()
        aux = self.surfistasL.inicio()

        while aux != None:
            if aux.idade < surfista_mais_novo.idade:
                surfista_mais_novo = aux
            aux = aux.prox

        return surfista_mais_novo.nome

    def maior_idade(self):
        if self.surfistasL.vazio():
            raise CampeonatoException('Campeonato ainda não tem surfistas')

        surfista_mais_velho = self.surfistasL.inicio()
        aux = self.surfistasL.inicio()

        while aux != None:
            if aux.idade > surfista_mais_velho.idade:
                surfista_mais_velho = aux
            aux = aux.prox

        return surfista_mais_velho.nome

    def incrementa_titulo_surfista(self, cpf):
        surfista = self.surfistasL.buscar_por_cpf(cpf)
        surfista.incrementa_titulo()

    def adicionar_surfista_P(self, novo_surfista):
        self._surfistasP.adicionar(novo_surfista)

    def adicionar_surfista_F(self, novo_surfista):
        self._surfistasF.adicionar(novo_surfista)

    def adicionar_surfista_L(self, novo_surfista, posicao):
        self._surfistasL.adicionar(novo_surfista, posicao)

    def remover_surfista_P(self):
        self._surfistasP.remover()

    def remover_surfista_F(self):
        self._surfistasF.remover()

    def remover_surfista_L(self, posicao):
        self._surfistasL.remover(posicao)

    def busca_surfista(self, cpf):
        return self.surfistasL.buscar_por_cpf(cpf)

    def ordena_surfistas(self):
        self.surfistasL.ordenar()

    def imprimir_surfistas(self):
        if self.surfistasL.vazio():
            raise CampeonatoException('A lista de participantes do Campeonato está vazia.')
        aux = self.surfistasL.inicio()
        while aux != None:
            print(aux)
            aux = aux.prox

    def mostrar_tam_surfistasL(self):
        return self.surfistasL.tamanho()

    def mostrar_tam_surfistasP(self):
        return self.surfistasP.tamanho()

    def mostrar_tam_surfistasF(self):
        return self.surfistasF.tamanho()

    def __str__(self):
        return f"{self._nome_do_campeonato}"


class CampeonatoException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
