# main.py

from grafo import Grafo

def main():
    """
    Función principal que demuestra la construcción y recorrido de un grafo
    utilizando la clase Grafo y los algoritmos de Búsqueda en Amplitud (BFS) y
    Búsqueda en Profundidad (DFS).
    """
    grafo = Grafo()
    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(1, 3)
    grafo.agregar_arista(2, 4)
    grafo.agregar_arista(2, 5)
    grafo.agregar_arista(3, 6)
    grafo.agregar_arista(3, 7)

    print("Recorrido BFS desde el nodo 1:")
    grafo.bfs(1)
    print("\nRecorrido DFS desde el nodo 1:")
    grafo.dfs(1)

if __name__ == "__main__":
    main()
