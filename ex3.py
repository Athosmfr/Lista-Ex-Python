# Exercicio 3 - Desenvolver o jogo https://term.ooo/ a partir do arquivo lista_palavras.txt. O jogo deve ser
# jogado por meio do terminal, mantendo a lógica do jogo original. Devem aparecer as letras que já foram 
# descobertas, as letras já tentadas no teclado e assim por diante. Atente-se à formatação.

# Explicação da estratégia: Primeiramente é feita uma função para carregar o arquivo lista_palavras.txt, onde é
# feita a 'leitura' das palavras dentro do arquivo e então separadas as palavras usando .strip(). A função
# jogo_termo() é criada para iniciar o jogo, carregando o arquivo com as palavras e utilizando a biblioteca random
# para escolher de forma aleatória uma palavra e pegar as letras contidas na palavra escolhida, então é disponibilizado
# uma lista com todas as letras do alfabeto que estão disponiveis para usar no jogo e uma variavel acertos para guardar
# as letras corretas inseridas, uma variavel erros com o numero de tentativas erradas a serem acumuladas e uma lista com
# as letras erradas para mostrar ao jogador, finalmente uma variavel 'concluido' para definir se o jogo terminou ou não.
# Dentro do loop while o jogo é executado, primeiramente fazendo uma limpa na tela do terminal para cada jogada, usando
# a biblioteca os. Para cada acerto é alocado a letra no espaço correto da palavra dentro do '[ ]', então são feitas
# verificações, caso uma letra já inserida seja utilizada ou caso acerta uma letra seja alocado no espaço e também caso
# erre uma letra da palavra ela seja retirada da lista de disponiveis e seja colocada na lista de letras erradas. No final
# caso acerte a palavra é demonstrado qual era a palavra correta e o numero de erros que cometeu.

# Detalhamento das estruturas usadas: Listas: para armazenar as letras disponiveis para o jogador utilizar em jogo,
# como também as letras erradas e para armazenar as letras da palavra escolhida como também os acertos.
# While: Loop utilizado para executar o jogo e fazer as verificações dentro até que o jogador acerte a palavra e termine
# o jogo.
# Input: Utilizado para que o jogador insira o valor, no caso uma letra para tentar adivinhar a palavra no jogo.
# os.system: Utilizado para limpar o terminal fazendo com que o jogo possua uma saida mais simples e limpa.
# Random: Biblioteca usada para pegar um valor aleatório da lista de palavras inserida no código.

""" 
Importando as bibliotecas responsaveis pelo funcionamento melhor do jogo, sendo uma responsavel por pegar um valor
aleatório (random) e outra para limpar o terminal (os).

Biblioteca Random: Utilizada para definir valores aleatorios de listas ou semelhantes.
Biblioteca os: Utilizada no código para realizar a limpeza do terminal ao fim de cada jogada.
"""
import random
import os

"""
Função responsavel por carregar o arquivo .txt contendo as palavras para o jogo, fazendo a leitura das linhas do texto
e das palavras com readlines() e usando strip() para remover espaços em branco e separar as palavras
"""
def carregar_palavras(arquivo):
    with open(arquivo, 'r') as file:
        palavras = file.readlines()
    return [palavra.strip() for palavra in palavras]

"""
Função principal do jogo, onde é carregado a lista de palavras e então escolhida uma palavra aleatóriamente com 
random, então é alocada a palavra e disponibilizado uma lista de letras disponiveis, como também outras variaveis
para verificar as letras corretas inseridas, o numero de erros e as letras erradas como também se o jogo foi concluido
ou não. Seguindo é feito o loop While responsavel por continuar o jogo caso o jogador não tenha acertado a palavra,
fazendo a limpeza do terminal com a biblioteca os e fazendo as verificações, caso acerte a letra, alocar no espaço correto
dentro da palavra, caso erre a letra, aumentar o numero de erros e alocar a letra errada dentro da lista de letras erradas.
Ao final do jogo demonstrar a palavra correta e o numero de erros.
"""
def jogo_da_forca():
    termos = carregar_palavras('lista_palavras.txt')

    indice_sorteado = random.randint(0, len(termos) - 1)
    palavra = termos[indice_sorteado]
    letras = list(palavra)

    disponiveis = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"
    ]

    acertos = []
    erros = 0
    letras_erradas = []
    concluido = False

    print("--------TERMO--------")

    while concluido is False:

        os.system('cls' if os.name == 'nt' else 'clear')

        tela = ""
        concluido = True
        for letra in palavra:
            if letra in acertos:
                tela += f"[{letra}] "
            else:
                tela += "[ ] "
                concluido = False

        if concluido:
            continue

        print(tela)
        print()
        print("Letras Disponíveis: ")
        print(disponiveis)
        print(f"Letras Erradas: [{', '.join(letras_erradas)}]")
        print()
        escolha = input("Escolha uma letra: ")

        if escolha not in disponiveis:
            print("Você já usou esta letra. Escolha outra ...")
            continue

        if escolha in palavra:
            print(f"Você acertou a letra {escolha}!")
            acertos.append(escolha)
        else:
            print(f"Ops, você errou! A letra {escolha} não está na palavra.")
            erros += 1
            letras_erradas.append(escolha)

        disponiveis.remove(escolha)

    print("----------------------")
    print("Parabéns, você finalizou o jogo")
    print(f"A palavra era {palavra}!")
    print(f"Total de erros: {erros}")

"""
Chamando a função responsavel por iniciar o jogo
"""
jogo_da_forca()