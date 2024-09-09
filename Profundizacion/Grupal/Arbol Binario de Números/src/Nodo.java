/**
 * Clase Nodo que representa un nodo en un árbol binario de búsqueda.
 * Esta clase contiene el valor del nodo y referencias a sus hijos izquierdo y derecho.
 */
public class Nodo {

    // Valor almacenado en el nodo
    int valor;

    // Referencias a los hijos izquierdo y derecho del nodo
    Nodo izquierdo, derecho;

    /**
     * Constructor para inicializar un nodo con un valor dado.
     * Los hijos izquierdo y derecho se inicializan en null.
     *
     * @param item el valor que será almacenado en el nodo
     */
    public Nodo(int item) {
        this.valor = item;
        this.izquierdo = null;
        this.derecho = null;
    }
}
