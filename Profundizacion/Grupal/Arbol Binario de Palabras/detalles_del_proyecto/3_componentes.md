# Componentes

**NodoPalabra.java**
Este componente representará un nodo en el árbol binario de búsqueda. Cada nodo almacenará una palabra y la frecuencia de aparición de esa palabra en el archivo de texto.

- Atributos:
palabra: (Tipo: String) Almacena la palabra correspondiente al nodo.
frecuencia: (Tipo: int) Un contador que almacena la cantidad de veces que aparece la palabra en el archivo de texto.
izquierdo: (Tipo: NodoPalabra) Referencia al nodo hijo izquierdo, que contendrá palabras menores en orden alfabético.
derecho: (Tipo: NodoPalabra) Referencia al nodo hijo derecho, que contendrá palabras mayores en orden alfabético.

- Métodos:
Constructor NodoPalabra(String palabra): Inicializa un nodo con una palabra y establece la frecuencia en 1.
incrementarFrecuencia(): Incrementa el contador de frecuencia en 1 cada vez que se repite la palabra.

**ArbolBinarioPalabras.java**
Este componente será el responsable de gestionar la estructura del árbol binario de búsqueda (BST). Permitirá insertar palabras en el árbol y manejar la frecuencia de aparición de cada palabra. También proporcionará métodos para recorrer el árbol y mostrar las palabras en orden descendente según su frecuencia.

- Atributos:
raiz: (Tipo: NodoPalabra) Referencia al nodo raíz del árbol binario.

- Métodos:
insertar(String palabra): Inserta una palabra en el árbol binario de búsqueda. Si la palabra ya existe en el árbol, incrementa su frecuencia.
insertarRecursivo(NodoPalabra nodo, String palabra): Método recursivo para insertar palabras en el árbol binario. Ordena las palabras alfabéticamente.
obtenerPalabrasPorFrecuencia(): Devuelve una lista con todas las palabras almacenadas en el árbol, ordenadas por su frecuencia de aparición, de mayor a menor.
recorrerArbol(NodoPalabra nodo, List<NodoPalabra> palabras): Método recursivo para recorrer el árbol binario y agregar las palabras a una lista para su posterior ordenación.
imprimirPalabrasPorFrecuencia(): Imprime en consola las palabras del archivo, ordenadas por su frecuencia de aparición, de mayor a menor.

**Main.java**
Este componente será el punto de entrada del programa. Se encargará de leer el archivo de texto, extraer las palabras y almacenarlas en el árbol binario de búsqueda. También llamará al método que imprimirá las palabras ordenadas por frecuencia de aparición.

- Atributos:
Ninguno (Solo contiene el método principal).

- Métodos:
main(String[] args):
Crea una instancia de ArbolBinarioPalabras.
Lee las palabras desde un archivo de texto (frase.txt).
Inserta las palabras en el árbol binario de búsqueda.
Llama al método imprimirPalabrasPorFrecuencia() para mostrar las palabras y sus frecuencias ordenadas.

- Funcionalidad:
Este componente gestionará la interacción con el archivo de texto, procesando las palabras y llamando a los métodos del árbol binario para realizar las operaciones de almacenamiento y visualización.

**frase.txt (Archivo de entrada)**
Este archivo contendrá la frase que será procesada por el programa. Será leído por el componente Main.java, y las palabras extraídas serán almacenadas en el árbol binario.

- Contenido:
Un archivo de texto plano (.txt) que puede contener una o más frases, separadas por espacios y signos de puntuación.

## Interacción entre los Componentes:

**Lectura del Archivo:**
Main.java leerá el contenido del archivo frase.txt línea por línea y dividirá las frases en palabras.

**Inserción de Palabras en el Árbol:**
Cada palabra extraída será insertada en el árbol binario de búsqueda utilizando el método insertar() de la clase ArbolBinarioPalabras.java.
Si una palabra ya existe en el árbol, se incrementará el contador de frecuencia.

**Almacenamiento en el Árbol:**
Las palabras serán almacenadas en nodos de la clase NodoPalabra.java, manteniendo el orden alfabético.

**Recorrido y Visualización:**
Una vez que todas las palabras estén insertadas, Main.java llamará al método imprimirPalabrasPorFrecuencia(), que recorrerá el árbol, ordenará las palabras por frecuencia, y las mostrará en la consola.
