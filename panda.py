# Criar DataFrame
import pandas as pd #importa da biblioteca panda
import numpy as np

cliente = {
    "nome": ['Marcio', 'Ana', 'Maria', 'João'],
    "idade": [33, 25, 78, 44]
}
print(cliente)
print("\n")
dataframe = pd.DataFrame(cliente)
print(dataframe)


vetor = np.array([5, 6, 7, 8])
v = pd.Series(vetor)
print("\n")
print(vetor)
print(v)