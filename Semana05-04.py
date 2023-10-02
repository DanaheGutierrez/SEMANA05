#!/usr/bin/env python
# coding: utf-8

# # SEMANA 05
# Danahe Arleni Gutierrez Gutierrez

# Temas
# 1. Colecciones
# 2. Estructuras decisivas y estructuras repetitivas
# 3. Funciones
# 4. Clases y objetos

# 4. Clases y objetos

# In[1]:


class persona:
    nombre=""
    apellidos=""
    dni=""
    talla=0


# In[2]:


persona1= persona()
persona1.nombre="Danahe"
persona1.apellidos="Gutierrez Gutierrez"
persona1.dni="12345678"
persona1.talla=1.5

#para mostrar
print("persona1")
print(f"Nombre: {persona1.nombre}")
print(f"Apellidos: {persona1.apellidos}")
print(f"DNI: {persona1.dni}")
print(f"Talla: {persona1.talla}")


# In[8]:


#problema 2

#solucion
class curso:
    def __init__(self, codigo, nombre, horas, creditos):
        self.codigo=codigo
        self.nombre=nombre
        self.horas=horas
        self.creditos=creditos
        
    def mostrar_datos_curso(self):
        print(f"Curso: {self.nombre}")
        print(f"Codigo: {self.codigo}")
        print(f"Horas: {self.horas}")
        print(f"Creditos: {self.creditos}")


# In[9]:


curso1 = curso("C0501","LP3",6,3)


# In[10]:


curso1.mostrar_datos_curso();

