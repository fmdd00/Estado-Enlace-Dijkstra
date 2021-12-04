############################################################################################################

# Como observación, si quisieramos que este programa soporte grafos dirigidos,
# entonces, en la función agregarArista() de la clase Grafo solo tendríamos que
# dejar la línea 48 y eliminar la línea 49, esto significa que al momento de
# construir nuestro grafo en la funcion main, deberíamos defininir que la
# arista es de a hacia b, escribiendo primero el vértice a, luego el b
# y luego el peso p

############################################################################################################

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

############################################################################################################
    
    # Topología de complejidad media
    
    print("\n\nTopología de complejidad media")
    
    # Equivalencias:
    # A 1
    # B 2
    # C 3
    # D 4
    # E 5
    # F 6
    # G 7
    # H 8
    # I 9
    # J 10
    # K 11
    
    g3 = Grafo()
    g3.agregarVertice(1)
    g3.agregarVertice(2)
    g3.agregarVertice(3)
    g3.agregarVertice(4)
    g3.agregarVertice(5)
    g3.agregarVertice(6)
    g3.agregarVertice(7)
    g3.agregarVertice(8)
    g3.agregarVertice(9)
    g3.agregarVertice(10)
    g3.agregarVertice(11)
    
    # Escribimos las aristas junto con su peso, sin repetir
    g3.agregarArista(1, 2, 4)
    g3.agregarArista(1, 5, 5)
    g3.agregarArista(2, 3, 2)
    g3.agregarArista(3, 5, 3)
    g3.agregarArista(3, 4, 1)
    g3.agregarArista(4, 5, 6)
    g3.agregarArista(4, 6, 8)
    g3.agregarArista(4, 7, 5)
    g3.agregarArista(5, 6, 4)
    g3.agregarArista(6, 7, 7)
    g3.agregarArista(6, 9, 1)
    g3.agregarArista(7, 8, 5)
    g3.agregarArista(8, 9, 3)
    g3.agregarArista(8, 11, 1)
    g3.agregarArista(9, 19, 3)
    g3.agregarArista(10, 11, 2)
    
    print("\nLa ruta mas rapida mediante el algoritmo Dijkstra junto con su costo es: ")
    g3.dijkstra(1) # 1 es la raíz, en este caso, A
    # Los resultados se expresan de la siguiente forma:
    # [['ruta'], 'peso de la ruta']
    # El numero que está a la derecha del todo es el peso de la ruta, mientras 
    # que la lista de la izquierda es la ruta en sí
    print(g3.camino(1,11)) # El camino se realizará desde el 1 hasta el 11, A-K
    print("\nLos valores finales del grafo son los siguientes: ")
    g3.imprimirGrafo()
  
############################################################################################################
  
    #CASOS DE PRUEBA UN COMPAÑERO:

    # 1 ACHATA: Topología de complejidad baja
    
    # Nodos: 7
    # Aristas: 9
    
    print("\n\nTopología de complejidad baja de ACHATA")
    
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
    g2.agregarArista(1, 3, 1)
    g2.agregarArista(2, 4, 2)
    g2.agregarArista(3, 4, 2)
    g2.agregarArista(4, 5, 2)
    g2.agregarArista(4, 7, 4)
    g2.agregarArista(5, 6, 1)
    g2.agregarArista(5, 7, 3)
    g2.agregarArista(6, 7, 6)
    
    print("\nLa ruta mas rapida mediante el algoritmo Dijkstra (izquierda) y el costo (derecha): ")
    g2.dijkstra(1) # 1 es la raíz, en este caso, A
    # Los resultados se expresan de la siguiente forma:
    # [['ruta'], 'peso de la ruta']
    # El numero que está a la derecha del todo es el peso de la ruta, mientras 
    # que la lista de la izquierda es la ruta en sí
    print(g2.camino(1,7)) # El camino se realizará desde el 1 hasta el 7, A-G
    print("\nLos valores finales del grafo son los siguientes: ")
    g2.imprimirGrafo()

############################################################################################################
    
    # 2 ACHATA: Topología de complejidad media   
    
    print("\n\nTopología de complejidad media de ACHATA")

    # Nodos: 10
    # Aristas: 17
    
    g3 = Grafo()
    g3.agregarVertice(1)
    g3.agregarVertice(2)
    g3.agregarVertice(3)
    g3.agregarVertice(4)
    g3.agregarVertice(5)
    g3.agregarVertice(6)
    g3.agregarVertice(7)
    g3.agregarVertice(8)
    g3.agregarVertice(9)
    g3.agregarVertice(10)
    
    # Escribimos las aristas junto con su peso, sin repetir
    g3.agregarArista(1, 2, 2)
    g3.agregarArista(1, 3, 1)
    g3.agregarArista(1, 4, 4)
    g3.agregarArista(2, 3, 2)
    g3.agregarArista(2, 5, 4)
    g3.agregarArista(3, 4, 4)
    g3.agregarArista(3, 6, 5)
    g3.agregarArista(4, 6, 6)
    g3.agregarArista(4, 9, 1)
    g3.agregarArista(5, 6, 3)
    g3.agregarArista(5, 7, 7)
    g3.agregarArista(5, 8, 8)
    g3.agregarArista(6, 9, 2)
    g3.agregarArista(7, 8, 9)
    g3.agregarArista(8, 9, 3)
    g3.agregarArista(8, 10, 6)
    g3.agregarArista(9, 10, 4)
    
    print("\nLa ruta mas rapida mediante el algoritmo Dijkstra junto con su costo es: ")
    g3.dijkstra(1) # 1 es la raíz, en este caso, A
    # Los resultados se expresan de la siguiente forma:
    # [['ruta'], 'peso de la ruta']
    # El numero que está a la derecha del todo es el peso de la ruta, mientras 
    # que la lista de la izquierda es la ruta en sí
    print(g3.camino(1,10)) # El camino se realizará desde el 1 hasta el 11, A-K
    print("\nLos valores finales del grafo son los siguientes: ")
    g3.imprimirGrafo()
    
############################################################################################################