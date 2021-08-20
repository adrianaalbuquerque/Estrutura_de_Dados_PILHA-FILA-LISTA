class PilhaEncadeada:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def mostrar_elemento(self):
        if self.vazio():
            raise PilhaException('A pilha está vazia')

        return self.__topo

    def vazio(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

    def adicionar(self, surfista):
        surfista.prox = self.__topo
        self.__topo = surfista

        self.__tamanho += 1

    def remover(self):
        if self.vazio():
            raise PilhaException('A pilha está vazia, não há o que remover.')

        self.__topo = self.__topo.prox
        self.__tamanho -= 1

    def __str__(self):
        saida = ''
        p = self.__topo

        while p != None:
            saida += f'\n{p.nome}'
            p = p.prox

            if p != None:
                saida += ' '

        saida += ' '
        return saida

    def imprimir(self):
        print(self.__str__())


class PilhaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
