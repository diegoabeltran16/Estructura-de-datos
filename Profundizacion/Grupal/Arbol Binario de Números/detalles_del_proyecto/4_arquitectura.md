# Arquitectura

El proyecto está compuesto por tres componentes principales que interactúan para lograr el objetivo de gestionar un árbol binario de búsqueda (BST), filtrar números primos y presentarlos en orden decreciente. A continuación se describe la arquitectura del proyecto de manera detallada.

## Nodo.java
**Responsabilidad:** La clase Nodo es la base de la estructura del árbol binario de búsqueda. Representa cada elemento (nodo) del árbol y contiene los atributos necesarios para vincular a sus hijos izquierdo y derecho. Este componente es fundamental para almacenar el valor numérico de cada nodo en el árbol.

**Atributos:**
- int valor: El valor almacenado en el nodo (en este caso, un número entero).
- Nodo izquierdo: Referencia al hijo izquierdo del nodo.
- Nodo derecho: Referencia al hijo derecho del nodo.

**Métodos:**
- Constructor Nodo(int valor): Inicializa el nodo con el valor proporcionado y establece sus referencias a los hijos como null.
- Interacción: La clase Nodo será utilizada por la clase ArbolBinarioBusqueda para crear e interconectar los nodos del árbol. Cada nodo se relaciona con otros nodos mediante sus atributos izquierdo y derecho, formando el árbol binario.

## ArbolBinarioBusqueda.java
**Responsabilidad:** Esta clase contiene la lógica principal del árbol binario de búsqueda. Se encarga de insertar valores, recorrer el árbol, identificar números primos, y reordenar estos números en orden decreciente.

**Atributos:**
- Nodo raiz: La raíz del árbol binario de búsqueda, el punto de entrada del árbol.

**Métodos:**
- void insertar(int valor): Inserta un nuevo valor en el árbol binario de búsqueda, asegurando que se mantenga el orden ascendente (hijos izquierdos menores, hijos derechos mayores).
- Nodo insertarRecursivo(Nodo nodo, int valor): Método recursivo auxiliar que se utiliza para insertar el valor en su lugar correspondiente en el árbol.
- List<Integer> obtenerPrimosEnOrdenDecreciente(): Devuelve una lista de números primos encontrados en el árbol, ordenados de mayor a menor.
- void obtenerPrimosRecursivo(Nodo nodo, List<Integer> primos): Método recursivo que recorre el árbol en busca de números primos y los agrega a la lista proporcionada.
- boolean esPrimo(int numero): Verifica si un número es primo, realizando divisiones hasta la raíz cuadrada del número para comprobar su divisibilidad.
- void imprimirPrimosEnOrdenDecreciente(): Imprime los números primos en orden decreciente.
- Interacción: ArbolBinarioBusqueda interactúa directamente con Nodo para construir el árbol binario y gestionar los enlaces entre nodos. Esta clase también interactúa con la clase Main al proporcionar los métodos para insertar y procesar los números del árbol.

## Main.java
**Responsabilidad:** La clase Main es el punto de entrada del programa. Su responsabilidad es coordinar la ejecución del código, permitiendo que el usuario cree el árbol binario de búsqueda, inserte los valores, y finalmente imprima los números primos en orden decreciente.

**Métodos:**
- public static void main(String[] args): Método principal que inicializa el árbol binario de búsqueda, inserta varios valores en el árbol, y ejecuta el método para imprimir los números primos en orden decreciente.
- Interacción: La clase Main interactúa con la clase ArbolBinarioBusqueda para gestionar la inserción de números en el árbol y para invocar el método que procesa e imprime los números primos. También gestiona la creación de la instancia del árbol y la definición de los valores que serán insertados en el mismo.