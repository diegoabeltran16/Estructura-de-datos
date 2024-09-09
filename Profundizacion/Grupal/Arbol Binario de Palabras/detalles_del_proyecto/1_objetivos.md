# Objetivos

## Diseño de un Algoritmo para Almacenar y Gestionar Palabras en un Árbol Binario de Búsqueda:
Diseñar un algoritmo que lea una frase almacenada en un archivo de texto y la procese en un árbol binario de búsqueda (BST). Cada palabra de la frase será almacenada en el árbol sin repetirse. Si una palabra aparece más de una vez en la frase, el árbol incrementará el contador de frecuencia en lugar de almacenar la palabra nuevamente. El algoritmo deberá recorrer el árbol para mostrar las palabras de la frase, ordenadas por la frecuencia de aparición (de mayor a menor). La frase será definida por los estudiantes, quienes la almacenarán previamente en el archivo de texto.

**Parametros a cumplir para el arbol binario de palabras**
- El árbol binario de búsqueda no debe almacenar duplicados. En su lugar, cada nodo contendrá una palabra y la frecuencia de su aparición en el archivo de texto.
- El algoritmo deberá mostrar las palabras en orden descendente según la cantidad de veces que aparecen en el archivo de texto.
- La lectura de la frase deberá manejarse desde un archivo de texto externo y no a través de entradas directas del usuario.

**Objetivos especificos**
- Leer una Frase desde un Archivo de Texto: Desarrollar un algoritmo en Java que lea el contenido de un archivo de texto que contiene una frase. Este archivo será procesado utilizando IntelliJ IDEA, y la frase extraída será dividida en palabras para su posterior almacenamiento en un árbol binario de búsqueda.
- Almacenar Palabras sin Duplicados en un Árbol Binario de Búsqueda: Diseñar un procedimiento que inserte cada palabra de la frase en un árbol binario de búsqueda, garantizando que no se repitan palabras. En caso de que una palabra se repita, el algoritmo deberá incrementar un contador de frecuencia en lugar de añadir la palabra nuevamente.
- Ordenar y Mostrar Palabras por Frecuencia de Aparición: Implementar un método en Java que recorra el árbol binario de búsqueda y muestre las palabras almacenadas, ordenándolas según su frecuencia de aparición en la frase. Las palabras con mayor frecuencia deberán mostrarse primero, utilizando el entorno de desarrollo IntelliJ IDEA para garantizar la correcta implementación y visualización de los resultados.
