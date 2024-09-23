# Importa la biblioteca deque de collections para el manejo eficiente de colas
from collections import deque

class Grafo:
    """
    Clase que representa un Grafo utilizando listas de adyacencia.
    Permite la construcción de grafos, la adición de aristas y la realización de
    recorridos utilizando el algoritmo de Búsqueda en Amplitud (BFS).
    """

    def __init__(self):
        """
        Inicializa una instancia del grafo con un diccionario vacío.
        El diccionario almacenará los nodos y sus listas de adyacencia.
        Complejidad Temporal: O(1)
        """
        self.grafo = {}

    def agregar_arista(self, nodo1, nodo2):
        """
        Añade una arista entre dos nodos en el grafo.
        Si los nodos no existen, se inicializan en el diccionario.
        
        Parámetros:
            nodo1: El nodo de origen de la arista.
            nodo2: El nodo de destino de la arista.
        
        Detalles de implementación:
            Se verifica la existencia de cada nodo en el diccionario y se agregan a sus listas
            de adyacencia respectivas para representar la conexión.
        
        Complejidad Temporal: O(1) en promedio.
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
        
        Parámetros:
            nodo_inicial: El nodo desde donde se iniciará el recorrido BFS.
        
        Detalles de implementación:
            - Utiliza un conjunto 'visitados' para rastrear los nodos ya visitados.
            - Utiliza una 'deque' como cola para manejar el orden de visita de los nodos.
            - Recorre todos los vecinos de cada nodo, marcándolos como visitados y
              añadiéndolos a la cola para su posterior exploración.
        
        Complejidad Temporal: O(V + E), donde V es el número de vértices y E el número de aristas.
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
