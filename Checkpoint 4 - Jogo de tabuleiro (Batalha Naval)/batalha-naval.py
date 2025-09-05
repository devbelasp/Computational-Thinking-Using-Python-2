#Isabela dos Santos Pinto - RM 563422
#Manuela de Lacerda Soares - RM 564887

'''
Requisitos:
- criar o tabuleiro [linha][coluna]
- colocar navios aleatóriamente # verificar para não colocar navios no mesmo lugar
- mostrar tabuleiro
- ataque # verificações para ataque/acertos
- verificar vitória
- criar uma função principal para rodar o jogo
'''
import random

#Função para criar o tabuleiro
def criar_tabuleiro(tamanho):
    tabuleiro = [] #Matriz vazia
    for indice_linha in range(tamanho):
        linha = [] #Criando uma lista vazia para indice de linha x
        for indice_coluna in range(tamanho):
            linha.append('~') #Preencher as colunas dessa lista com '~'
        tabuleiro.append(linha) #Terminando o loop o tabuleiro vai receber a linha preenchida com as colunas
    return tabuleiro #Retorna o tabuleiro preenchido


#Função para mostrar o tabuleiro
def mostrar_tabuleiro(tabuleiro, ocultar=False):

    #Cabeçalho - indices de coluna
    print('  ', end='')
    for indice_coluna in range(len(tabuleiro)):
        print(f'{indice_coluna:2}', end=' ')
    print()

    #Indices de linha
    for indice_linha in range(len(tabuleiro)):
        print(f'{indice_linha:2}', end=' ')
        #Mostrar conteudo do tabuleiro
        for indice_coluna in range(len(tabuleiro)):
            conteudo = tabuleiro[indice_linha][indice_coluna]
            # caso ocultar for verdadeiro
            if ocultar and conteudo not in ['~', 'X', 'O']:
                print(f'{"~":2}', end=' ')
            else:
                print(f'{conteudo:2}', end=' ')
        print()

#Função para colocar navios no tabuleiro
def colocar_navios(tabuleiro):

    navios = {
        'P' : 4, # Porta-aviões
        'S' : 1, # Submarino
        'C' : 2, # Cruzador
        'D' : 5, # Destroyer
        'G' : 3  # Guardião dos Mares'
    }

    for nome_navio, tamanho_navio in navios.items():
        colocado = False
        while not colocado:
            #randomizar posição inicial [linha][coluna]
            indice_linha = random.randint(0, len(tabuleiro) - 1)
            indice_coluna = random.randint(0, len(tabuleiro) - 1)

            posicao = random.choice(['h','v']) #horizontal ou vertical
            if posicao == 'h':
                if indice_coluna + tamanho_navio <= len(tabuleiro): #certifica se o navio não irá ultrapassar o tabuleiro

                    #verificar espaço livre
                    espaco_livre = True
                    for espaco in range(tamanho_navio):
                        if tabuleiro [indice_linha][indice_coluna + espaco] != '~':
                            espaco_livre = False
                            break

                    if espaco_livre:
                        for espaco in range(tamanho_navio):
                            tabuleiro[indice_linha][indice_coluna + espaco] = nome_navio
                        colocado = True

            else: #vertical
                if indice_linha + tamanho_navio <= len(tabuleiro):
                    espaco_livre = True
                    for espaco in range(tamanho_navio):
                        if tabuleiro [indice_linha + espaco][indice_coluna] != '~':
                            espaco_livre = False
                            break
                    if espaco_livre:
                        for espaco in range(tamanho_navio):
                            tabuleiro[indice_linha + espaco][indice_coluna] = nome_navio
                        colocado = True


#Função para atacar o inimigo
def ataque_jogador(tabuleiro):
    while True:
        try:
            linha = int(input("\nEscolha a linha para atacar: "))
            coluna = int(input("Escolha a coluna para atacar: "))

            # Verifica limites do tabuleiro antes de acessar
            if linha < 0 or linha >= len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro):
                print("\nNúmero fora do tabuleiro! Tente novamente.")
                continue

            if tabuleiro[linha][coluna] in ['X', 'O']:
                print("\nVocê já atacou nessa posição!")
                continue

            print('\n*------ Resumo da Batalha ------*')

            if tabuleiro[linha][coluna] in ['P', 'S', 'C', 'D', 'G']:
                tabuleiro[linha][coluna] = 'X'
                print("\nSeu ataque: Acertou! 😎")
            else:
                tabuleiro[linha][coluna] = 'O'
                print("\nSeu ataque: Ops, passou longe! 😅")
            break

        except ValueError:
            print("\nDigite números válidos!")



