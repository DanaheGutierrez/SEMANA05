#!/usr/bin/env python
# coding: utf-8

# # SEMANA 05
# Danahe Arleni Gutierrez Gutierrez

# Temas
# 1. Colecciones
# 2. Estructuras decisivas y estructuras repetitivas
# 3. Clases y objetos
# 4. Funciones

# 1. Colecciones

# In[ ]:


#1.2. Tuplas
tupla_aula = ('Marcani','Vegas','Figueroa','Navarro')
tupla_aula


# In[ ]:


tupla_aula[2]


# In[ ]:


len(tupla_aula)


# In[ ]:


#1.3 Conjuntos
conjunto_aula = ('Ramon','Moreno','Pascacio','Luque')
conjunto_aula


# In[ ]:


for alumno in conjunto_aula:
    print(alumno)


# In[ ]:


#observacion: no se puede acceder por posicion pues no considera indexacion
conjunto_aula[2]


# In[ ]:


len(conjunto_aula)


# In[ ]:


conjunto_aula.add("Muñoz")
conjunto_aula


# In[ ]:


conjunto_aula.remove("Luque")
conjunto_aula


# In[ ]:


#1.4 Diccionarios
diccionario_aula = (2:'Muñoz','1':'Luque','dos':'Pascacio','3':'Navarro','0':'Lopez')
diccionario_aula


# In[ ]:


diccionario_aula['0']


# In[ ]:


diccionario_aula[2]


# In[ ]:


diccionario_aula['1']


# In[ ]:


diccionario_aula['3']


# In[ ]:


diccionario_aula['dos']


# In[ ]:


diccionario_aula['20']="Tenorio"
diccionario_aula


# In[ ]:


diccionario_aula.pop(2)
diccionario_aula


# In[ ]:


del(diccionario_aula["dos"])
diccionario_aula


# In[ ]:


for indice in diccionario_aula:
    print(indice)


# In[ ]:


for indice, valor in diccionario_aula:
    print(indice, valor)


# # 1.5 Ejercicio
# #Dado una lista de [FIGUEROA, GARCIA, GUTIERREZ, ISLA, LOPEZ, LUQUE, MAMANI, MARCANI, MONDRAGON, MORENO, MUÑOZ, NAVARRO, OTAZU, PASCACIO, RAMON, TENORIO, VEGAS]
# #Diseñar un codigo que muestre si el apellido de un estudiante
# #(Ingresado por teclado) forma parte de la lista
# # tiempo 12 minutos

# In[36]:


apellidos = ["FIGUEROA", "GARCIA", "GUTIERREZ", "ISLA", "LOPEZ", "LUQUE", "MAMANI", "MARCANI", "MONDRAGON", "MORENO", "MUÑOZ", "NAVARRO", "OTAZU", "PASCACIO", "RAMON", "TENORIO", "VEGAS"]


# In[37]:


apellido_buscar = input("Ingrese un apellido: ")


# In[38]:


apellido_buscar = apellido_buscar.upper()


# In[39]:


if apellido_buscar in apellidos:
    print(f"El apellido {apellido_buscar} se encuentra en la lista.")
else:
    print(f"El apellido {apellido_buscar} no se encuentra en la lista.")


# In[ ]:




