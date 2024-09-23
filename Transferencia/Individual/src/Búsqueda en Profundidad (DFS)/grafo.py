# grafo.py

from collections import deque

class Grafo:
    """
    Clase que representa un Grafo utilizando listas de adyacencia.
    Permite la construcción de grafos, la adición de aristas y la realización de
    recorridos utilizando los algoritmos de Búsqueda en Amplitud (BFS) y Búsqueda en Profundidad (DFS).
    """

    def __init__(self):
        """
        Inicializa una instancia del grafo con un diccionario vacío.
        """
        self.grafo = {}

    def agregar_arista(self, nodo1, nodo2):
        """
        Añade una arista entre dos nodos en el grafo.
        """
        if nodo1 not in self.grafo:
            self.grafo[nodo1] = []
        if nodo2 not in self.grafo:
            self.grafo[nodo2] = []
        self.grafo[nodo1].append(nodo2)
        self.grafo[nodo2].append(nodo1)  # Asume que el grafo es no dirigido

    def bfs(self, nodo_inicial):
        """
        Realiza un recorrido en amplitud (BFS) a partir de un nodo inicial.
        """
        visitados = set()
        cola = deque([nodo_inicial])
        visitados.add(nodo_inicial)

        while cola:
            nodo_actual = cola.popleft()
            print(nodo_actual, end=" ")

            for vecino in self.grafo[nodo_actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
    
    def dfs(self, nodo_inicial):
        """
        Realiza un recorrido en profundidad (DFS) a partir de un nodo inicial.
        
        Parámetros:
            nodo_inicial: El nodo desde donde se iniciará el recorrido DFS.
        
        Detalles de implementación:
            - Utiliza un conjunto 'visitados' para rastrear los nodos ya visitados.
            - Utiliza una lista como pila para manejar el orden de visita de los nodos.
            - Recorre todos los vecinos de cada nodo, marcándolos como visitados y
              añadiéndolos a la pila para su posterior exploración.
        
        Complejidad Temporal: O(V + E), donde V es el número de vértices y E el número de aristas.
        """
        visitados = set()
        pila = [nodo_inicial]  # Utilizamos una lista como pila

        while pila:
            nodo_actual = pila.pop()  # Extraemos el último elemento (último en entrar, primero en salir)
            if nodo_actual not in visitados:
                print(nodo_actual, end=" ")
                visitados.add(nodo_actual)
                
                # Añadir los vecinos no visitados a la pila
                for vecino in reversed(self.grafo[nodo_actual]):  # Usamos reversed para mantener el orden de visita
                    if vecino not in visitados:
                        pila.append(vecino)
