# main.py

from grafo import Grafo

def main():
    """
    Función principal que interactúa con la clase Grafo para demostrar la funcionalidad del Tipo Abstracto de Dato (TAD).
    - Crea un grafo vacío.
    - Inserta nodos y aristas.
    - Verifica si el grafo está vacío.
    - Busca nodos en el grafo.
    - Muestra la estructura del grafo.
    """
    # Crear un grafo vacío
    grafo = Grafo()
    
    # Verificar si el grafo está vacío
    print("¿El grafo está vacío?", grafo.esta_vacio())  # Esperado: True

    # Insertar nodos
    grafo.insertar_nodo(1)
    grafo.insertar_nodo(2)
    grafo.insertar_nodo(3)
    
    # Insertar aristas
    grafo.insertar_arista(1, 2)
    grafo.insertar_arista(1, 3)
    grafo.insertar_arista(2, 3)

    # Mostrar el grafo
    print("\nEstructura del grafo:")
    grafo.mostrar_grafo()
    
    # Buscar nodos
    print("\n¿El nodo 2 existe en el grafo?", grafo.buscar_nodo(2))  # Esperado: True
    print("¿El nodo 4 existe en el grafo?", grafo.buscar_nodo(4))    # Esperado: False
    
    # Verificar si el grafo está vacío
    print("\n¿El grafo está vacío?", grafo.esta_vacio())  # Esperado: False

if __name__ == "__main__":
    main()
