import pandas as pd #importa da biblioteca panda
import numpy as np

cliente = {
    "nome": ['Marcio', 'Ana', 'Maria', 'João'],
    "idade": [33, 25, 78, 44],
    "telefone": [123, 456, 789, 101]
} #? criacao do dicionario cliente
# print(cliente) #? print do cliente sem ser criado o dataframe
# print("\n")
#? Criar DataFrame
# dataframe = pd.DataFrame(cliente)
# print(dataframe) #? print do cliente apos ser criado o dataframe, fica igual a uma tabela

# vetor = np.array([5, 6, 7, 8])
# v = pd.Series(vetor)
# print("\n")
# print(vetor)
# print(v)


#* Situação problema
df = pd.DataFrame(cliente)
print(df)
# print("\n")
# print(df.nome)
print("media das idades =", df.idade.mean()) #? faz a media das idades do dataframe
print("maior idade =", df.idade.max()) #? tira a maior idade
print("menor idade =", df.idade.min()) #? tira a menor idade

s = pd.Series(("Carla", "Alice"), index = ["03", "07"])
print("\n")
print(s)