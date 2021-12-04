# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:59:16 2021

@author: FRANCISCO
"""
from timeit import default_timer
import os
import psutil

# Se empleará la función orientada a objetos del lenguaje Python, pues la POO
# trabaja muy bien con algoritmos de búsqueda de rutas

class Vertice:
    # Clase para definir un vertice, el cual posee como atributos un id distintivo,
    # lista de relacion de vecinos, estado de visitado
    def __init__(self, i):
        self.id = i             # Distintivo de otros vertices
        self.vecinos = []       # Relacion de vertices vecinos
        self.visitado = False   # Indica si el vertice ha sido visitado
        self.padre = None   # Indica el predecesor al vertice
        self.distancia = float('inf')
        
    def agregarVecino(self, v, p): # La v es el id del vecino, p es el peso
        if v not in self.vecinos:   # Primero se verifica que el vertice no
                                    # esté en la lista de vecinos
            self.vecinos.append([v, p]) # Si no lo está, entonces se agrega a
                                        # la lista

class Grafo:
    # Clase que define los vertices del grafo
    def __init__(self):
        self.vertices = {}  # Se empleará un diccionario, del lado izdistanciaquierdo
                            # estarán los id y del lado derecho los objetos de
                            # tipo Vertice(id)
        
    def agregarVertice(self, id):
        if id not in self.vertices: # Primero se verifica que el id del 
                                    # vertice no se encuentra en el diccionario
            self.vertices[id] = Vertice(id) # Si no lo está, entonces se 
                                            # agrega al diccionario la llave id
                                            # con un objeto de tipo Vertice(id)
    
    def agregarArista(self, a, b, p):   # Se envían los vertices a y b para
                                        # formar la arista. Tener en cuenta 
                                        # que nuestro grafo es de aristas no 
                                        # direccionadas, y poseen un peso p
        if a in self.vertices and b in self.vertices:   # Primero se verifica
                                                        # que los vertices esten
                                                        # en el diccionario
            # Entonces se crea la arista, el vertice a tiene como vecino al b y
            #  esa arista tiene un peso p. Empleamos el metodo agregarVecino()
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)
            # Se tiene que hacer la arista de a hacia b y viceversa, pues es
            # no dirigido y la ruta puede ser en cualquier direccion
            
    def imprimirGrafo(self): # Para imprimir cada nodo con su informacion
        # Del conjunto de vertices, imprimimos al vertice con su distancia y a su predecesor con su distancia
        for v in self.vertices:
            print(
                "La distancia del vertice " + str(v) +
                " es " + str(self.vertices[v].distancia) +
                " llegando desde " + str(self.vertices[v].padre)
                )
            
    def camino(self, a, b): # Indica el camino desde la raíz hasta el nodo final
                            # reconstruyendo el grafo desde el fin hasta el inicio,
                            # para indicarnos la ruta que se debe tomar
        camino = []
        actual = b
        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[b].distancia]
    
    def minimo(self, lista):
        if len(lista) > 0: # Revisamos que la lista tenga elementos
            m = self.vertices[lista[0]].distancia # Escogemos al primer elemento, tomando su distancia
            v = lista[0] # Nodo en la posicion 0 de la lista
            for i in lista:
                if m > self.vertices[i].distancia:  # Si la distancia de un elemento es menor a m, se
                                                    # actualiza m con esa distancia
                    m = self.vertices[i].distancia # Y se actualiza v con el vertice que posee esa menor distancia
                    v = i
            
            return v # Regresamos ese nodo con la minima distancia
            
    def dijkstra(self, a): # El algoritmo parte del nodo inicial a
        if a in self.vertices:  # Se pregunta si el nodo está en el diccionario
                                # de vértices
            
            # El nodo inicial tiene una distancia de 0
            self.vertices[a].distancia = 0
            actual = a  # El nodo actual es a
            noVisitados = []    # Creamos el conjunto de nodos no visitados
            
            for v in self.vertices:
                if v != a: # Se comprueba que v no sea a para no modificar la distancia inicial de 0
                    # Mientras no se encuentre la distancia de a, se establece como infinito
                    self.vertices[v].distancia = float('inf') 
                self.vertices[v].padre = None
                noVisitados.append(v) # Se agregan a todos los nodos al conjunto de no visitados
            
            while len(noVisitados) > 0: # Mientras noVisitados tenga elementos
                for vecino in self.vertices[actual].vecinos: # Recorremos a cada vecino del vertice actual
                    if self.vertices[vecino[0]].visitado == False: # Consideramos a los vertices no visitados
                        # Tomamos la distancia del nodo actual y la sumamos con la distancia de la arista para
                        # llegar al nodo vecino. Si esta suma es menor a la distancia que tiene el vecino
                        # actualmente, entonces se intercambian
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual # Establecemos al nodo actual como padre del vecino
                
                # Marcamos al vertice actual como visitado y lo eliminamos del grupo de no visitados
                self.vertices[actual].visitado = True 
                noVisitados.remove(actual)
                
                # Se selecciona al nodo no visitado con la minima distancia como nodo actual, empleamos una nueva
                # funcion llamada minimo() y le enviamos los no visitados
                actual = self.minimo(noVisitados)
        else:   # En caso que el vertice a no se encuentre en la relacion de 
                # vertices, no se prodrá hacer la ruta
            return False
        
# Construimos el grafo
class main:
    
    inicio = default_timer()
    
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0]/2.**30 #Expresa aproximadamente el uso de la memoria en GB 

    #CASOS DE PRUEBA PROPIOS:

    # Topología de complejidad baja
    
    # Equivalencias:
    # A 1
    # B 2
    # C 3
    # D 4
    # E 5
    # F 6
    # G 7
    
    print("\n\nTopología de complejidad baja")
    
    g2 = Grafo()
    g2.agregarVertice(1)
    g2.agregarVertice(2)
    g2.agregarVertice(3)
    g2.agregarVertice(4)
    g2.agregarVertice(5)
    g2.agregarVertice(6)
    g2.agregarVertice(7)
    
    # Escribimos las aristas junto con su peso, sin repetir
    g2.agregarArista(1, 2, 5)
    g2.agregarArista(1, 3, 2)
    g2.agregarArista(2, 3, 4)
    g2.agregarArista(2, 6, 4)
    g2.agregarArista(3, 4, 1)
    g2.agregarArista(3, 5, 6)
    g2.agregarArista(4, 6, 6)
    g2.agregarArista(5, 7, 7)
    g2.agregarArista(6, 7, 8)
    
    print("\nLa ruta mas rapida mediante el algoritmo Dijkstra (izquierda) y el costo (derecha): ")
    g2.dijkstra(1) # 1 es la raíz, en este caso, A
    # Los resultados se expresan de la siguiente forma:
    # [['ruta'], 'peso de la ruta']
    # El numero que está a la derecha del todo es el peso de la ruta, mientras 
    # que la lista de la izquierda es la ruta en sí
    print(g2.camino(1,7)) # El camino se realizará desde el 1 hasta el 7, A-G
    print("\nLos valores finales del grafo son los siguientes: ")
    g2.imprimirGrafo()
    
    fin = default_timer()
    tiempo = fin - inicio
    
    print('Tiempo de ejecución: ', tiempo)
    print ('Memoria utilizada: ', memoryUse)