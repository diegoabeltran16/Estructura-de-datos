import sys
sys.path.append('c:/Users/diego_dx9e5pi/OneDrive/Documents/Git Repos/Estructura-de-datos/Transferencia/Individual/src/1')

from grafo import Grafo

def main():
    """
    Función principal que demuestra la construcción y recorrido de un grafo
    utilizando la clase Grafo y el algoritmo de Búsqueda en Amplitud (BFS).
    
    - Crea una instancia de la clase Grafo.
    - Añade aristas que forman un grafo no dirigido.
    - Realiza un recorrido BFS a partir del nodo 1 y muestra el resultado.
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

if __name__ == "__main__":
    main()
