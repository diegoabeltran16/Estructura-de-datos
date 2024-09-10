# Arquitectura

El proyecto está compuesto por tres componentes principales que interactúan para lograr el objetivo de gestionar un árbol binario de búsqueda (BST), filtrar números primos y presentarlos en orden decreciente. A continuación se describe la arquitectura del proyecto de manera detallada.

## Numeros.Nodo.java
**Responsabilidad:** La clase Numeros.Nodo es la base de la estructura del árbol binario de búsqueda. Representa cada elemento (nodo) del árbol y contiene los atributos necesarios para vincular a sus hijos izquierdo y derecho. Este componente es fundamental para almacenar el valor numérico de cada nodo en el árbol.

**Atributos:**
- int valor: El valor almacenado en el nodo (en este caso, un número entero).
- Numeros.Nodo izquierdo: Referencia al hijo izquierdo del nodo.
- Numeros.Nodo derecho: Referencia al hijo derecho del nodo.

**Métodos:**
- Constructor Numeros.Nodo(int valor): Inicializa el nodo con el valor proporcionado y establece sus referencias a los hijos como null.
- Interacción: La clase Numeros.Nodo será utilizada por la clase Numeros.ArbolBinarioBusqueda para crear e interconectar los nodos del árbol. Cada nodo se relaciona con otros nodos mediante sus atributos izquierdo y derecho, formando el árbol binario.

## Numeros.ArbolBinarioBusqueda.java
**Responsabilidad:** Esta clase contiene la lógica principal del árbol binario de búsqueda. Se encarga de insertar valores, recorrer el árbol, identificar números primos, y reordenar estos números en orden decreciente.

**Atributos:**
- Numeros.Nodo raiz: La raíz del árbol binario de búsqueda, el punto de entrada del árbol.

**Métodos:**
- void insertar(int valor): Inserta un nuevo valor en el árbol binario de búsqueda, asegurando que se mantenga el orden ascendente (hijos izquierdos menores, hijos derechos mayores).
- Numeros.Nodo insertarRecursivo(Numeros.Nodo nodo, int valor): Método recursivo auxiliar que se utiliza para insertar el valor en su lugar correspondiente en el árbol.
- List<Integer> obtenerPrimosEnOrdenDecreciente(): Devuelve una lista de números primos encontrados en el árbol, ordenados de mayor a menor.
- void obtenerPrimosRecursivo(Numeros.Nodo nodo, List<Integer> primos): Método recursivo que recorre el árbol en busca de números primos y los agrega a la lista proporcionada.
- boolean esPrimo(int numero): Verifica si un número es primo, realizando divisiones hasta la raíz cuadrada del número para comprobar su divisibilidad.
- void imprimirPrimosEnOrdenDecreciente(): Imprime los números primos en orden decreciente.
- Interacción: Numeros.ArbolBinarioBusqueda interactúa directamente con Numeros.Nodo para construir el árbol binario y gestionar los enlaces entre nodos. Esta clase también interactúa con la clase Numeros.Palabras.Main al proporcionar los métodos para insertar y procesar los números del árbol.

## Numeros.Palabras.Main.java
**Responsabilidad:** La clase Numeros.Palabras.Main es el punto de entrada del programa. Su responsabilidad es coordinar la ejecución del código, permitiendo que el usuario cree el árbol binario de búsqueda, inserte los valores, y finalmente imprima los números primos en orden decreciente.

**Métodos:**
- public static void main(String[] args): Método principal que inicializa el árbol binario de búsqueda, inserta varios valores en el árbol, y ejecuta el método para imprimir los números primos en orden decreciente.
- Interacción: La clase Numeros.Palabras.Main interactúa con la clase Numeros.ArbolBinarioBusqueda para gestionar la inserción de números en el árbol y para invocar el método que procesa e imprime los números primos. También gestiona la creación de la instancia del árbol y la definición de los valores que serán insertados en el mismo.