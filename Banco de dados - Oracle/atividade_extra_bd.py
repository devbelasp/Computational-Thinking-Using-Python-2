#Isabela dos Santos Pinto - RM: 563422

#Exercício: Sistema de Gerenciamento de Produtos

import oracledb

#Função para criar (obter) uma conexão com o banco de dados Oracle
def get_conexao():
    try:
        conn = oracledb.connect(
        user = 'rm563422',
        password = '240698',
        host = 'oracle.fiap.com.br',
        port= '1521',
        service_name= 'orcl'
        )
    except Exception as e:
        print(f'Erro ao obter a conexão: {e}')
    return conn

#Função para criar a tabela PRODUTO
def criar_tabela():
    conn = get_conexao()
    cursor = conn.cursor() #cursor - objeto utilizado para executar instruções SQL

    try:
        sql = """
            CREATE TABLE PRODUTO(
            id number GENERATED ALWAYS AS IDENTITY,
            nome VARCHAR(50),
            descricao VARCHAR(200),
            fornecedor VARCHAR(50),
            preco number(10),
            PRIMARY KEY (id)
            )
        """
        cursor.execute(sql)
        print(f'Tabela PRODUTO foi criada com sucesso!')
    except oracledb.Error as e:
        print(f'A Tabela PRODUTO já existe ou ocorreu um erro de conexão: {e}')

#Funcionalidades (CRUD)

#Create (insert)
def inserir_produto(nome, descricao, fornecedor, preco):
    print('\n*** Inserindo um novo produto na tabela PRODUTO ***')
    conn = get_conexao()

    #validação da conexão
    if not conn:
            return
    
    try:
        cursor = conn.cursor() #obter um cursor
        sql = """
            INSERT INTO PRODUTO (nome, descricao, fornecedor, preco)
            VALUES (:nome, :descricao, :fornecedor, :preco)
        """
        cursor.execute(sql, {
            'nome' : nome,
            'descricao' : descricao,
            'fornecedor' : fornecedor,
            'preco' : preco
        })
        conn.commit()
        print(f'PRODUTO {nome}, R$ {preco} adicionado com sucesso!')
    except oracledb.Error as e:
        print(f'\nErro ao inserir produto: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()    

#Read (select)
def listar_produtos():
    print('\n*** Lendo e exibindo todos os produtos da tabela ***')
    conn = get_conexao()
    if not conn:
        return
   
    try:
        cursor = conn.cursor()
        sql = """
            SELECT id, nome, descricao, fornecedor, preco
            FROM PRODUTO ORDER BY id
        """
        cursor.execute(sql)
        print('\n --------------------------------------------------Lista de Produtos------------------------------------------------------------')
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]}, Nome: {row[1]}, Descrição: {row[2]}, Fornecedor: {row[3]}, Preço: {row[4]}')
            print('--------------------------------------------------------------------------------------------------------------------------------')
    except oracledb.Error as e:
        print(f'\nErro ao ler PRODUTOS: {e}')
    finally:
        if conn:
            conn.close()

def buscar_produto_por_id(id_produto):
    print('\n*** Buscando um produto específico com base no seu id ***')
    conn = get_conexao()
    if not conn:
        return
   
    try:
        cursor = conn.cursor()
        sql = """
            SELECT * FROM PRODUTO WHERE id = :id
        """
        cursor.execute(sql, {'id' :id_produto})
        print(f'\n -------------------------------------------------- Exibindo produto com ID {id_produto} --------------------------------------------------')
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]}, Nome: {row[1]}, descrição: {row[2]}, Fornecedor: {row[3]}, Preço: {row[4]}')
            print('--------------------------------------------------------------------------------------------------------------------------------')
    except oracledb.Error as e:
        print(f'\nErro a buscar produtos: {e}')
    finally:
        if conn:
            conn.close()

#Update (update)
def atualizar_preco_produto(id_produto, novo_preco):
    print(f'\n*** Alterando o preço de um produto ***')
    conn = get_conexao()
    if not conn:
        return
   
    try:
        cursor = conn.cursor()
        sql = "UPDATE PRODUTO SET preco = :novo_preco WHERE id = :id"
        cursor.execute(sql, {'novo_preco' : novo_preco, 'id' : id_produto} )
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Preço do produto com ID {id_produto} foi atualizado!')
        else:
            print(f'Nenhum produto com ID {id_produto} foi encontrado!')
    except oracledb.Error as e:
        print(f'\nErro ao atualizar preço: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()

#Delete (delete)
def deletar_produto(id_produto):
    print(f'\n*** Excluindo o produto com id: {id_produto} ***')
 
    conn = get_conexao()
 
    if not conn:
        return
   
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM PRODUTO WHERE id= :id"
        cursor.execute(sql, {'id' : id_produto})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Produto com ID {id_produto} foi excluído com sucesso!')
        else:
            print(f'Nenhum Produto com ID {id_produto} foi encontrado!')
    except oracledb.Error as e:
        print(f'\n Erro ao excluir Produto: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()      
 
#Menu principal com opções para gerenciar Produtos (inserir, listar, buscar, atualizar e deletar)
def menu():
    print('\n*** MENU PRINCIPAL ***')
    print('----------------------')
 
    while True:
        print(f'\n --- Menu CRUD - PRODUTO ---')
        print('1. Inserir um novo produto')
        print('2. Listar todos os produtos')
        print('3. Buscar produto por id')
        print('4. Atualizar o preço de um produto')
        print('5. Excluir um produto')
        print('6. Sair')
    
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            nome = input('Nome do produto: ')
            descricao = input('Descrição: ')
            fornecedor = input('Fornecedor: ')
            preco = float(input('Preço: '))
            inserir_produto(nome, descricao, fornecedor, preco)
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            id_produto = int(input('Digite o ID do produto que deseja visualizar: '))
            buscar_produto_por_id(id_produto)
        elif opcao == 4:
           listar_produtos()
           id_produto =int(input('\nDigite o ID do produto que deseja atualizar: '))
           novo_preco = float(input('Digite o novo preço do produto: '))
           atualizar_preco_produto(id_produto, novo_preco)
        elif opcao == 5:
            listar_produtos()
            id_produto = int(input('\nDigite o ID do produto que deseja excluir: '))
            deletar_produto(id_produto)  
        elif opcao == 6:
            print('Saindo do programa. Até mais!')
            break
        else:
            print('Opção inválida. Tente novamente!')
 

# criando tabela PRODUTO
criar_tabela() 

#Programa Principal
menu()
 