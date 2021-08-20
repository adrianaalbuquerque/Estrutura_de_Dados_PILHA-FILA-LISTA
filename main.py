from surfista import Surfista
from campeonato import CampeonatoException
from pilha import PilhaException
from lista import ListaException
from fila import FilaException
from campeonato import Campeonato

if __name__ == "__main__":

    # criando objetos surfista

    surfista1 = Surfista("Stephanie Gilmore", 2, 23, 95674)
    surfista2 = Surfista("Sally Fitzgibbons", 3, 26, 84562)
    surfista3 = Surfista("Brisa Hennessy", 1, 21, 34835)
    surfista4 = Surfista("Tatiana Weston", 4, 29, 36475)

    surfista5 = Surfista("Grant Baker", 1, 38, 82373)
    surfista6 = Surfista("Lucas Chianca", 3, 28, 27384)
    surfista7 = Surfista("Natxo Gonzalez", 2, 27, 27383)
    surfista8 = Surfista("Alex Botelho", 1, 31, 51865)

    surfista9 = Surfista("Connor O'Leary", 3, 26, 64316)
    surfista10 = Surfista("Matt Banting", 1, 35, 38715)
    surfista11 = Surfista("Owen Wright", 2, 45, 84724)
    surfista12 = Surfista("Ian Gentil", 5, 18, 48796)

    campeonato1 = Campeonato("Pro Santa Cruz")

    campeonato1.adicionar_surfista_P(surfista1)
    campeonato1.adicionar_surfista_P(surfista2)
    campeonato1.adicionar_surfista_P(surfista3)
    campeonato1.adicionar_surfista_P(surfista4)

    campeonato1.adicionar_surfista_L(surfista5, 0)
    campeonato1.adicionar_surfista_L(surfista6, 1)
    campeonato1.adicionar_surfista_L(surfista7, 2)
    campeonato1.adicionar_surfista_L(surfista8, 3)

    campeonato1.adicionar_surfista_F(surfista9)
    campeonato1.adicionar_surfista_F(surfista10)
    campeonato1.adicionar_surfista_F(surfista11)
    campeonato1.adicionar_surfista_F(surfista12)

    # menu

    print("Seja bem-vindo ao Sistema de Surf! Escolha uma das opções abaixo:")

    while True:
        print("-"*62)
        print("[1] Consultar o Surfista mais jovem do Campeonato")
        print("[2] Consultar o Surfista mais velho do Campeonato")
        print("[3] Incrementar um novo título ao Surfista")
        print("[4] Remover Surfista da Pilha")
        print("[5] Remover Surfista da Lista")
        print("[6] Remover Surfista da Fila")
        print("[7] Buscar Surfista pelo CPF")
        print("[8] Exibir a Lista de Surfistas por ordem alfabética")
        print("[9] Mostrar lista de Surfistas com seus nomes e seus respectivos títulos")
        print("[10] Exibir o tamanho da Pilha da Surfistas")
        print("[11] Exibir o tamanho da Lista de Surfistas")
        print("[12] Exibir o tamanho da Fila da Surfistas")
        print("[X] Para sair")

        print("-"*62)

        opcao_escolhida = input("Digite a opção desejada: ").upper()

        print("-"*62)

        if opcao_escolhida == "1":
            try:
                print(f"Surfista mais jovem do Campeonato {campeonato1}:")
                print(campeonato1.menor_idade())
            except CampeonatoException as campex:
                print(campex)

        elif opcao_escolhida == "2":
            try:
                print(f"Surfista mais velho do Campeonato {campeonato1}:")
                print(campeonato1.maior_idade())
            except CampeonatoException as campex:
                print(campex)

        elif opcao_escolhida == "3":
            cpf = int(input("Digite o CPF do surfista que deseja incrementar um novo títulos:"))
            try:
                campeonato1.incrementa_titulo_surfista(cpf)
                print("Título incrementado com sucesso!!!")
            except ListaException as listex:
                print(listex)

        elif opcao_escolhida == "4":
            try:
                print("Pilha atual:")
                campeonato1.surfistasP.imprimir()
                campeonato1.remover_surfista_P()
                print(" ")
                print("Surfista removido da Pilha com sucesso!")
                print(" ")
                print("Pilha após a remoção:")
                campeonato1.surfistasP.imprimir()
            except PilhaException as pilhex:
                print(pilhex)

        elif opcao_escolhida == "5":
            try:
                print("Lista atual:")
                print(" ")
                campeonato1.imprimir_surfistas()
                print(" ")
                posicao = int(input("Digite a posição que deseja remover um surfista:"))
                campeonato1.remover_surfista_L(posicao - 1)
                print("Surfista removido da Lista com sucesso!")
                print(" ")
                print("Lista após a remoção:")
                print(" ")
                campeonato1.imprimir_surfistas()
            except CampeonatoException as campex:
                print(campex)

        elif opcao_escolhida == "6":
            try:
                print("Fila atual:")
                campeonato1.surfistasF.imprimir()
                campeonato1.remover_surfista_F()
                print("Surfista removido da Fila com sucesso!")
                print(" ")
                print("Fila após a remoção:")
                campeonato1.surfistasF.imprimir()
            except FilaException as filex:
                print(filex)

        elif opcao_escolhida == "7":
            cpf = int(input("Digite o CPF do surfista que deseja:"))
            try:
                print(f'Surfista encontrado: {campeonato1.busca_surfista(cpf)}')
            except ListaException as listex:
                print(listex)

        elif opcao_escolhida == "8":
            try:
                print("Lista atual de Surfistas participantes do Campeonato:")
                print(" ")
                campeonato1.imprimir_surfistas()
                print(" ")
                print("Lista de Surfistas participantes do Campeonato por ordem alfabética:")
                print(" ")
                campeonato1.ordena_surfistas()
                campeonato1.imprimir_surfistas()
            except CampeonatoException as campex:
                print(campex)

        elif opcao_escolhida == "9":
            try:
                campeonato1.imprimir_surfistas()
            except CampeonatoException as campex:
                print(campex)

        elif opcao_escolhida == "10":
            print(campeonato1.mostrar_tam_surfistasP())

        elif opcao_escolhida == "11":
            print(campeonato1.mostrar_tam_surfistasL())

        elif opcao_escolhida == "12":
            print(campeonato1.mostrar_tam_surfistasF())

        elif opcao_escolhida == "X":
            break

        else:
            print("opção inválida. Por favor, digite novamente a opção desejada:")
