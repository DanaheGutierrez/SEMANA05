#!/usr/bin/env python
# coding: utf-8

# # SEMANA 05
# Danahe Arleni Gutierrez Gutierrez

# Temas
# 1. Colecciones
# 2. Estructuras decisivas y estructuras repetitivas
# 3. Clases y objetos
# 4. Funciones

# 3. Clases y objetos

# In[1]:


def saludo():
    print("Bienvenido al curso de LP3")
    print("**** PYTHON ****")


# In[2]:


saludo()


# In[9]:


#3.4 metodo que reciben variables

def factorial2(numero):
    fac = 1
    for i in range(1,numero+1):
        fac*=i
        #fac =fc*1
    return fac


# In[10]:


numero = int(input("Numero: "))
print(f"El factorial es {numero} es {factorial2(numero)}")


# In[11]:


def obtenerigv(importe):
    return importe*0.19


# In[12]:


obtenerigv(150)


# In[13]:


factorial2(5)+20

