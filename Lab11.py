import pandas as pd
from statsmodels.tsa.api import SimpleExpSmoothing
from statsmodels.graphics import tsaplots
import matplotlib.pyplot as plt
import random
import scipy.signal
import seaborn as sns
import numpy as np
import statsmodels.api as sm
from math import *

df = pd.read_csv('C:/Users/Ciri/Desktop/Навчання/Economy_Indicators.csv')

#Експоненціальне згладжування 
def drawAlpha(name, fit):
	print(fit.summary()) 
	plt.title(name) 
	plt.plot(fit.fittedvalues, marker="o", color="blue") 
	plt.show() 

fit1 = SimpleExpSmoothing(df['Jobless Rate'], 
initialization_method="heuristic").fit(smoothing_level=0.1, optimized=False)
drawAlpha('Alpha = 0.1', fit1)

fit2 = SimpleExpSmoothing(df['Jobless Rate'], 
initialization_method="heuristic").fit(smoothing_level=0.2, optimized=False)
drawAlpha('Alpha = 0.2', fit2)

fit3 = SimpleExpSmoothing(df['Jobless Rate'], 
initialization_method="heuristic").fit(smoothing_level=0.3, optimized=False)
drawAlpha('Alpha = 0.3', fit3)
# fit Підігнати модель
# smoothing_level - Значення простого експоненційного згладжування

# медіанний фільтр
def medf(name, fit):
	plt.title(name)
	plt.plot(fit, marker="o", color="green")
	plt.show()

fit1 = scipy.signal.medfilt(df['Jobless Rate'], 3) 
medf('w = 3', fit1)
fit2 = scipy.signal.medfilt(df['Jobless Rate'], 5)
medf('w = 5', fit2)
fit3 = scipy.signal.medfilt(df['Jobless Rate'], 7)
medf('w = 7', fit3)
fit4 = scipy.signal.medfilt(df['Jobless Rate'], 9)
medf('w = 9', fit4)
fit5 = scipy.signal.medfilt(df['Jobless Rate'], 11)
medf('w = 11', fit5)

# Кореляційне відношення
df['Jobless Rate'] = df['Jobless Rate'].fillna(0) 
df['Inflation Rate'] = df['Inflation Rate'].fillna(0) 
X = np.array(df['Jobless Rate']) 
Y = np.array(df['Inflation Rate']) 
job = np.var(X) 
inf = np.var(Y) 
summ = job + inf
res = inf / summ
print('Кореляційне відношення = ', res)

# Ділення на частини
print("\n Ділення на частини")
N = int(len(df['Inflation Rate']) / 3)
arr = [[random.randrange(0,10) for y in range(3)] for x in range(N)] 
for i in range(int(len(df['Inflation Rate']))):
	if i < int(len(df['Inflation Rate']) / 3): 
		arr[i][0] = (df['Jobless Rate'][i]) 
	elif len(df['Inflation Rate']) / 3 < i < 2 * len(df['Inflation Rate']) / 3: 
		k = int(i - len(df['Inflation Rate']) / 3)
		arr[k][1] = (df['Jobless Rate'][i])
	else: 
		k = int(i - 2 * len(df['Inflation Rate']) / 3)
		arr[k][2] = (df['Jobless Rate'][i])
print(arr)

#Кореляційна матриця
data = pd.DataFrame(arr) 
correl_matrix = data.corr() 
print(correl_matrix) 
#sm.tsa.acf(df['Inflation Rate'])
#Теплова карта
sns.heatmap(correl_matrix, annot=True) 
plt.show()

#Автокореляція
fig = tsaplots.plot_acf(df['Inflation Rate'], lags=10)
plt.show() 
