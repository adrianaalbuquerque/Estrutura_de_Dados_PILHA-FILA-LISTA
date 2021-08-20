class ListaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def inicio(self):
        if self.vazio():
            raise ListaException('A lista está vazia')

        return self.__inicio

    def vazio(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

    def adicionar(self, surfista, posicao):
        if posicao < 0 or posicao > self.__tamanho:
            raise ListaException('Posição inválida')

        atual = self.__inicio

        if posicao == 0:
            self.__inicio = surfista
            if atual != None:
                self.__inicio.prox = atual
        else:
            i = 0
            while i != posicao:
                anterior = atual
                atual = atual.prox
                i += 1
            anterior.prox = surfista
            surfista.prox = atual

        self.__tamanho += 1

    def remover(self, posicao):
        if self.vazio():
            raise ListaException('A lista está vazia')

        if posicao < 0 or posicao > self.__tamanho:
            raise ListaException('Posição inválida')

        if posicao == 0:
            if self.__inicio != None:
                self.__inicio = self.__inicio.prox
        else:
            i = 0
            atual = self.__inicio
            while i != posicao:
                anterior = atual
                atual = atual.prox
                i += 1
            anterior.prox = atual.prox

        self.__tamanho -= 1

    def buscar(self, cpf, posicao):
        surfista = self.mostrar_elemento(posicao)
        if surfista.cpf == cpf:
            return surfista
        raise ListaException(f'Surfista com o cpf {cpf} não encontrado na posição {posicao}')

    def buscar_por_cpf(self, cpf):
        aux = self.__inicio
        while aux != None:
            if aux.cpf == cpf:
                return aux
            aux = aux.prox
        raise ListaException(f'Surfista com o cpf {cpf} não encontrado')

    def ordenar(self):
        if self.vazio() or self.__tamanho == 1:
            raise ListaException("A lista está vazia, não há o que ordenar.")

        final = self.__tamanho - 1
        while final > 0:
            anterior = None
            atual = self.__inicio
            proximo = atual.prox
            i = 0
            while i < final:
                if atual.nome > proximo.nome:
                    atual.prox = proximo.prox
                    proximo.prox = atual
                    if anterior == None:
                        self.__inicio = proximo
                    else:
                        anterior.prox = proximo
                i += 1
                anterior = self.mostrar_elemento(i - 1)
                atual = self.mostrar_elemento(i)
                proximo = atual.prox
            final -= 1

    def mostrar_elemento(self, posicao):
        if posicao >= self.__tamanho:
            raise ListaException(f'A posição {posicao} não existe')

        i = 0
        aux = self.__inicio
        while i != posicao:
            aux = aux.prox
            i += 1
        return aux

    def __str__(self):
        saida = 'Lista: ['
        p = self.__inicio
        while p != None:
            saida += f'{p.nome} - {p.titulos}'
            p = p.prox

            if p != None:
                saida += ', '

        saida += ']'
        return saida

    def imprimir(self):
        print(self.__str__())


class ListaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
