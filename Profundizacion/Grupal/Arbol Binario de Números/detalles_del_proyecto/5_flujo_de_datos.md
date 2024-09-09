# Flujo de datos

**Inicialización:**
La clase Main crea una instancia de ArbolBinarioBusqueda y comienza a insertar valores enteros.

**Inserción de Valores:**
ArbolBinarioBusqueda utiliza el método insertar para recorrer el árbol y encontrar el lugar correcto para cada nuevo valor. La estructura del árbol se mantiene ordenada.

**Filtrado de Números Primos:**
El método obtenerPrimosEnOrdenDecreciente recorre el árbol, filtra los números primos, y los almacena en una lista. Esta lista se ordena en orden descendente utilizando la clase Collections.

**Impresión:**
Finalmente, el método imprimirPrimosEnOrdenDecreciente de ArbolBinarioBusqueda imprime los números primos en orden decreciente en la consola.

## Diagrama de componentes 

```
+-------------------------+       +-------------------------+
|        Main.java         |      |   ArbolBinarioBusqueda  |
|--------------------------|      |-------------------------|
| - Crear instancia árbol  | ---> | - insertar(int valor)   |
| - Insertar valores       |      | - obtenerPrimosEnOrden  |
| - Imprimir primos        |      | - imprimirPrimos        |
+--------------------------+      +-------------------------+
                                               |
                                               v
                                     +-------------------+
                                     |     Nodo.java     |
                                     |-------------------|
                                     | - valor (int)     |
                                     | - izquierdo (Nodo)|
                                     | - derecho (Nodo)  |
                                     +-------------------+

```