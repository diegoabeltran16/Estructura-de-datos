package Palabras;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Clase ArbolBinarioPalabras que gestiona la inserción de palabras en un árbol binario de búsqueda.
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

    private void recorrerArbol(NodoPalabra nodo, List<NodoPalabra> palabras) {
        if (nodo != null) {
            recorrerArbol(nodo.izquierdo, palabras); // Recorrer el subárbol izquierdo
            palabras.add(nodo); // Agregar la palabra actual a la lista
            recorrerArbol(nodo.derecho, palabras); // Recorrer el subárbol derecho
        }
    }

    /**
     * Método para imprimir las palabras ordenadas por frecuencia de aparición.
     * Se imprime una tabla con las palabras y su frecuencia.
     */
    public void imprimirPalabrasPorFrecuencia() {
        List<NodoPalabra> palabras = obtenerPalabrasPorFrecuencia();

        // Encabezado
        System.out.println("==================================");
        System.out.println(" Palabras ordenadas por frecuencia");
        System.out.println("==================================");
        System.out.printf("%-15s %10s\n", "Palabra", "Frecuencia");

        for (NodoPalabra np : palabras) {
            // Formatear la salida: palabra y su frecuencia
            System.out.printf("%-15s %10d\n", np.palabra, np.frecuencia);
        }

        System.out.println("==================================");
    }
}
