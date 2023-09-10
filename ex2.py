# Exercicio 2 - Crie um jogo da velha NxN em que o usuário deve definir as dimensões do tabuleiro (sempre
# quadrado).

# Explicação da Estratégia: De inicio, foi construido o tabuleiro com uma lista com elementos definidos pelo jogador, 
# numerados dependendo do tamanho escolhido, tendo dois jogadores, o 'X' e o 'O'. Para garantir que os numeros inseridos
# estejam dentro dos representados na lista é feita uma verificação na função PegarNumero, onde o jogador insere
# o numero que deseja, sendo entre o tamanho definido inicialmente e sendo um numero ainda não selecionado. Então é 
# realizada a função Turno para trocar entre jogadores sua vez de jogar e alocar o simbolo no espaço selecionado. A principal 
# função é a ChecaVitoria() que faz a verificação das linhas e colunas, como também das diagonais, vendo se não foram totalmente
# preenchidas com o simbolo do jogador, caso alguma tenha sido totalmente preenchida com um simbolo de um jogador, o
# mesmo ganha o jogo.

# Detalhamento das estruturas usadas: Listas: Para armazenar valores do tabuleiro
# If : Usados para verificar etapas e regras do jogo.
# While: Loop utilizado para continuar o jogo dependendo da jogada feito pelo Jogador ou acabar caso jogador tenha ganho.
# Funções: Responsaveis por fazer o jogo ser funcional e validar todas as regras necessarias.

"""
Criando um input para o jogador inserir o tamanho do tabuleiro que quer, sendo sempre quadrado e maior que 3.
"""
def JogoDaVelha():
    tamanho_tabuleiro = int(input("Digite o tamanho do tabuleiro (por exemplo, 4 para um tabuleiro 4x4): "))
    if tamanho_tabuleiro < 3:
        print("O tamanho do tabuleiro deve ser pelo menos 3x3.")
        return

    tabuleiro = [str(i + 1) for i in range(tamanho_tabuleiro ** 2)]

    """
    Função que imprimi o tabuleiro de acordo com o tamanho escolhido dentro do terminal.
    """
    def ImprimirTabuleiro():
        for i in range(tamanho_tabuleiro):
            for j in range(tamanho_tabuleiro):
                print(tabuleiro[i * tamanho_tabuleiro + j], end=" ")
            print()

    """
    Criando uma função para pegar um numero valido entre o valor escolhido inicialmente, enquanto a entrada for valida, inserir um valor,
    convertendo o numero para inteiro e verificando se está os valores possiveis, retornando caso seja valido, caso contrario retorna 
    uma mensagem de erro.
    """
    def PegarNumero():
        while True:
            try:
                numero = int(input())
                if 1 <= numero <= tamanho_tabuleiro ** 2 and tabuleiro[numero - 1] != "X" and tabuleiro[numero - 1] != "O":
                    return numero
                else:
                    print("\nEspaço inválido. Tente novamente.")
            except ValueError:
                print("\nIsso não é um número válido. Tente novamente.")

    """
    Função para checar vitoria caso alguma situação demonstrada abaixo se concretize, fazendo verificação da vitória nas linhas,
    nas colunas e nas diagonais, caso o simbolo do jogador esteja em toda uma linha, coluna ou diagonal o mesmo vence o jogo, caso
    contrário o jogo continua e o jogador insere o simbolo em um espaço disponivel. Verificando também qual jogador está jogando e 
    se é seu turno. Loop while imprime o tabuleiro no estado atual e exibe a mensagem de quem é a vez de jogar, pegando a escolha
    do jogador e atualizando o campo caso seja um valor valido e disponivel, então checa se o jogador ganhou senão continua o jogo,
    e troca o turno de jogador.
    """
    def ChecaVitoria(jogador):
        for i in range(tamanho_tabuleiro):
            # Verifica vitória nas linhas
            if all(tabuleiro[i * tamanho_tabuleiro + j] == jogador for j in range(tamanho_tabuleiro)):
                print(f"Jogador {jogador} ganhou!")
                return True

            # Verifica vitória nas colunas
            if all(tabuleiro[i + j * tamanho_tabuleiro] == jogador for j in range(tamanho_tabuleiro)):
                print(f"Jogador {jogador} ganhou!")
                return True

        # Verifica vitória nas diagonais principais
        if all(tabuleiro[i * (tamanho_tabuleiro + 1)] == jogador for i in range(tamanho_tabuleiro)):
            print(f"Jogador {jogador} ganhou!")
            return True

        # Verifica vitória nas diagonais secundárias
        if all(tabuleiro[i * (tamanho_tabuleiro - 1)] == jogador for i in range(1, tamanho_tabuleiro + 1)):
            print(f"Jogador {jogador} ganhou!")
            return True

        return False

    jogador_atual = "X"

    while True:
        ImprimirTabuleiro()
        print(f"Jogador {jogador_atual}, é a sua vez. Escolha um espaço (1-{tamanho_tabuleiro ** 2}):")
        numero_escolhido = PegarNumero()
        tabuleiro[numero_escolhido - 1] = jogador_atual

        if ChecaVitoria(jogador_atual):
            ImprimirTabuleiro()
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"


JogoDaVelha()