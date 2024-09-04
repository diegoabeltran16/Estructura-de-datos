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


def son_similares(arbol1: NodoArbol, arbol2: NodoArbol) -> bool:
    """
    Función recursiva para comprobar si dos árboles son similares.

    Parámetros:
    -----------
    arbol1 : NodoArbol
        El nodo raíz del primer árbol.
    arbol2 : NodoArbol
        El nodo raíz del segundo árbol.

    Retorna:
    --------
    bool
        True si los árboles son similares, False en caso contrario.
    """
    # Caso 1: Ambos nodos son None, los árboles son similares
    if arbol1 is None and arbol2 is None:
        return True

    # Caso 2: Uno de los nodos es None y el otro no, los árboles no son similares
    if arbol1 is None or arbol2 is None:
        return False

    # Caso 3: Ambos nodos no son None, se comparan sus hijos
    if len(arbol1.hijos) != len(arbol2.hijos):
        return False

    # Comparar recursivamente los subárboles hijos
    for hijo1, hijo2 in zip(arbol1.hijos, arbol2.hijos):
        if not son_similares(hijo1, hijo2):
            return False

    # Si todos los hijos son similares, entonces los árboles son similares
    return True


if __name__ == "__main__":
    """
    Ejemplo de uso de la clase NodoArbol y de la función son_similares.
    Este bloque de código se ejecutará solo si el script se ejecuta directamente,
    no si se importa como un módulo.
    """

    # Crear nodos de dos árboles similares
    raiz1 = NodoArbol(10)
    nodo1_1 = NodoArbol(5)
    nodo1_2 = NodoArbol(15)
    nodo1_3 = NodoArbol(3)
    nodo1_4 = NodoArbol(7)

    raiz2 = NodoArbol(10)
    nodo2_1 = NodoArbol(5)
    nodo2_2 = NodoArbol(15)
    nodo2_3 = NodoArbol(3)
    nodo2_4 = NodoArbol(7)

    # Construir los árboles similares
    raiz1.agregar_hijo(nodo1_1)
    raiz1.agregar_hijo(nodo1_2)
    nodo1_1.agregar_hijo(nodo1_3)
    nodo1_1.agregar_hijo(nodo1_4)

    raiz2.agregar_hijo(nodo2_1)
    raiz2.agregar_hijo(nodo2_2)
    nodo2_1.agregar_hijo(nodo2_3)
    nodo2_1.agregar_hijo(nodo2_4)

    # Verificar si los árboles son similares
    print("¿Son los árboles similares?:", son_similares(raiz1, raiz2))

    # Crear otro árbol no similar
    raiz3 = NodoArbol(10)
    nodo3_1 = NodoArbol(5)
    nodo3_2 = NodoArbol(20)

    raiz3.agregar_hijo(nodo3_1)
    raiz3.agregar_hijo(nodo3_2)

    # Verificar si los árboles son similares
    print("¿Son el primer y el tercer árbol similares?:", son_similares(raiz1, raiz3))
