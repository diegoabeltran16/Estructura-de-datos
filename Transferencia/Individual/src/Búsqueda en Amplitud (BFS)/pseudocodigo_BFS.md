# Pseudocodigo para desarrollar el código en Python del BFS

## Grafo

"""
Clase Grafo:
    
    Clase que representa un Grafo utilizando listas de adyacencia.
    Permite la construcción de grafos, la adición de aristas y la realización de
    recorridos utilizando el algoritmo de Búsqueda en Amplitud (BFS).
    

    Método inicializar():
        """
        Inicializa un grafo vacío utilizando un diccionario para almacenar las listas de adyacencia.
        Cada clave del diccionario representa un nodo y su valor es una lista de nodos adyacentes.
        
        Complejidad Temporal: O(1)
        """
        grafo = diccionario vacío

    Método agregar_arista(nodo1, nodo2):
        """
        Añade una arista entre dos nodos en el grafo.
        Si los nodos no existen, se insertan como claves en el diccionario con listas vacías.
        
        Parámetros:
            nodo1: El nodo de origen de la arista.
            nodo2: El nodo de destino de la arista.
        
        Detalles de implementación:
            Verificar la existencia de nodo1 y nodo2 en el diccionario.
            Si no existen, se inicializan con listas vacías.
            Se añade nodo2 a la lista de adyacencia de nodo1 y viceversa, asumiendo un grafo no dirigido.
        
        Complejidad Temporal: O(1) en promedio
        """
        si nodo1 no está en grafo:
            grafo[nodo1] = lista vacía
        si nodo2 no está en grafo:
            grafo[nodo2] = lista vacía
        
        añadir nodo2 a la lista de grafo[nodo1]
        añadir nodo1 a la lista de grafo[nodo2]  # Asume que el grafo es no dirigido

    Método bfs(nodo_inicial):
        """
        Realiza un recorrido en amplitud (BFS) a partir de un nodo inicial.
        
        Parámetros:
            nodo_inicial: El nodo desde donde se iniciará el recorrido BFS.
        
        Detalles de implementación:
            - Utiliza un conjunto 'visitados' para rastrear los nodos ya visitados.
            - Utiliza una estructura de datos tipo cola para manejar el orden de visita de los nodos.
            - Recorre todos los vecinos de cada nodo, marcándolos como visitados y añadiéndolos a la cola para su posterior exploración.
        
        Complejidad Temporal: O(V + E), donde V es el número de vértices y E el número de aristas.
        """
        visitados = conjunto vacío
        cola = cola con nodo_inicial
        añadir nodo_inicial a visitados

        mientras la cola no esté vacía:
            nodo_actual = extraer el primer elemento de la cola
            imprimir nodo_actual

            para cada vecino en la lista de grafo[nodo_actual]:
                si vecino no está en visitados:
                    añadir vecino a visitados
                    añadir vecino a la cola

"""

## main

"""
Función principal main():
    """
    Función principal que demuestra la construcción y recorrido de un grafo
    utilizando la clase Grafo y el algoritmo de Búsqueda en Amplitud (BFS).
    
    - Crea una instancia de la clase Grafo.
    - Añade aristas que forman un grafo no dirigido.
    - Realiza un recorrido BFS a partir del nodo 1 y muestra el resultado.
    """
    
    Crear una instancia de la clase Grafo llamada grafo
    
    # Añadir aristas al grafo
    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(1, 3)
    grafo.agregar_arista(2, 4)
    grafo.agregar_arista(2, 5)
    grafo.agregar_arista(3, 6)
    grafo.agregar_arista(3, 7)

    # Realizar el recorrido BFS e imprimir el resultado
    imprimir "Recorrido BFS desde el nodo 1:"
    grafo.bfs(1)

Si este es el módulo principal a ejecutar, entonces llamar a main()

"""