import matplotlib.pyplot as plt
import numpy as np

# Dados
nomes = ['Lucas', 'Dulce', 'Jorge', 'Helen', 'Ernesto']
idades = [20, 21, 18, 32, 24]

cores_tab10 = plt.cm.tab10(np.arange(len(nomes)))
fig, axs = plt.subplots(1, 2, figsize=(10,5))  # 1 linha, 2 colunas

# Gráfico de barras
axs[0].bar(nomes, idades, color=cores_tab10)
axs[0].set_title("Barras")

# Gráfico de pizza
axs[1].pie(idades, labels=nomes, autopct='%1.1f%%')
axs[1].set_title("Pizza")

# Mostrar as duas janelas
plt.show()