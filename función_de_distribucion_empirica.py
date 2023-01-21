import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF 
from scipy.stats import binom
from scipy import stats

print('Dado la siguiente lista crea un programa que encuentre F_n(x) como su grafica  7')
lista = [1, 3, 4 ,4 ,8 ,2 ,5 ,4 ,6 ,8 ,4 ,4 ,3 ,1 ,3 ,4 ,3 ,4 ,4 ,4 ,5 ,2 ,6 ,2 ,8 ,6 ,3 ,3 ,6 ,2 ,5 ,8 ,8 ,3 ,3 ,2 ,6 ,6 ,3 ,6 ,5 ,2 ,6 ,2 ,8 ,6 ,3 ,3 ,6 ,2 ,5 ,8 ,8 ,3 ,3 ,2 ,6 ,6 ,3 ,6 ]

def fnx(X):
  df = pd.DataFrame({"X":X})
  dfclean = pd.DataFrame(df.groupby('X')['X'].count().reset_index(name='counts'))
  dfclean.columns = ['x','Fx']
  dfclean['pxn'] = dfclean['Fx']/len(lista) 
  dfclean['Fxn'] = np.cumsum(dfclean['pxn'])
  return(dfclean)
  
a = fnx(lista)

sns.ecdfplot(lista)

print(a)

plt.title(str('Funcion de distribucion empírica. ') )
plt.xlabel('Tamaño de la muestra')
plt.ylabel('Probabilidad acumulada')
plt.legend([ 'JairAmaro_Fn(x)'], loc ="upper left")
plt.grid(color='red', linestyle='dotted',linewidth=1.3)
plt.show()

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Con tu lista encuentra la prueba de las hipótesis: la mediana es al menos 5 y el percentil .77 es a lo mas 6
a = np.percentile(lista, 50)
print('\n')
print('La mediana y el percentil (al menos 5 y .77 es a lo mas 6')
print('La hipotesis es falsa ya que la mediana es :' , a)
c = 77 / 100 * 100
a = np.percentile(lista, c)
print('El percentil .77 es verdadera ya que el precentil es :' , a)
print('\n  \n')

# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
# Suponga que tiene un tamaño de la muestra 53: se plantea el siguiente intervalo
# Dado el Intervalo : (X_(13), X_(34)) para la mediana ¿Cual es su nivel de confianza?
# Dado el Intervalo : (X_(18), X_(33)) para el tercer cuartil ¿Cual es su nivel de confianza?
# Dado el Intervalo : (X_(2), X_(52)) para el primer cuartil ¿Cual es su nivel de confianza?

k = 13
R = 34
p = 0.5
n = 53

prob = binom.cdf(R-1,n,p) - binom.cdf(k-1,n,p)

print('El nivel de confianza para la media es:', prob)


k = 18
R = 33
p = 0.75
n = 53

prob = binom.cdf(R-1,n,p) - binom.cdf(k-1,n,p)

print('El nivel de confianza para el tercer cuartil es:', prob)


k = 2
R = 52
p = 0.25
n = 53

prob = binom.cdf(R-1,n,p) - binom.cdf(k-1,n,p)

print('El nivel de confianza para el primer cuartil es:', prob)