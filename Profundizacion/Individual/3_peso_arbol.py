class NodoArbol:
    """
    Clase que representa un nodo en un árbol.

    Atributos:
    -----------
    valor : int o float
        El valor almacenado en el nodo.
    hijos : list[NodoArbol]
        Lista de nodos que son hijos de este nodo.
    """

    def __init__(self, valor):
        """
        Constructor para inicializar un nodo del árbol.

        Parámetros:
        -----------
        valor : int o float
            El valor que será almacenado en el nodo.
        """
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, nodo_hijo: 'NodoArbol') -> None:
        """
        Método para agregar un hijo a este nodo.

        Parámetros:
        -----------
        nodo_hijo : NodoArbol
            El nodo que será añadido como hijo.

        Retorna:
        --------
        None

        Lanza:
        -------
        ValueError:
            Si el nodo hijo es None.
        """
        if nodo_hijo is None:
            raise ValueError("El nodo hijo no puede ser None.")
        self.hijos.append(nodo_hijo)

    def agregar_hijos_binarios(self, izquierdo: 'NodoArbol' = None, derecho: 'NodoArbol' = None) -> None:
        """
        Método específico para agregar hijos izquierdo y derecho en un árbol binario.

        Parámetros:
        -----------
        izquierdo : NodoArbol, opcional
            El nodo que será añadido como hijo izquierdo.
        derecho : NodoArbol, opcional
            El nodo que será añadido como hijo derecho.

        Retorna:
        --------
        None

        Lanza:
        -------
        TypeError:
            Si alguno de los nodos proporcionados no es una instancia de NodoArbol o None.
        """
        if izquierdo and not isinstance(izquierdo, NodoArbol):
            raise TypeError("El hijo izquierdo debe ser una instancia de NodoArbol o None.")
        if derecho and not isinstance(derecho, NodoArbol):
            raise TypeError("El hijo derecho debe ser una instancia de NodoArbol o None.")
        if izquierdo:
            self.agregar_hijo(izquierdo)
        if derecho:
            self.agregar_hijo(derecho)

    def __str__(self):
        return str(self.valor)

    def __repr__(self):
        return f'NodoArbol(valor={self.valor!r}, hijos={len(self.hijos)})'


def peso_arbol(nodo: NodoArbol) -> float:
    """
    Función recursiva para calcular el peso de un árbol.

    Parámetros:
    -----------
    nodo : NodoArbol
        El nodo raíz del árbol o subárbol cuyo peso se quiere calcular.

    Retorna:
    --------
    float
        El peso total del árbol, que es la suma de los valores de todos los nodos.
        Si el árbol está vacío, retorna 0.
    """
    if nodo is None:
        return 0.0
    else:
        # El peso del nodo actual más el peso de todos los nodos hijos
        return nodo.valor + sum(peso_arbol(hijo) for hijo in nodo.hijos)


if __name__ == "__main__":
    """
    Ejemplo de uso de la clase NodoArbol y de la función peso_arbol.
    Este bloque de código se ejecutará solo si el script se ejecuta directamente,
    no si se importa como un módulo.
    """

    # Crear nodos del árbol general
    raiz = NodoArbol(10)
    nodo1 = NodoArbol(5)
    nodo2 = NodoArbol(15)
    nodo3 = NodoArbol(3)
    nodo4 = NodoArbol(7)

    # Construir el árbol general
    raiz.agregar_hijo(nodo1)
    raiz.agregar_hijo(nodo2)
    nodo1.agregar_hijo(nodo3)
    nodo1.agregar_hijo(nodo4)

    # Calcular el peso del árbol
    print("Peso del árbol:", peso_arbol(raiz))
