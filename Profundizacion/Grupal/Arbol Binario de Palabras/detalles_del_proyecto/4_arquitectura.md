# Arquitectura

El proyecto sigue una arquitectura basada en tres capas principales:

- Capa de Datos: Esta capa está compuesta por los nodos del árbol binario, que almacenan las palabras y la frecuencia de aparición. La clase NodoPalabra es el elemento clave en esta capa, ya que define la estructura básica de los datos que se almacenan y gestionan en el árbol.

- Capa de Lógica del Negocio:Aquí se encuentran las operaciones que permiten insertar, gestionar y ordenar las palabras. La clase ArbolBinarioPalabras encapsula la lógica del árbol binario de búsqueda, permitiendo realizar inserciones y consultas sobre las palabras y sus frecuencias.

- Capa de Presentación/Interacción: Esta capa es responsable de la interacción del usuario con el sistema. La clase Main en esta capa se encarga de leer el archivo de entrada, procesar los datos y mostrar el resultado en la consola. Además, coordina las operaciones entre las otras dos capas.

## Diagrama de componentes en la arquitectura

```
+---------------------------+    +------------------------------+    +----------------------------+
|     Capa de Presentación   |    |    Capa de Lógica del BST   |    |        Capa de Datos        |
|        (Main.java)         |    |   (ArbolBinarioPalabras)    |    |        (NodoPalabra)        |
+---------------------------+    +------------------------------+    +----------------------------+
| - Lee el archivo de texto  |    | - Inserta palabras en el BST|    | - Palabra (String)          |
| - Coordina la inserción de |    | - Maneja la frecuencia de   |    | - Frecuencia (int)          |
|   palabras en el BST       |    |   cada palabra              |    | - Izquierdo (NodoPalabra)   |
| - Muestra el resultado     |    | - Recorre y ordena las      |    | - Derecho (NodoPalabra)     |
|   (palabras y frecuencias) |    |   palabras por frecuencia   |     +----------------------------+
+---------------------------+    +------------------------------+

```

