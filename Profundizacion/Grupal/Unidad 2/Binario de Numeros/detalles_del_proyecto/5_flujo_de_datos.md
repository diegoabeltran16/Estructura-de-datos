# Flujo de datos

**Inicialización:**
La clase Numeros.Palabras.Main crea una instancia de Numeros.ArbolBinarioBusqueda y comienza a insertar valores enteros.

**Inserción de Valores:**
Numeros.ArbolBinarioBusqueda utiliza el método insertar para recorrer el árbol y encontrar el lugar correcto para cada nuevo valor. La estructura del árbol se mantiene ordenada.

**Filtrado de Números Primos:**
El método obtenerPrimosEnOrdenDecreciente recorre el árbol, filtra los números primos, y los almacena en una lista. Esta lista se ordena en orden descendente utilizando la clase Collections.

**Impresión:**
Finalmente, el método imprimirPrimosEnOrdenDecreciente de Numeros.ArbolBinarioBusqueda imprime los números primos en orden decreciente en la consola.

## Diagrama de componentes 

```
+-------------------------+       +-------------------------+
|        Numeros.Palabras.Main.java         |      |   Numeros.ArbolBinarioBusqueda  |
|--------------------------|      |-------------------------|
| - Crear instancia árbol  | ---> | - insertar(int valor)   |
| - Insertar valores       |      | - obtenerPrimosEnOrden  |
| - Imprimir primos        |      | - imprimirPrimos        |
+--------------------------+      +-------------------------+
                                               |
                                               v
                                     +-------------------+
                                     |     Numeros.Nodo.java     |
                                     |-------------------|
                                     | - valor (int)     |
                                     | - izquierdo (Numeros.Nodo)|
                                     | - derecho (Numeros.Nodo)  |
                                     +-------------------+

```