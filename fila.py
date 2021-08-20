class FilaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def mostrar_elemento(self):
        if self.vazio():
            raise FilaException('A fila está vazia')

        return self.__inicio

    def vazio(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

    def adicionar(self, surfista):
        aux = self.__inicio

        if aux == None:
            self.__inicio = surfista

        else:
            while aux.prox != None:
                aux = aux.prox

            aux.prox = surfista

        self.__tamanho += 1

    def remover(self):
        if self.vazio():
            raise FilaException('A fila está vazia, não há o que remover.')

        self.__inicio = self.__inicio.prox
        self.__tamanho -= 1

    def __str__(self):
        saida = ' '
        p = self.__inicio

        while p != None:
            saida += f'\n{p.nome}'
            p = p.prox

            if p != None:
                saida += ' '

        saida += ' '
        return saida

    def imprimir(self):
        print(self.__str__())


class FilaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
