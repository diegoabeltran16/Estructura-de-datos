package Numeros;

/**
 * Clase principal que contiene el método main.
 * Aquí se crean instancias del árbol binario de búsqueda, se insertan números y
 * se imprimen los números primos en orden decreciente.
 */
public class Main {

    /**
     * Método principal del programa. Inserta números en el árbol binario de búsqueda
     * y luego imprime los números primos en orden decreciente.
     *
     * @param args los argumentos de línea de comandos (no se utilizan en este programa)
     */
    public static void main(String[] args) {
        // Crear una instancia del árbol binario de búsqueda
        ArbolBinarioBusqueda arbol = new ArbolBinarioBusqueda();

        // Insertar una serie de números en el árbol
        arbol.insertar(10);
        arbol.insertar(5);
        arbol.insertar(3);
        arbol.insertar(7);
        arbol.insertar(15);
        arbol.insertar(17);
        arbol.insertar(2);

        // Imprimir los números primos en orden decreciente
        arbol.imprimirPrimosEnOrdenDecreciente();
    }
}
