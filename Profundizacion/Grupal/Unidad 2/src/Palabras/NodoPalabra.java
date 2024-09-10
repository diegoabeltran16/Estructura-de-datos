package Palabras;

/**
 * Clase Palabras.NodoPalabra que representa un nodo en un árbol binario de búsqueda.
 * Cada nodo contiene una palabra y la frecuencia de aparición de esa palabra en el archivo.
 */
public class NodoPalabra {

    // Atributos del nodo
    String palabra; // La palabra almacenada en el nodo
    int frecuencia; // Frecuencia de aparición de la palabra
    NodoPalabra izquierdo, derecho; // Referencias a los nodos hijos izquierdo y derecho

    /**
     * Constructor para inicializar un nodo con una palabra.
     * Establece la frecuencia inicial en 1 y los hijos en null.
     *
     * @param palabra la palabra que será almacenada en el nodo.
     */
    public NodoPalabra(String palabra) {
        this.palabra = palabra;
        this.frecuencia = 1;
        this.izquierdo = null;
        this.derecho = null;
    }

    /**
     * Método para incrementar la frecuencia de aparición de la palabra en el nodo.
     * Incrementa el contador de frecuencia en 1 cada vez que la palabra aparece de nuevo.
     */
    public void incrementarFrecuencia() {
        this.frecuencia++;
    }
}
