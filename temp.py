# Importação da função norm
from scipy.stats import norm


# Conjunto de objetos em uma cesta, a média é 8 e o desvio padrão é 2
# Qual a probabilidade de tirar um objeto que peso é menor que 6 quilos?
norm.cdf(6, 8, 2)


from scipy import stats
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt

# Criação de uma variável com dados em uma distribuição normal com a função rvs (100 elementos)
dados = norm.rvs(size = 1000)
dados

#histograma
plt.hist(dados, bins = 20)
plt.title('Dados')


fig, ax = plt.subplots()
stats.probplot(dados, fit=True,   plot=ax)
plt.show()



