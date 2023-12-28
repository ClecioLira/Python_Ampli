import sqlite3
# conn = sqlite3.connect('bancoDB.db')
# cursor = conn.cursor()

# dll_create = '''
# CREATE TABLE fornecedor (
#     id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     nome_fornecedor TEXT NOT NULL,
#     cnpj VARCHAR(18) NOT NULL,
#     cidade TEXT,
#     estado VARCHAR(2) NOT NULL,
#     cep VARCHAR(9) NOT NULL,
#     data_cadastro DATE NOT NULL
# );
# '''

# cursor.execute(dll_create)
# cursor.execute("UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor = 1")

# dados = [
#     ('Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01'),

#     ('Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01'),

#     ('Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')
# ]

# cursor.executemany("""
# INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
# VALUES (?, ?, ?, ?, ?, ?)
# """, dados)

# cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = 2")

# conn.commit()
# cursor.execute("SELECT * FROM fornecedor")
# # print("Dados inseridos!")
# # print("Descrição do cursor: ", cursor.description)
# # print("Linhas afetadas: ", cursor.rowcount)
# for linha in cursor.fetchall():
#     print(linha)

# cursor.close()
# conn.close()

class DDLSQLite:
    def _conectar(self, nome_banco):
        nome_banco += '.db'
        conn = sqlite3.connect(nome_banco)
        return conn
    
    def criar_banco_de_dados(self, nome_banco):
        nome_banco += '.db'
        sqlite3.connect(nome_banco).close()
        print(f'O banco de dados {nome_banco} foi criado com sucesso!')
        return None

    def criar_tabela(self, nome_banco, ddl_create):
        conn = self._conectar(nome_banco)
        cursor = conn.cursor()
        cursor.execute(ddl_create)
        cursor.close()
        conn.close()
        print('Tabela criada com sucesso!')
        return None
    
    def apagar_tabela(self, nome_banco, tabela):
        conn = self._conectar(nome_banco)
        cursor = conn.cursor()
        cursor.execute(f'DROP TABLE {tabela}')
        cursor.close()
        conn.close()
        print('Tabela apagada com sucesso!')
        return None
    
class CrudSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco + '.db'
    
    def _conectar(self):
        conn = sqlite3.connect(self.nome_banco)
        return conn

    def inserir_registro(self, tabela, registro):
        colunas = tuple(registro.keys())
        valores = tuple(registro.values())
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""INSERT INTO {tabela} {colunas} VALUES {valores}"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print('Dados inseridos com sucesso!')
        return None

    def ler_registros(self, tabela):
        conn = self._conectar
        cursor = conn.cursor()
        query = f"""SELECT * FROM {tabela}"""
        cursor.execute(query)
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado
    
    def atualizar_registro(self, tabela, dado, condicao):
        campo_alterar = list(dado.keys())[0]
        valor_alterar = dado.get(campo_alterar)
        campo_condicao = list(condicao.keys())[0]
        valor_condicao = condicao.get(campo_condicao)
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""UPDATE {tabela} SET {campo_alterar} = '{valor_alterar}' WHERE {campo_condicao} = {valor_condicao}"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print('Dado atualizado com sucesso!')
        return None
    
    def apagar_registro(self, tabela, condicao):
        campo_condicao = list(condicao.keys())[0]
        valor_condicao = condicao.get(campo_condicao)
        conn = self._conectar()
        cursor = conn.cursor()
        query = f"""DELETE FROM {tabela} WHERE {campo_condicao} = {valor_condicao}"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print('Registro apagado com sucesso!')
        return None
    

objeto_ddl = DDLSQLite()

objeto_ddl.criar_banco_de_dados('desafio')

ddl_create = """
    CREATE TABLE cliente (
        id_cliente INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_cliente TEXT NOT NULL,
        cpf VARCHAR(14) NOT NULL,
        email TEXT NOT NULL,
        telefone VARCHAR(15),
        cidade TEXT, 
        estado VARCHAR(2) NOT NULL,
        data_cadastro DATE NOT NULL
    )
"""

objeto_ddl.criar_tabela(nome_banco='desafio', ddl_create=ddl_create)