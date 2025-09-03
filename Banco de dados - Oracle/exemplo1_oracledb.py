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
        connection = oracledb.connect(user = '********',
                                      password='******', 
                                      host='***********',
                                      port='****',
                                      service_name='****')
    except Exception as e:
        print(f'Erro ao obter a conexão: {e}')
    return connection

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



#Programa Principal
conn = getConnection() #testando a conexão
print(f'Conexão: {conn.version}')
criar_tabela(conn)


