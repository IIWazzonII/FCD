#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Números e operações aritméticas

2+1 #soma


# In[2]:


3 #Coloquei errado *ignorar*


# In[3]:


2-1 #Subtração


# In[4]:


3*4 #Multiplicação


# In[5]:


3/4 #Divisão


# In[6]:


2**8 #Potenciação


# In[7]:


# Variáveis

a = 5

print(a)


# In[8]:


# Strings

minha_string = "Oi" #Aspas podem ser duplas ou simples

print(minha_string)


# In[9]:


# Veriicar comprimento da string

len(minha_string)


# In[10]:


# Colocar tudo em maiúsculas
minha_string.upper()


# In[11]:


# Colocar tudo em minúsculas
"MATHEUS".lower()


# In[13]:


#Quebrando uma string
minha_string_2 = "Matheus Borges Roncete"
minha_string_2.split() #Por padrão dá split no "espaço"


# In[14]:


#Dando split em caracteres específicos
minha_string_2.split("M")


# In[15]:


#Listas

minha_lista = [2, 4, 5, 7]
minha_lista


# In[16]:


minha_lista[0] #Pegando o primeiro elemento da lista


# In[17]:


minha_lista[0:2] #Pegando o primeiro e o segundo elementos


# In[18]:


minha_lista[-1] #-1 se refere ao último elemento


# In[21]:


# Acrecentando um elemento à lista
minha_lista.append(10)
minha_lista


# In[22]:


#Removendo o último elemento
minha_lista.pop()
minha_lista


# In[24]:


#Ordenando elementos
minha_lista_2 = ["d", "b", "c", "a"]
minha_lista_2.sort()
minha_lista_2


# In[25]:


#Ordem reversa
minha_lista_2.reverse()
minha_lista_2


# In[27]:


#Input (pedir informação)

print("Digite seu nome")
nome = input()
print("Nome é", nome)


# In[ ]:




