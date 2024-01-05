import pandas as pd
import matplotlib.pyplot as plt

Data = {
    "Ano": [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
    "Taxa_Desemprego": [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
}

df = pd.DataFrame(Data, columns=['Ano', 'Taxa_Desemprego'])
df.plot(x= 'Ano', y= 'Taxa_Desemprego', kind='line')
plt.show()