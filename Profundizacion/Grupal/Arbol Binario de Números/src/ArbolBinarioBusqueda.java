import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Clase ArbolBinarioBusqueda que contiene la lógica para insertar valores,
 * filtrar números primos, y reordenarlos en un árbol binario de búsqueda.
 */
public class ArbolBinarioBusqueda {

    // La raíz del árbol binario de búsqueda
    Nodo raiz;

    /**
     * Método para insertar un valor en el árbol binario de búsqueda.
     * Se garantiza que el valor se inserta en el lugar correcto para mantener el orden ascendente.
     *
     * @param valor el valor entero que se desea insertar en el árbol
     */
    public void insertar(int valor) {
        raiz = insertarRecursivo(raiz, valor);
    }

    /**
     * Método recursivo que inserta un valor en el árbol binario de búsqueda.
     * Inserta el valor en el lugar adecuado según las reglas del árbol binario de búsqueda.
     *
     * @param raiz el nodo raíz desde donde comenzar la inserción
     * @param valor el valor que se desea insertar
     * @return el nodo raíz actualizado
     */
    private Nodo insertarRecursivo(Nodo raiz, int valor) {
        if (raiz == null) {
            return new Nodo(valor); // Crear un nuevo nodo si el árbol está vacío
        }

        if (valor < raiz.valor) {
            raiz.izquierdo = insertarRecursivo(raiz.izquierdo, valor); // Insertar en el subárbol izquierdo
        } else if (valor > raiz.valor) {
            raiz.derecho = insertarRecursivo(raiz.derecho, valor); // Insertar en el subárbol derecho
        }

        return raiz; // Devolver la raíz actualizada
    }

    /**
     * Método que obtiene los números primos almacenados en el árbol binario de búsqueda,
     * y los devuelve en una lista ordenada de mayor a menor.
     *
     * @return una lista de números primos en orden decreciente
     */
    public List<Integer> obtenerPrimosEnOrdenDecreciente() {
        List<Integer> primos = new ArrayList<>();
        obtenerPrimosRecursivo(raiz, primos);

        // Ordenar los números primos en orden decreciente
        Collections.sort(primos, Collections.reverseOrder());
        return primos;
    }

    /**
     * Método recursivo que recorre el árbol binario de búsqueda, identificando
     * los números primos y agregándolos a la lista de números primos.
     *
     * @param nodo el nodo actual que se está evaluando
     * @param primos la lista donde se almacenan los números primos encontrados
     */
    private void obtenerPrimosRecursivo(Nodo nodo, List<Integer> primos) {
        if (nodo != null) {
            obtenerPrimosRecursivo(nodo.izquierdo, primos); // Recorrer el subárbol izquierdo

            if (esPrimo(nodo.valor)) {
                primos.add(nodo.valor); // Agregar a la lista si el número es primo
            }

            obtenerPrimosRecursivo(nodo.derecho, primos); // Recorrer el subárbol derecho
        }
    }

    /**
     * Método para verificar si un número es primo.
     * Un número es primo si solo es divisible por 1 y por sí mismo.
     *
     * @param numero el número a verificar
     * @return true si el número es primo, false si no lo es
     */
    private boolean esPrimo(int numero) {
        if (numero <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(numero); i++) {
            if (numero % i == 0) {
                return false;
            }
        }
        return true;
    }

    /**
     * Método que imprime los números primos encontrados en el árbol binario de búsqueda,
     * ordenados de mayor a menor.
     */
    public void imprimirPrimosEnOrdenDecreciente() {
        List<Integer> primos = obtenerPrimosEnOrdenDecreciente();
        System.out.println("Números primos en orden decreciente: " + primos);
    }
}
