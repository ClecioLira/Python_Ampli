import sqlite3

conector = sqlite3.connect('conta.db')
cursor = conector.cursor()

sql = """
    CREATE TABLE cadastro (codigo INTEGER, nome TEXT, idade INTEGER)
"""
cursor.execute(sql)

sql = """
    INSERT INTO cadastro (codigo, nome, idade) VALUES (1284, 'Pedro Oliveira', 32)
"""
cursor.execute(sql)

sql = """
    INSERT INTO cadastro (codigo, nome, idade) VALUES (1389, 'Luzia Magalhães', 27)
"""
cursor.execute(sql)

sql = """
    INSERT INTO cadastro (codigo, nome, idade) VALUES (1587, 'Mario Guard', 18)
"""
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()