#Função para o ataque da máquina
def ataque_maquina(tabuleiro):
    atacou = False
    while not atacou:
        linha = random.randint(0, len(tabuleiro) - 1)
        coluna = random.randint(0, len(tabuleiro) - 1)
        if tabuleiro[linha][coluna] not in ['X', 'O']: #previne que o ataque seja no mesmo lugar
            if tabuleiro[linha][coluna] in ['P', 'S', 'C', 'D', 'G']:
                tabuleiro[linha][coluna] = 'X'
                print(f'\nA máquina atacou a posição [{linha}, {coluna}] e acertou seu navio! 💥')
            else:
                tabuleiro[linha][coluna] = 'O'
                print(f'\nA máquina atacou a posição [{linha}, {coluna}] e errou! 😅')
            atacou = True


#Função para verificar navios afundados
def verificar_navios_afundados(tabuleiro,navios_afundados, navios_restantes, quem = 'Você'):
    navios = {
        'P': 'Porta-aviões',
        'S': 'Submarino',
        'C': 'Cruzador',
        'D': 'Destroyer',
        'G': 'Guardião dos Mares'
    }

    for simbolo, nome in navios.items():
        # Verifica se o navio ainda não foi afundado
        if nome not in navios_afundados:
            afundado = True
            for linha in tabuleiro:
                if simbolo in linha:
                    afundado = False
                    break
            if afundado:
                navios_restantes -= 1
                print(f'\n💥 {quem} afundou o navio {nome}! ⚓ Navio(s) restante(s): {navios_restantes} 🚢')
                navios_afundados.append(nome)
    return navios_restantes


#Função principal do jogo
def jogar_batalha_naval():
    while True:  # Loop do "jogar novamente"
        tamanho = 10

        #Criando os tabuleiros
        tabuleiro_jogador = criar_tabuleiro(tamanho)
        tabuleiro_maquina = criar_tabuleiro(tamanho)

        #Colocando os navios nos tabuleiros respectivos
        colocar_navios(tabuleiro_jogador)
        colocar_navios(tabuleiro_maquina)

        #Regras do jogo
        print('\nBem-vindo(a) à Batalha Naval! 🚢⚔️')
        print('\nDentro do campo de batalha existem 5 navios para cada tabuleiro:')
        print('(P) Porta-aviões - ocupa 4 espaços')
        print('(S) Submarino - ocupa 1 espaço')
        print('(C) Cruzador - ocupa 2 espaços')
        print('(D) Destroyer - ocupa 5 espaços')
        print('(G) Guardião dos Mares - ocupa 3 espaços')

        print('\n🎯 Objetivo do jogo:')
        print('Afundar todos os navios do inimigo antes que ele afunde os seus!')

        print('\n📜 Regras básicas:')
        print('- Escolha uma coordenada (linha e coluna) para atacar.')
        print("- Se acertar um navio, o local será marcado com 'X'.")
        print("- Se errar, o local será marcado com 'O'.")
        print('- O jogo continua até todos os navios de um dos jogadores serem destruídos.')

        navios_restantes_maquina = 5
        navios_restantes_jogador = 5
        navios_afundados_jogador = []
        navios_afundados_maquina = []

        while True: # Loop da partida
            print('\n *---- Tabuleiro do inimigo ----*\n')
            mostrar_tabuleiro(tabuleiro_maquina, ocultar=True)

            # Ataque do jogador
            ataque_jogador(tabuleiro_maquina)
            navios_restantes_maquina = verificar_navios_afundados(tabuleiro_maquina, navios_afundados_maquina, navios_restantes_maquina, quem='Você')

            if navios_restantes_maquina == 0:
                print('\nParabéns! Você venceu a Batalha Naval! 🏆')
                break

            # Ataque da máquina
            ataque_maquina(tabuleiro_jogador)
            navios_restantes_jogador = verificar_navios_afundados(tabuleiro_jogador, navios_afundados_jogador, navios_restantes_jogador, quem='A máquina')

            if navios_restantes_jogador == 0:
                print('\nA máquina venceu! 💻')
                break

            print('\n\n *------- Seu tabuleiro -------*\n')
            mostrar_tabuleiro(tabuleiro_jogador)


        jogar_novamente = input('\nDeseja jogar novamente? (s/n): ').lower()
        if jogar_novamente != 's':
            print('\n-----------------------------------')
            print('\nObrigada por jogar! Até a próxima 👋')
            break


jogar_batalha_naval()