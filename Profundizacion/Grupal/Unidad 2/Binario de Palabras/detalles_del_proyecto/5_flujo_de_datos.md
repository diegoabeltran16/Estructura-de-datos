# Flujo de datos y Ejecucion

- Entrada del Archivo de Texto:
Numeros.Palabras.Main.java abre el archivo frase.txt y lo lee línea por línea.
Se extraen las palabras usando delimitadores de espacios y puntuaciones, convirtiendo todo a minúsculas para evitar duplicados.

- Inserción en el Árbol Binario:
Cada palabra es enviada al método insertar() de Palabras.ArbolBinarioPalabras.
Si la palabra no existe en el árbol, se crea un nuevo nodo en la posición correcta.
Si la palabra ya existe, el método incrementarFrecuencia() del nodo correspondiente es llamado para incrementar el contador.

- Recorrido y Ordenación de Palabras:
Una vez que todas las palabras han sido insertadas, se llama al método obtenerPalabrasPorFrecuencia(), que recorre el árbol en orden alfabético.
Las palabras se agregan a una lista, que luego es ordenada por frecuencia usando Collections.sort() con un comparador personalizado.

- Salida en Consola:
Numeros.Palabras.Main.java muestra las palabras en la consola, en orden descendente según su frecuencia de aparición, junto con el número de veces que aparecen en el archivo.

## Diagrama de flujo 

```
+---------------------------+    +---------------------------+      +---------------------------+
|     Leer Archivo (Numeros.Palabras.Main)    | ---> | Insertar Palabras (BST)    | ---> | Recorrer y Mostra(BST)   |
+---------------------------+   +---------------------------+      +---------------------------+
| - Leer línea del archivo   |    | - Insertar recursivamente  |      | - Recorrer el árbol y      |
| - Extraer palabras         |    |   palabras en el BST       |      |   ordenar por frecuencia   |
| - Convertir a minúsculas   |    | - Incrementar frecuencia   |      | - Mostrar en consola       |
+---------------------------+      +---------------------------+      +---------------------------+

```
