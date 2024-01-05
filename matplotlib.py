import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 

# Data = {
#     "Ano": [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
#     "Taxa_Desemprego": [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
# }

# df = pd.DataFrame(Data, columns=['Ano', 'Taxa_Desemprego'])
# df.plot(x= 'Ano', y= 'Taxa_Desemprego', kind='line')
# plt.show()

#* SP
x = np.random.randn(200)
y = np.random.randn(200)

df = pd.DataFrame({"x": x, "y": y})
sns.displot(df['x'])
plt.show()

sns.barplot(df.x, df.y)
plt.show()

sns.scatterplot(df.x, df.y, hue=df.x)
plt.show()