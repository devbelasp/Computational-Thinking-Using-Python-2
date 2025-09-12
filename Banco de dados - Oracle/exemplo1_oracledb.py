'''
CRUD - Create, Read, Update, Delete
- conjunto de operações básicas de manipulação de dados

- Módulo Oracle python-oracledb (biblioteca) (sucessor do cx_oracle)
    - permite que a aplicação Python se conecte a um banco de dados
    Oracle e execute comandos SQL
    
    Pré- requisito
        - pip install oracledb (*)
        - pip install cx_oracle
        - pip install python_oracledb
        - ter um banco de dados Oracle

    String de conexão
    <user_name>/<password>@<db_host_address>:<db_port>/<db_service>
    conn = 'usuario/senha@localhost:1521/orcl' #String de conexão

    Tabela - ceo_details
    campos - nome, sobrenome, empresa, idade
    "Steve"
    "Jobs"
    "Apple"
    50
'''

import oracledb

#criar uma conexão com o Banco de Dados Oracle
def getConnection():
    try:
        conn = oracledb.connect(user = '',
                                      password='', 
                                      host='',
                                      port='',
                                      service_name='')
    except Exception as e:
        print(f'Erro ao obter a conexão: {e}')
    return conn

def criar_tabela(conn):
    #obter uma conexão
    #conn = getConnection()

    #obter um cursor - objeto utilizado para executar instruções SQL
    cursor = conn.cursor()

    try:
        create_table_sql = """
        CREATE TABLE ceo_details (
        id number GENERATED ALWAYS AS IDENTITY,
        first_name VARCHAR (50),
        last_name VARCHAR (50),
        company VARCHAR(30),
        age number(10),
        PRIMARY KEY (id)
        )
    """
        cursor.execute(create_table_sql)
        print(f'Tabela CEO_DETAILS foi criada com sucesso!')
    except oracledb.Error as e:
        print(f'Erro de conexão: {e}')


#Operações CRUD

#Create (insert)
def create_ceo(first_name, last_name, company, age):
    print('*** Inserindo um novo CEO na tabela CEO_DETAILS ***')
    conn = getConnection() #obtendo uma conexão com o BD Oracle
       
    #validação da conexão
    if not conn:
            return
        
    try:
        cursor = conn.cursor() #obter um cursor
        sql = """
            INSERT INTO ceo_details (first_name, last_name, company, age)
            VALUES (:first_name, :last_name, :company, :age)
        """
        cursor.execute(sql, {
            'first_name': first_name,
            'last_name' : last_name,
            'company' : company,
            'age' : age
        })
        conn.commit()
        print(f'CEO {first_name} {last_name} foi adicionado com sucesso!')
    except oracledb.Error as e:
        print(f'Erro ao inserir CEO: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()

#Exibir os dados de todos os CEOs
#Read (select)
def read_ceos():
    print(f'*** Lê e exibe todos os CEOs da tabela ***')

    conn = getConnection()

    if not conn:
        return
        
    try: 
        cursor = conn.cursor()
        sql = """
            SELECT id, first_name, last_name, company, age
            FROM ceo_details ORDER BY id
        """
        cursor.execute(sql)
        print(f'\n --- Lista de CEOs ---')
        rows = cursor.fetchall()
        for row in rows:
            print(f'ID: {row[0]}, Nome: {row[1]} {row[2]}, Empresa: {row[3]}, Idade: {row[4]}')
            print('----------------------------------------')
    except oracledb.Error as e:
        print(f'\nErro ao ler CEOs: {e}')
    finally:
        if conn:
            conn.close()

#Atualizar dados da tabela CEOs
#Update
def update_ceo(id_ceo, new_age):
    print('*** Atualizando a idade de um CEO ***')
    
    conn = getConnection()

    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        sql = """
            UPDATE ceo_details SET age = :new_age
            WHERE id = : id
        """
        cursor.execute(sql, {'new_age' : new_age, 'id' :id_ceo})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'Idade do CEO com ID {id_ceo} foi atualizada com sucesso!')
        else:
            print(f'Nenhum CEO com ID {id_ceo} foi encontrado!')
    except oracledb.Error as e:
        print(f'\nErro ao atualizar idade: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()

#Remover um CEO por id
#Delete
def delete_ceo(id_ceo):
    print(f'*** Excluindo o CEO com id: {id_ceo} ***')

    conn = getConnection()

    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM ceo_details WHERE id = :id"
        cursor.execute(sql, {'id' : id_ceo})
        conn.commit()
        if cursor.rowcount > 0:
            print(f'CEO com ID {id_ceo} foi excluído com sucesso!')
        else:
            print(f'Nenhum CEO com ID {id_ceo} foi encontrado!')
    except oracledb.Error as e:
        print(f'\nErro ao excluir CEO: {e}')
        conn.rollback()
    finally:
        if conn:
            conn.close()

#menu principal
def main():

    print(f'\n --- Menu CRUD - CEO DETAILS ---')
    print('-----------------------------------')

    while True:
            print('1. Inserir um novo CEO')
            print('2. Listar todos os CEOs')
            print('3. Atualizar a idade do CEO')
            print('4. Excluir um CEO')
            print('5. Sair')

            opcao = int(input('Escolha uma opção: '))
            if opcao == 1:
                first_name = input('Nome: ')
                last_name = input('Sobrenome: ')
                company = input('Empresa: ')
                age = int(input('Idade: '))
                create_ceo(first_name, last_name, company, age)
            elif opcao == 2:
                read_ceos()
            elif opcao == 3:
                id_ceo = int(input('ID do CEO: '))
                new_age = int(input('Nova Idade: '))
                update_ceo(id_ceo, new_age)
            elif opcao == 4:
                id_ceo = int(input('ID do CEO que será removido: '))
                delete_ceo(id_ceo)
            elif opcao == 5:
                print('Saindo do programa... Até breve!')
                break
            else:
                print('Opção inválida... Digite novamente!')


#Programa Principal
#conn = getConnection() #testando a conexão
#print(f'Conexão: {conn.version}')

#criar_tabela(conn)
#print('Fechando a conexão...')
#conn.close()

#create_ceo('Steve', 'Jobs', 'Apple', 50)
#create_ceo('Bill', 'Gates', 'Microsoft', 55)
#create_ceo('Wagner', 'Sanches', 'FIAP', 47)

#read_ceos()
#update_ceo(3, 48)

#delete_ceo(3)
#read_ceos()

main()

