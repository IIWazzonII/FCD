#!/usr/bin/env python
# coding: utf-8

# In[31]:


#importando os pacotes

import pandas as pd #importar csv
import matplotlib.pyplot as plt #graficos
import seaborn as sns #graficos
from sklearn.linear_model import LinearRegression #Regressão Linear
from sklearn.metrics import r2_score #R²


# In[32]:


#importando os dados
dados = pd.read_csv("C:/Users/20201enpro0168/Downloads/score_updated.csv")
dados


# In[33]:


# (i) diagrama de dispersão

plt.scatter(dados['Hours'], dados['Scores'], color = 'lightcoral')
plt.title('Nota vs. Horas de estudo')
plt.xlabel('Horas de estudo')
plt.ylabel('Nota')


# In[34]:


# Separação de X e Y

x = dados.iloc[:, :1] #variável independente
y = dados.iloc[:, 1:] #variável dependente


# In[35]:


# (ii) ajuste do modelo (encontrar beta_0 e beta_1 que minimizam o erro)

modelo = LinearRegression()
modelo.fit(x, y)


# In[36]:


print('Coeficiente angular (beta_1): ', modelo.coef_)
print('Intercepto (beta_0): ', modelo.intercept_)


# In[37]:


# Fazendo predições para y usando x

y_pred = modelo.predict(x)


# In[38]:


plt.scatter(dados['Hours'], dados['Scores'], color = 'lightcoral')
plt.plot(x, y_pred, color = 'firebrick')
plt.title('Nota vs. Horas de estudo')
plt.xlabel('Horas de estudo')
plt.ylabel('Nota')


# In[39]:


# (iii) Verificação do coeficiente de determinação (R²)

r2_score(y, y_pred)


# In[40]:


# A pessoa com 4 anos de experiência ganha quanto?

import numpy as np

x_novo = np.array([[4]])
modelo.predict(x_novo)


# In[ ]:





# In[ ]:




