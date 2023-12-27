import sqlite3
conn = sqlite3.connect('bancoDB.db')
cursor = conn.cursor()

dll_create = '''
CREATE TABLE fornecedor (
    id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    cidade TEXT,
    estado VARCHAR(2) NOT NULL,
    cep VARCHAR(9) NOT NULL,
    data_cadastro DATE NOT NULL
);
'''

cursor.execute(dll_create)
cursor.execute("UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor = 5")

dados = [
    ('Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2020-01-01'),

    ('Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01'),

    ('Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')
]

cursor.executemany("""
INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES (?, ?, ?, ?, ?, ?)
""", dados)

conn.commit()
cursor.execute("SELECT * FROM fornecedor")
# print("Dados inseridos!")
# print("Descrição do cursor: ", cursor.description)
# print("Linhas afetadas: ", cursor.rowcount)
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()
