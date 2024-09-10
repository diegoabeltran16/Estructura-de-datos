package Palabras;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Clase Palabras.ArbolBinarioPalabras que gestiona la inserción de palabras en un árbol binario de búsqueda.
 * También permite mostrar las palabras ordenadas por la frecuencia de aparición de mayor a menor.
 */
public class ArbolBinarioPalabras {

    // Raíz del árbol binario de búsqueda
    NodoPalabra raiz;

    /**
     * Método para insertar una palabra en el árbol binario de búsqueda.
     * Si la palabra ya existe, incrementa su frecuencia.
     *
     * @param palabra la palabra que será insertada en el árbol.
     */
    public void insertar(String palabra) {
        raiz = insertarRecursivo(raiz, palabra);
    }

    /**
     * Método recursivo para insertar una palabra en el árbol binario de búsqueda.
     * Inserta la palabra en la posición correcta, respetando el orden alfabético.
     * Si la palabra ya existe en el árbol, se incrementa su frecuencia.
     *
     * @param nodo el nodo actual que se está evaluando.
     * @param palabra la palabra que se desea insertar.
     * @return el nodo raíz actualizado.
     */
    private NodoPalabra insertarRecursivo(NodoPalabra nodo, String palabra) {
        if (nodo == null) {
            return new NodoPalabra(palabra); // Crear un nuevo nodo si no existe en el árbol
        }

        int comparacion = palabra.compareTo(nodo.palabra); // Comparar las palabras alfabéticamente

        if (comparacion < 0) {
            nodo.izquierdo = insertarRecursivo(nodo.izquierdo, palabra); // Insertar en el subárbol izquierdo
        } else if (comparacion > 0) {
            nodo.derecho = insertarRecursivo(nodo.derecho, palabra); // Insertar en el subárbol derecho
        } else {
            nodo.incrementarFrecuencia(); // Incrementar la frecuencia si la palabra ya existe
        }

        return nodo;
    }

    /**
     * Método para obtener una lista de palabras almacenadas en el árbol, ordenadas por su frecuencia.
     *
     * @return una lista de las palabras ordenadas por frecuencia de aparición.
     */
    public List<NodoPalabra> obtenerPalabrasPorFrecuencia() {
        List<NodoPalabra> palabras = new ArrayList<>();
        recorrerArbol(raiz, palabras);

        // Ordenar las palabras por frecuencia de mayor a menor
        palabras.sort(Comparator.comparingInt((NodoPalabra np) -> np.frecuencia).reversed());
        return palabras;
    }

    /**
     * Método recursivo que recorre el árbol binario y agrega las palabras y sus frecuencias a una lista.
     *
     * @param nodo el nodo actual que se está evaluando.
     * @param palabras la lista donde se almacenan las palabras y sus frecuencias.
     */
    private void recorrerArbol(NodoPalabra nodo, List<NodoPalabra> palabras) {
        if (nodo != null) {
            recorrerArbol(nodo.izquierdo, palabras); // Recorrer el subárbol izquierdo
            palabras.add(nodo); // Agregar la palabra actual a la lista
            recorrerArbol(nodo.derecho, palabras); // Recorrer el subárbol derecho
        }
    }

    /**
     * Método que imprime las palabras almacenadas en el árbol, ordenadas por frecuencia de mayor a menor.
     */
    public void imprimirPalabrasPorFrecuencia() {
        List<NodoPalabra> palabras = obtenerPalabrasPorFrecuencia();
        for (NodoPalabra np : palabras) {
            System.out.println(np.palabra + ": " + np.frecuencia);
        }
    }
}
