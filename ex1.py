# Exercicio 1 - Crie uma versão do jogo da velha 4x4. As regras são as mesmas da versão 3x3.

# Explicação da Estratégia: De inicio, foi construido o tabuleiro com uma lista com 16 elementos, numerados de 1
# a 16, pois o tamanho do jogo deve ser 4x4, tendo dois jogadores, o 'X' e o 'O'. Para garantir que os numeros inseridos
# estejam dentro dos representados na lista é feita uma verificação na função PegarNumero, onde o jogador insere
# o numero que deseja, sendo entre 1 a 16 e sendo um numero ainda não selecionado. Então é realizada a função Turno
# para trocar entre jogadores sua vez de jogar e alocar o simbolo no espaço selecionado. A principal função é a 
# ChecaVitoria() que faz a verificação das linhas e colunas, como também das diagonais, vendo se não foram totalmente
# preenchidas com o simbolo do jogador, caso alguma tenha sido totalmente preenchida com um simbolo de um jogador, o
# mesmo ganha o jogo.

# Detalhamento das estruturas usadas: Listas: Para armazenar valores do tabuleiro
# If : Usados para verificar etapas e regras do jogo.
# While: Loop utilizado para continuar o jogo dependendo da jogada feito pelo Jogador ou acabar caso jogador tenha ganho.
# Funções: Responsaveis por fazer o jogo ser funcional e validar todas as regras necessarias.

"""
Criando uma lista para inicializar os espaços do tabuleiro de 1 a 16 (4x4), uma variavel responsavel pelo fim do jogo.
"""
def JogoDaVelha():
    # Criando uma lista para inicializar os espaços do tabuleiro de 1 a 16 (4x4)
    tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # Variavel responsavel pelo fim do jogo
    acabou = False

    """
    Criando uma função para imprimir o tabuleiro no terminal, alocando cada espaço do tabuleiro de acordo com os numeros
    """
    # Criando uma função para imprimir o tabuleiro no terminal, alocando cada espaço do tabuleiro de acordo 
    # com os numeros
    def ImprimirTabuleiro():
        print()
        print('', tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2], "|", tabuleiro[3])
        print("---|---|---|---")
        print('', tabuleiro[4], "|", tabuleiro[5], "|", tabuleiro[6], "|", tabuleiro[7])
        print("---|---|---|---")
        print('', tabuleiro[8], "|", tabuleiro[9], "|", tabuleiro[10], "|", tabuleiro[11])
        print("---|---|---|---")
        print('', tabuleiro[12], "|", tabuleiro[13], "|", tabuleiro[14], "|", tabuleiro[15])
        print()

    """
    Criando uma função para pegar um numero valido entre 1 a 16 do jogador, enquanto a entrada for valida, inserir um valor,
    convertendo o numero para inteiro e verificando se está entre 1 a 16, retornando caso seja valido, caso contrario retorna 
    mensagem de erro
    """
    # Criando uma função para pegar um numero valido entre 1 a 16 do jogador
    def PegarNumero():
        while True:
            numero = input() # Enquanto a entrada for valida, inserir um valor
            try:
                numero = int(numero) # Converte a entrada para um numero inteiro
                if numero in range(1, 17): # Verifica se o numero inserido está entre 1 a 16
                    return numero # Retorna o numero caso seja valido
                else: # Caso não seja um numero entre 1 a 16 retorna erro
                    print("\nNúmero não está no tabuleiro.")
            except ValueError:
                pass

    """
    Função responsavel pelo turno do jogador, chama a função pegando o numero inserido e diminuindo 1 para pegar o indice correto,
    verifica se a posição escolhida já esta ocupada e retorna para o jogador poder escolher novamente, caso contrario o simbolo é
    inserido no espaço.
    """            
    # Função responsavel pelo turno do jogador
    def Turno(jogador): 
        espaco_colocado = PegarNumero() - 1 # Chama a função pegando o numero inserido e diminuindo 1 para pegar o indice correto
        if tabuleiro[espaco_colocado] == "X" or tabuleiro[espaco_colocado] == "O": # verifica se a posição escolhida já esta ocupada
            print("\nEspaço já ocupado. Tente colocar em outro.")
            Turno(jogador) # Retorna para o jogador poder escolher novamente
        else: # Caso o espaço não tenha sido alocado por algum jogador, o simbolo é inserido no espaço
            tabuleiro[espaco_colocado] = jogador 

    """
    Função para checar vitoria caso alguma situação demonstrada abaixo se concretize, fazendo verificação da vitória nas linhas,
    nas colunas e nas diagonais, caso o simbolo do jogador esteja em toda uma linha, coluna ou diagonal o mesmo vence o jogo, caso
    contrário o jogo continua e o jogador insere o simbolo em um espaço disponivel.
    """
    # Função para checar vitoria caso alguma situação demonstrada abaixo se concretize
    def ChecaVitoria(jogador):
        for i in range(4):
            # Verificando vitória nas linhas
            if tabuleiro[i * 4] == tabuleiro[i * 4 + 1] == tabuleiro[i * 4 + 2] == tabuleiro[i * 4 + 3] == jogador:
                # Verifica se todas as posições em uma linha tem o mesmo simbolo do jogador, se a soma for igual 
                # ao total de elementos da linha, significa que o jogador ganhou tendo o simbolo em toda a linha.
                print("Jogador", jogador, "ganhou!\n")
                return True

            # Verifica vitória nas colunas
            if tabuleiro[i] == tabuleiro[i + 4] == tabuleiro[i + 8] == tabuleiro[i + 12] == jogador:
                #  Verifica se todas as posições em uma coluna tem o mesmo simbolo do jogador, sendo i o indice
                # inicial da coluna e adicionando valores multiplos de 4 para cada indice da coluna
                print("Jogador", jogador, "ganhou!\n")
                return True

        # Verifica vitória nas diagonais
        if tabuleiro[0] == tabuleiro[5] == tabuleiro[10] == tabuleiro[15] == jogador:
            # Verifica se todos os espaços da diagonal possui os mesmos elementos do jogador
            print("Jogador", jogador, "ganhou!\n")
            return True

        if tabuleiro[3] == tabuleiro[6] == tabuleiro[9] == tabuleiro[12] == jogador:
            # Verifica se todos os espaços da diagonal possui os mesmos elementos do jogador
            print("Jogador", jogador, "ganhou!\n")
            return True

        return False
    
    # Loop principal do jogo, enquanto ninguem ganhou, continuar...
    while not acabou:
        ImprimirTabuleiro() # Chama função para imprimir tabuleiro
        acabou = ChecaVitoria("O") # Checa se alguem ganhou
        if acabou:
            break
        print("Jogador X, escolha um espaço.")
        Turno("X") # Jogador X

        ImprimirTabuleiro()
        acabou = ChecaVitoria("X")
        if acabou:
            break
        print("Jogador O, escolha um espaço.")
        Turno("O") # Jogador O


JogoDaVelha() 