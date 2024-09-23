# grafo.py

class Grafo:
    """
    Clase que representa un grafo utilizando listas de adyacencia y que implementa un Tipo Abstracto de Dato (TAD).
    Permite la creación de un grafo vacío, la inserción de nodos y aristas, la verificación de si el grafo está vacío
    y la búsqueda de nodos.
    """

    def __init__(self):
        """
        Inicializa un grafo vacío utilizando un diccionario para almacenar las listas de adyacencia.
        Cada clave en el diccionario representa un nodo, y el valor es una lista de nodos adyacentes.
        
        Complejidad Temporal: O(1)
        """
        self.grafo = {}

    def insertar_nodo(self, nodo):
        """
        Inserta un nodo en el grafo. Si el nodo ya existe, no se realiza ninguna acción.
        
        Parámetros:
            nodo: El nodo que se desea insertar en el grafo.
        
        Complejidad Temporal: O(1)
        """
        if nodo not in self.grafo:
            self.grafo[nodo] = []
    
    def insertar_arista(self, nodo1, nodo2):
        """
        Inserta una arista entre dos nodos. Si los nodos no existen, se insertan primero en el grafo.
        
        Parámetros:
            nodo1: El primer nodo que formará la arista.
            nodo2: El segundo nodo que formará la arista.
        
        Complejidad Temporal: O(1) en promedio
        """
        if nodo1 not in self.grafo:
            self.insertar_nodo(nodo1)
        if nodo2 not in self.grafo:
            self.insertar_nodo(nodo2)
        
        # Añadir la arista en ambas direcciones para un grafo no dirigido
        if nodo2 not in self.grafo[nodo1]:
            self.grafo[nodo1].append(nodo2)
        if nodo1 not in self.grafo[nodo2]:
            self.grafo[nodo2].append(nodo1)
    
    def esta_vacio(self):
        """
        Verifica si el grafo está vacío.
        
        Retorna:
            True si el grafo no contiene nodos, False en caso contrario.
        
        Complejidad Temporal: O(1)
        """
        return len(self.grafo) == 0
    
    def buscar_nodo(self, nodo):
        """
        Busca un nodo en el grafo.
        
        Parámetros:
            nodo: El nodo que se desea buscar.
        
        Retorna:
            True si el nodo existe en el grafo, False en caso contrario.
        
        Complejidad Temporal: O(1)
        """
        return nodo in self.grafo
    
    def mostrar_grafo(self):
        """
        Muestra la estructura del grafo, indicando los nodos y sus conexiones (adyacencias).
        
        Complejidad Temporal: O(V + E), donde V es el número de nodos y E es el número de aristas.
        """
        for nodo in self.grafo:
            print(f"{nodo}: {self.grafo[nodo]}")
