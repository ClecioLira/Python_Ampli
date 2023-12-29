import sqlite3

def ExcluirCliente(cod):
    sql = """
        DELETE FROM cadastro WHERE codigo = :param
    """
    cursor.execute(sql, {"param" : cod})
    conector.commit()
    return f"Cliente {cod} EXCLUIDO."

conector = sqlite3.connect('conta.db')
cursor = conector.cursor()

ExcluirCliente(1587)