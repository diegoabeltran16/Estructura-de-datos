class NodoArbol:
    """
    Clase que representa un nodo en un árbol. Puede ser usado tanto para árboles generales como binarios.

    Atributos:
    -----------
    valor : cualquier tipo de dato
        El valor almacenado en el nodo.
    hijos : lista de NodoArbol
        Lista de nodos que son hijos de este nodo.
    """

    def __init__(self, valor):
        """
        Constructor para inicializar un nodo del árbol.

        Parámetros:
        -----------
        valor : cualquier tipo de dato
            El valor que será almacenado en el nodo.
        """
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        """
        Método para agregar un hijo a este nodo.

        Parámetros:
        -----------
        nodo_hijo : NodoArbol
            El nodo que será añadido como hijo.
        """
        self.hijos.append(nodo_hijo)

    def agregar_hijos_binarios(self, izquierdo=None, derecho=None):
        """
        Método específico para agregar hijos izquierdo y derecho en un árbol binario.

        Parámetros:
        -----------
        izquierdo : NodoArbol, opcional
            El nodo que será añadido como hijo izquierdo.
        derecho : NodoArbol, opcional
            El nodo que será añadido como hijo derecho.
        """
        if izquierdo:
            self.agregar_hijo(izquierdo)
        if derecho:
            self.agregar_hijo(derecho)

def altura_arbol(nodo):
    """
    Función recursiva para calcular la altura de un árbol.

    Parámetros:
    -----------
    nodo : NodoArbol
        El nodo raíz del árbol o subárbol cuya altura se quiere calcular.

    Retorna:
    --------
    int
        La altura del árbol (número máximo de niveles desde la raíz hasta una hoja).
        Si el árbol está vacío, retorna -1.
    """
    if nodo is None:
        return -1
    elif not nodo.hijos:
        return 0
    else:
        alturas_hijos = [altura_arbol(hijo) for hijo in nodo.hijos]
        return 1 + max(alturas_hijos)


if __name__ == "__main__":
    # Crear nodos del árbol general
    raiz = NodoArbol("raíz")
    nodo1 = NodoArbol("nodo1")
    nodo2 = NodoArbol("nodo2")
    nodo3 = NodoArbol("nodo3")
    nodo4 = NodoArbol("nodo4")

    # Construir un árbol general
    raiz.agregar_hijo(nodo1)
    raiz.agregar_hijo(nodo2)
    nodo1.agregar_hijo(nodo3)
    nodo3.agregar_hijo(nodo4)

    # Calcular la altura del árbol general
    print("Altura del árbol general:", altura_arbol(raiz))

    # Construir un árbol binario con el mismo enfoque
    raiz_binario = NodoArbol("raíz")
    nodo_izq = NodoArbol("izquierdo")
    nodo_der = NodoArbol("derecho")
    nodo_izq_izq = NodoArbol("izquierdo_izquierdo")
    nodo_izq_derecho = NodoArbol("izquierdo_derecho")

    raiz_binario.agregar_hijos_binarios(izquierdo=nodo_izq, derecho=nodo_der)
    nodo_izq.agregar_hijos_binarios(izquierdo=nodo_izq_izq, derecho=nodo_izq_derecho)

    # Calcular la altura del árbol binario
    print("Altura del árbol binario:", altura_arbol(raiz_binario))
