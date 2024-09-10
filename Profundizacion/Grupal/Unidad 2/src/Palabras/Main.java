package Palabras;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * Clase principal que lee un archivo de texto y procesa las palabras en un árbol binario de búsqueda.
 * Al final, muestra las palabras almacenadas en el árbol, ordenadas por frecuencia de aparición.
 */
public class Main {

    /**
     * Método principal del programa que coordina la lectura del archivo y la inserción de palabras en el árbol.
     *
     * @param args los argumentos de línea de comandos (no se utilizan en este programa).
     */
    public static void main(String[] args) {
        ArbolBinarioPalabras arbol = new ArbolBinarioPalabras();

        // Imprimir la ruta actual de ejecución para verificar dónde está buscando el archivo
        System.out.println("Ruta de ejecución actual: " + System.getProperty("user.dir"));

        // Leer las palabras desde el archivo de texto
        try (BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\diego_dx9e5pi\\OneDrive\\Documents\\Git Repos\\Estructura-de-datos\\Profundizacion\\Grupal\\Unidad 2\\src\\Palabras\\frase.txt"))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                // Separar palabras por espacios y signos de puntuación
                String[] palabras = linea.split("\\W+");
                for (String palabra : palabras) {
                    if (!palabra.isEmpty()) {
                        arbol.insertar(palabra.toLowerCase()); // Convertir a minúsculas y agregar al árbol
                    }
                }
            }
        } catch (IOException e) {
            System.out.println("Error al leer el archivo: " + e.getMessage());
        }

        // Imprimir las palabras ordenadas por frecuencia de aparición
        arbol.imprimirPalabrasPorFrecuencia();
    }
}
