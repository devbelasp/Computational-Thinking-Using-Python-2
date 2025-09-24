'''
Pensamento Computacional
- Persistência de dados - decomposição em 3 etapas:
    1. Abrir o arquivo (leitura e escrita)
    2. Processar os dados - (escrever ou ler)
    3. Fechar o arquivo - salva as informações

Em Python, a função open() - lida com a etapa 1. e a função (método) .close() - lida com a etapa 3.

Modos de operação:
- 'w' (write - escrita) - cria um novo arquivo permitindo a escrita.
    OBS.: se o arquivo já existir, todo o seu conteúdo será APAGADO!
- 'r' (read - leitura) - abre o arquivo APENAS para leitura.
- 'a' (append - adicionar) - abre o arquivo para escrita, adicionando um novo conteúdo
    ao final, sem apagar o que já existe


'''

#Exemplo prático de persistência de dados em Arquivos texto
# Cadastro de Alunos

import os

ARQUIVO_TEXTO = "cadastro.txt"

def escrever(dados):
    """Escrever uma lista de Strings em um arquivo, sobrescrevendo o conteúdo ('w')"""
    
    print('Escrevendo no arquivo...')

    try:
        #with permite que o arquivo seja fechado através da abstração (esconde a complexidade do gerenciamento de recursos)
        with open(ARQUIVO_TEXTO, "w") as arquivo:
            for item in dados:
                arquivo.write(f'{item}\n')
        print(f'\n[SUCESSO] Dados escritos em {ARQUIVO_TEXTO}.')
    except Exception as e:
        print(f'\n[ERRO] Ocorreu um erro ao escrever no arquivo: {e}')


def ler():
    """Leitura de todas as linhas de um arquivo e as retorna como uma lista"""

    print('Lendo do arquivo...')

    try:
        with open(ARQUIVO_TEXTO, "r") as arquivo:
            linhas = []
            for linha in arquivo.readlines():
                #strip - remove espaços em branco e quebra de linha
                linhas.append(linha.strip())
        return linhas
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f'\n[ERRO] Ocorreu um erro ao ler o arquivo: {e}')
        return []
    

def adicionar(novo_dado):
    """Adiciona uma nova string ao final do arquivo"""

    print(f'Adicionando um novo dado...')

    try:
        with open(ARQUIVO_TEXTO, "a") as arquivo:
            arquivo.write(f'{novo_dado}\n')
        print(f'\n[SUCESSO] {novo_dado} adicionado no arquivo!')
    except Exception as e:
        print(f'[ERRO] Ocorreu um erro ao adicionar {novo_dado} ao arquivo: {e}')
    

def menu():
    """Exibe o menu de opções para o usuárioe processa as operações"""

    print(' >>> Menu de Operações <<<')

    while True:
        print('\n --- Persistência de dados em Arquivos ---')
        print('1. Escrever nova lista de dados (sobrescrevendo o arquivo)')
        print('2. Ler dados existentes no arquivo')
        print('3. Adicionar um novo dado')
        print('4. Sair')

        escolha = input('Escolha uma opção (1-4): ')

        if escolha == '1':
            dados_brutos = input('Digite os dados separados por vírgula (ex. Ana,Bruno,Carla)')
            dados = dados_brutos.split(',')

            dados_limpos = []
            for item in dados:
                # str = "   Hello World " -> str.strip() | ling = '--- Python ---' -> ling.strip('-')
                dados_limpos.append(item.strip())
                escrever(dados_limpos)
        elif escolha == '2':
            dados = ler()
            if dados:
                print('\nConteúdo do arquivo: ')
                for item in dados:
                    print(item)
            else:
                print('\nO arquivo está vazio ou não existe!')
        elif escolha == '3':
            novo_dado = input('Digite o novo dado: ')
            adicionar(novo_dado)
        elif escolha == '4':
            print('Saindo do programa... até breve!')
            break
        else:
            print('\nOpção inválida! Escolha uma opção...')

#Programa Principal
menu()
