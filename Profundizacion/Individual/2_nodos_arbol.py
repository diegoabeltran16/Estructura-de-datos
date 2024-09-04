class NodoArbol:
    """
    Clase que representa un nodo en un árbol.

    Atributos:
    -----------
    valor : cualquier tipo de dato
        El valor almacenado en el nodo.
    hijos : list[NodoArbol]
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
        """
        Retorna una representación en forma de cadena del valor del nodo.

        Retorna:
        --------
        str
            El valor del nodo como una cadena.
        """
        return str(self.valor)

    def __repr__(self):
        """
        Retorna una representación más detallada del nodo, incluyendo el valor y el número de hijos.

        Retorna:
        --------
        str
            Representación detallada del nodo.
        """
        return f'NodoArbol(valor={self.valor!r}, hijos={len(self.hijos)})'


def contar_nodos(nodo: NodoArbol) -> int:
    """
    Función recursiva para calcular el número de nodos en un árbol.

    Parámetros:
    -----------
    nodo : NodoArbol
        El nodo raíz del árbol o subárbol cuyo número de nodos se quiere calcular.

    Retorna:
    --------
    int
        El número total de nodos en el árbol.
        Si el árbol está vacío, retorna 0.
    """
    if nodo is None:
        return 0
    else:
        return 1 + sum(contar_nodos(hijo) for hijo in nodo.hijos)


def altura_arbol(nodo: NodoArbol) -> int:
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


def imprimir_arbol(nodo: NodoArbol, nivel: int = 0) -> None:
    """
    Función recursiva para imprimir un árbol en una representación en forma de árbol.

    Parámetros:
    -----------
    nodo : NodoArbol
        El nodo raíz del árbol o subárbol a imprimir.
    nivel : int, opcional
        El nivel actual en el árbol, usado para la indentación. Por defecto es 0.

    Retorna:
    --------
    None
    """
    if nodo is not None:
        print(' ' * (nivel * 4) + str(nodo))
        for hijo in nodo.hijos:
            imprimir_arbol(hijo, nivel + 1)


if __name__ == "__main__":
    """
    Ejemplo de uso de la clase NodoArbol y de las funciones contar_nodos, altura_arbol e imprimir_arbol.
    Este bloque de código se ejecutará solo si el script se ejecuta directamente,
    no si se importa como un módulo.
    """

    # Crear nodos del árbol general
    raiz = NodoArbol("raíz")
    nodo1 = NodoArbol("nodo1")
    nodo2 = NodoArbol("nodo2")
    nodo3 = NodoArbol("nodo3")
    nodo4 = NodoArbol("nodo4")

    # Construir el árbol general
    raiz.agregar_hijo(nodo1)
    raiz.agregar_hijo(nodo2)
    nodo1.agregar_hijo(nodo3)
    nodo3.agregar_hijo(nodo4)

    # Imprimir el árbol
    print("Estructura del árbol general:")
    imprimir_arbol(raiz)

    # Calcular el número de nodos del árbol
    print("Número de nodos en el árbol general:", contar_nodos(raiz))

    # Calcular la altura del árbol
    print("Altura del árbol general:", altura_arbol(raiz))

    # Crear un árbol binario con el mismo enfoque
    raiz_binario = NodoArbol("raíz_binario")
    nodo_izq = NodoArbol("izquierdo")
    nodo_der = NodoArbol("derecho")
    nodo_izq_izq = NodoArbol("izquierdo_izquierdo")
    nodo_izq_derecho = NodoArbol("izquierdo_derecho")

    raiz_binario.agregar_hijos_binarios(izquierdo=nodo_izq, derecho=nodo_der)
    nodo_izq.agregar_hijos_binarios(izquierdo=nodo_izq_izq, derecho=nodo_izq_derecho)

    # Imprimir el árbol binario
    print("\nEstructura del árbol binario:")
    imprimir_arbol(raiz_binario)

    # Calcular el número de nodos del árbol binario
    print("Número de nodos en el árbol binario:", contar_nodos(raiz_binario))

    # Calcular la altura del árbol binario
    print("Altura del árbol binario:", altura_arbol(raiz_binario))
