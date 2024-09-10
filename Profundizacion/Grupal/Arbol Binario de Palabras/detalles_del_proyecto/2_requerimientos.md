# Requerimientos

El proyecto tiene como objetivo almacenar y gestionar palabras desde un archivo de texto en un árbol binario de búsqueda. Utilizando Java y VS Code como entorno de desarrollo, el sistema deberá permitir la inserción de palabras en el árbol, gestionar la frecuencia de aparición de cada palabra y mostrar las palabras en orden descendente según su frecuencia.

## Requerimientos funcionales

**Lectura de Archivo de Texto:** El sistema debe ser capaz de leer el contenido de un archivo de texto externo, que contiene una o más frases. El archivo será procesado para extraer las palabras y luego almacenarlas en el árbol binario de búsqueda.
- Formato del Archivo de Texto: El archivo debe estar en formato .txt y contener palabras separadas por espacios, signos de puntuación u otros delimitadores comunes.
- Gestión de Mayúsculas y Minúsculas: Todas las palabras extraídas del archivo deberán ser convertidas a minúsculas para evitar duplicados que difieran solo por el uso de mayúsculas.

**Inserción de Palabras en el Árbol Binario:** El sistema debe insertar cada palabra en el árbol binario de búsqueda. Si la palabra ya existe en el árbol, el sistema debe incrementar la frecuencia de aparición en lugar de insertar la palabra de nuevo.
- No se permiten duplicados: Cada palabra se almacenará una sola vez en el árbol, con su contador de frecuencia correspondiente.
- Estructura del Nodo: Cada nodo del árbol debe contener la palabra y un contador de frecuencia que indica cuántas veces ha aparecido la palabra en el archivo.

**Ordenación y Visualización de Palabras por Frecuencia:** El sistema debe mostrar las palabras almacenadas en el árbol binario de búsqueda, ordenadas por la frecuencia de aparición, de mayor a menor.
- Formato de Salida: Cada palabra debe mostrarse junto con su frecuencia de aparición, en formato claro y legible. Las palabras con mayor frecuencia deben aparecer primero.

**Manejo de Casos Extremos:** El sistema debe poder manejar archivos vacíos sin generar errores.
- Palabras no válidas: Si se encuentran símbolos o caracteres no válidos, estos deben ser ignorados adecuadamente sin interrumpir el flujo del programa.
- Espacios en Blanco: Las líneas en blanco o los espacios entre palabras no deben ser considerados como palabras válidas.

## Requerimientos tecnicos

**Lenguaje de Programación:**
El proyecto debe ser desarrollado completamente en Java, utilizando las convenciones del lenguaje para la manipulación de árboles binarios, manejo de archivos, y entrada/salida de texto.

**Entorno de Desarrollo:**
VS Code será el entorno de desarrollo utilizado para la implementación del proyecto. Se debe asegurar que el entorno esté correctamente configurado con un SDK de Java adecuado (por ejemplo, OpenJDK).

**Estructura del Árbol Binario de Búsqueda:** El árbol binario de búsqueda debe ser implementado de manera que permita la inserción eficiente de palabras y la gestión de su frecuencia.
- Inserción Recursiva: El método de inserción debe ser recursivo para mantener la eficiencia y simplicidad del código.
- Recorridos del Árbol: El recorrido del árbol debe permitir extraer las palabras en orden ascendente según su valor alfabético, pero una vez almacenadas en una lista, deberán ordenarse por su frecuencia.

**Manejo de Archivos:** El sistema debe ser capaz de manejar archivos de texto de manera eficiente. Para ello, se utilizarán clases estándar de Java, como BufferedReader y FileReader, para leer las líneas y extraer las palabras de manera fluida.
- Excepciones Controladas: En caso de que no se pueda acceder al archivo de texto (por ejemplo, si el archivo no existe), el sistema debe capturar estas excepciones y mostrar un mensaje de error claro sin detener la ejecución completa del programa.

**Optimización y Eficiencia:**
- Espacio en Memoria: El árbol binario debe estar optimizado para no mantener referencias innecesarias y gestionar eficientemente la memoria.
- Uso de Colecciones: Para la ordenación de las palabras por frecuencia, se utilizarán las clases de colecciones como ArrayList y Collections.sort() para asegurar un rendimiento adecuado, incluso con archivos de texto más grandes.

## Requerimientos de Pruebas
- Pruebas de Inserción de Palabras: Se debe verificar que las palabras son insertadas correctamente en el árbol binario sin duplicados. Si una palabra aparece más de una vez, se debe incrementar el contador de frecuencia.
- Pruebas con Archivos de Diferente Tamaño: El sistema debe ser probado con archivos de texto de diversos tamaños; desde archivos vacíos, archivos con pocas palabras, hasta archivos más grandes con múltiples frases.
- Archivos Vacíos: El sistema no debe fallar al procesar un archivo vacío. Debe mostrar simplemente que no hay palabras para procesar.
- Pruebas de Frecuencia de Aparición: Verificar que el sistema ordena las palabras correctamente por frecuencia de aparición, mostrando primero las más frecuentes.
Probar con frases que contengan palabras con la misma frecuencia para asegurarse de que se manejen correctamente.
- Pruebas de Manejo de Excepciones: Probar el comportamiento del programa cuando no se puede acceder al archivo (por ejemplo, si se pasa un nombre de archivo incorrecto) y verificar que el mensaje de error es claro y no causa una interrupción completa del sistema.
