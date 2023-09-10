# Exercicio 4 - “Banco de dados” de dicionários.Crie um menu com três opções: 1-cadastrar usuário 2-imprimir usuários 0-encerrar
# Ao iniciar, o programa deve solicitar ao usuário os nomes dos campos que serão obrigatórios para os cadastros.
# Na sequência, deve mostrar o menu e iniciar o fluxo normal de execução.

# Explicação da estratégia: Primeiramente, é definida uma função chamada "cadastrar_usuario" que recebe como argumento uma lista chamada "campos_obrigatorios".
# Essa função é responsável por coletar informações de um usuário e adicioná-lo a um banco de dados global chamado "banco_usuarios".
# Dentro da função "cadastrar_usuario", é criado um dicionário vazio chamado "usuario" para armazenar as informações do usuário.
# Em seguida, inicia-se um loop que percorre os campos obrigatórios definidos na lista "campos_obrigatorios". Para cada campo, o programa
# solicita ao usuário que insira um valor correspondente e armazena esse valor no dicionário "usuario" com a chave sendo o nome do campo.
# Após coletar os valores dos campos obrigatórios, o programa entra em outro loop que permite ao usuário adicionar campos adicionais e seus valores,
# até que o usuário digite "sair". Os campos adicionais e seus valores também são armazenados no dicionário "usuario".
# Por fim, o dicionário "usuario" é adicionado à lista global "banco_usuarios", que armazena todos os usuários cadastrados.
# Em seguida, a função "imprimir_usuarios" é definida. Ela permite imprimir os usuários com várias opções de filtragem.
# O usuário é solicitado a escolher uma opção de filtragem (1, 2, 3 ou 4) e, com base na opção escolhida, a função realiza diferentes ações,
# como imprimir todos os usuários, filtrar por nomes, campos, ou nomes e campos.
# A função "programa" é a função principal do programa. Ela começa solicitando ao usuário que insira os campos obrigatórios para o cadastro
# e, em seguida, entra em um loop que exibe um menu com três opções: cadastrar usuário, imprimir usuários e encerrar o programa.
# Dependendo da opção escolhida pelo usuário, a função chama as funções "cadastrar_usuario" ou "imprimir_usuarios" para executar a ação desejada.
# O código é organizado em funções separadas, o que torna o programa modular e mais fácil de entender. Isso também permite que o usuário
# realize várias operações, como cadastrar e visualizar usuários, de acordo com suas necessidades.

# Detalhamento das estruturas usadas: Dicionario: para armazenar os usuarios e seus valores foi criado um dicionario, alocando seus respectivos campos.
# While: Loop utilizado para verificar se quer inserir um novo campo ou executar o programa, e voltar para o menu para que seja escolhido uma nova opção.
# Input: Usado para que possa inserir os campos para cadastro do usuario e para cadastrar o usuario de acordo com os campos inseridos.

# Dicionário para armazenar os usuários a serem registrados.
usuarios = []

"""
Função para cadastrar um usuario, pegando os campos criados inicialmente e trazendo um input para alocar os valores obrigatorio,
passando por todos os campos e no final perguntando se quer criar algum novo campo, caso contrario escreva sair e então é
cadastrado o usuario.
"""
def cadastro_de_usuario(campos_obgt):
    usuario = {}
    for campo in campos_obgt:
        valor = input(f"Digite o valor para o campo '{campo}': ")
        usuario[campo] = valor
    
    while True:
        campo_extra = input("Digite um campo extra (ou 'sair' para finalizar): ")
        if campo_extra.lower() == 'sair':
            break
        valor_extra = input(f"Digite o valor para o campo '{campo_extra}': ")
        usuario[campo_extra] = valor_extra
    
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

"""
Função para imprimir os usuarios baseados em opções, podendo imprimir todos caso usuario insira o valor de numero 1, e 
filtrar por nomes caso escolha o numero 2, filtrar pelos campos com o numero 3 e por fim filtrar por nomes e campos com o numero 4,
retornando erro caso escolha uma opção com numero diferente dos que são exibidos.
"""
def imprimir_usuarios(*args, **kwargs):
    opcao = input("1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\nEscolha uma opção: ")
    
    if opcao == '1':
        for usuario in usuarios:
            print(usuario)
    elif opcao == '2':
        nomes = args
        for usuario in usuarios:
            if usuario['nome'] in nomes:
                print(usuario)
    elif opcao == '3':
        campos = kwargs.keys()
        for usuario in usuarios:
            if all(usuario[campo] == kwargs[campo] for campo in campos):
                print(usuario)
    elif opcao == '4':
        nomes = input("Digite os nomes (separados por vírgula): ").split(',')
        campos = input("Digite os campos (separados por vírgula): ").split(',')
        condicoes = {}
        for campo in campos:
            valor = input(f"Digite o valor para o campo '{campo}': ")
            condicoes[campo] = valor
        
        for usuario in usuarios:
            if usuario['nome'] in nomes and all(usuario[campo] == condicoes[campo] for campo in campos):
                print(usuario)
    else:
        print("Opção inválida")

"""
Função principal, pedindo para que crie inicialmente os campos para cadastro do usuario, em seguida demonstrando o menu,
podendo escolher entre as opções de Cadastrar usuario, imprimir usuario ou encerrar a sessão usando os numeros demonstrados (1, 2, 0).
Enquanto continuar nas operações 1 e 2 o loop cadastra e imprimi de acordo com as ações do usuario e somente encerra caso o 
usuario deseje ao selecionar a opção 0 de Encerrar.
"""
def programa():
    campos_obgt = input("Digite os campos obrigatórios (separados por vírgula): ").split(',')
    
    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastro_de_usuario(campos_obgt)
        elif opcao == '2':
            imprimir_usuarios()
        elif opcao == '0':
            break
        else:
            print("Opção inválida")

programa()