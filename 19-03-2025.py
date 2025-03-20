#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importando os pacotes

import pandas as pd #importar csv
import matplotlib.pyplot as plt #graficos
import seaborn as sns #graficos
from sklearn.linear_model import LinearRegression #Regressão Linear
from sklearn.metrics import r2_score #R²


# In[2]:


#importando os dados
dados = pd.read_csv("C:/Users/20201enpro0168/Downloads/Salary_Data.csv")
dados


# In[6]:


# (i) diagrama de dispersão

plt.scatter(dados['YearsExperience'], dados['Salary'], color = 'lightcoral')
plt.title('Salário anual (dólares) vs. Experiência')
plt.xlabel('Anos de experiência')
plt.ylabel('Salário anual (dólares)')


# In[11]:


# Separação de X e Y

x = dados.iloc[:, :1] #variável independente
y = dados.iloc[:, 1:] #variável dependente


# In[12]:


# (ii) ajuste do modelo (encontrar beta_0 e beta_1 que minimizam o erro)

modelo = LinearRegression()
modelo.fit(x, y)


# In[13]:


print('Coeficiente angular (beta_1): ', modelo.coef_)
print('Intercepto (beta_0): ', modelo.intercept_)


# In[14]:


# Fazendo predições para y usando x

y_pred = modelo.predict(x)


# In[15]:


plt.scatter(dados['YearsExperience'], dados['Salary'], color = 'lightcoral')
plt.plot(x, y_pred, color = 'firebrick')
plt.title('Salário anual (dólares) vs. Experiência')
plt.xlabel('Anos de experiência')
plt.ylabel('Salário anual (dólares)')


# In[16]:


# (iii) Verificação do coeficiente de determinação (R²)

r2_score(y, y_pred)


# In[21]:


# A pessoa com 4 anos de experiência ganha quanto?

import numpy as np

x_novo = np.array([[4]])
modelo.predict(x_novo)


# In[ ]:





# In[ ]:




