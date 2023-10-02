#!/usr/bin/env python
# coding: utf-8

# # SEMANA 05
# Danahe Arleni Gutierrez Gutierrez

# Temas
# 1. Colecciones
# 2. Estructuras decisivas y estructuras repetitivas
# 3. Clases y objetos
# 4. Funciones

# 2. Estructuras decisivas y estructuras repetitivas

# In[6]:


#problema 1
LP3 = ["FIGUEROA", "GARCIA", "GUTIERREZ", "ISLA", "LOPEZ", "LUQUE", "MAMANI", "MARCANI", "MONDRAGON", "MORENO", "MUÑOZ", "NAVARRO", "OTAZU", "PASCACIO", "RAMON", "TENORIO", "VEGAS"]

apellido_buscar = input("Ingrese un apellido: ")

apellido_buscar = apellido_buscar.upper()

# Verificar si el apellido está en la lista
if apellido_buscar in LP3:
    print(f"El apellido {apellido_buscar} se encuentra en la lista.")
else:
    print(f"El apellido {apellido_buscar} no se encuentra en la lista.")


# In[4]:


#problema 2

#solucion
ventas = float(input("Importe de ventas realizados: "))
if ventas <0:
    print("Datos erroneos")
else:
    if ventas<=1000:
        print("Categoria A")
else:
    if ventas <=2500:
        print("Categoria B")
else:
    if ventas <=5000:
        print("Categoria C")
else:
    print("Categoria D")


# In[ ]:


#PROBLEMA

#SOLUCION
cadena = input 


# In[3]:


range(5)
#range(0,5)


# In[7]:


for numero in range(10,22,2):
    print (numero)


# In[8]:


#while
numero=1
fin=10
while numero<=fin:
    print(numero)
    numero+=1


# In[ ]:




