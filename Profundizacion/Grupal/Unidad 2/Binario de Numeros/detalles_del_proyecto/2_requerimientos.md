# Requerimientos

## Requerimientos Funcionales:
- Recorrido del Árbol Binario de Búsqueda (BST): El sistema debe permitir recorrer el árbol binario de búsqueda de manera eficiente. Dado que el árbol almacena los números en orden ascendente, el algoritmo deberá implementar un recorrido en orden inverso (postorden o en orden) para asegurar que se analicen correctamente los valores, especialmente cuando se requiere la identificación de números primos.
- Identificación de Números Primos: El procedimiento debe ser capaz de identificar de forma precisa los números primos que se encuentran almacenados en el árbol. Esto implica la creación de un método que verifique si un número almacenado en el nodo es primo, aplicando los criterios matemáticos correspondientes para la validación (un número es primo si solo es divisible por 1 y por sí mismo).
- Filtrado de Números Primos: Durante el recorrido del árbol, los números que no sean primos deben ser descartados. El sistema deberá almacenar solo los números primos encontrados para procesarlos y luego imprimirlos en el orden requerido.
- Reorganización de los Números en Orden Decreciente: El algoritmo debe ser capaz de reorganizar los números primos filtrados para que sean impresos en orden descendente, a pesar de que originalmente están almacenados en orden ascendente en el árbol binario de búsqueda.
- Impresión de los Números Primos en Orden Decreciente: Una vez que los números primos han sido identificados y reordenados, el sistema deberá imprimirlos de manera clara en la consola, asegurándose de que el orden final de salida sea del mayor número primo al menor.

## Requerimientos Técnicos:
- Lenguaje de Programación: El código debe estar completamente desarrollado en Java utilizando las características y funcionalidades propias del lenguaje para la manipulación de árboles binarios de búsqueda.
- Entorno de Desarrollo: El procedimiento debe implementarse y probarse en el entorno IntelliJ IDEA, aprovechando las herramientas de depuración y optimización que ofrece el IDE.
- Estructura del Árbol Binario de Búsqueda: El árbol binario de búsqueda utilizado debe estar bien definido y estructurado para permitir el almacenamiento y la búsqueda eficiente de números enteros. Este árbol debe contener nodos con un valor numérico y punteros a los nodos hijos (izquierdo y derecho).
- Algoritmo para la Verificación de Números Primos: El procedimiento de identificación de números primos debe ser eficiente, evitando operaciones innecesarias y garantizando un tiempo de ejecución razonable, incluso para árboles de gran tamaño.
- Optimización del Recorrido del Árbol: El algoritmo que recorre el árbol debe estar optimizado para no realizar recorridos redundantes o innecesarios. Dado que los números ya están ordenados de manera ascendente, se deberá ajustar el recorrido para facilitar la extracción de los números en orden descendente después de su filtrado.

## Requerimientos de Pruebas:
- Prueba de Identificación de Primos: Se debe probar que el sistema identifica correctamente los números primos en diferentes casos (por ejemplo, en árboles con números consecutivos, mezclas de números primos y no primos, o solo números no primos).
- Prueba de Reordenamiento: Una vez identificados los números primos, se debe validar que el sistema los reordena correctamente en orden decreciente y que la salida en la consola refleja esta ordenación.
- Prueba de Casos Extremos: El sistema debe ser probado con diferentes tamaños de árboles, incluyendo árboles con pocos nodos, árboles muy grandes, o árboles con todos los números siendo primos, para garantizar que el algoritmo se comporte de manera eficiente y precisa en todos los escenarios.