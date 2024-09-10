# Mejores Practicas

- **Nombres Claros:** Se recomienda usar nombres descriptivos para las clases, métodos y variables. Por ejemplo, nombres como Palabras.NodoPalabra, insertar() e incrementarFrecuencia() deben reflejar claramente su propósito.

- **Modularidad:** Cada clase debe cumplir una responsabilidad específica. Por ejemplo, Palabras.NodoPalabra.java se utilizará solo para almacenar palabras y frecuencias, mientras que Palabras.ArbolBinarioPalabras.java se encargará de gestionar la estructura del árbol.

- **Documentación:** Es importante añadir comentarios en el código y utilizar JavaDoc para describir claramente el propósito de clases y métodos, lo que facilitará la comprensión y mantenimiento del proyecto.

- **Evitar Código Duplicado:** Se recomienda usar métodos auxiliares y recursivos para evitar la duplicación de lógica en varias partes del código.

- **Uso de Expresiones Regulares:** Se deben emplear expresiones regulares, como split("\\W+"), para separar las palabras y eliminar los signos de puntuación.

- **Manejo Eficiente de Archivos:** Al leer archivos, se sugiere el uso de BufferedReader para optimizar la lectura de archivos grandes. Además, es necesario capturar las excepciones adecuadas para manejar posibles errores.

- **Árbol Binario Optimizado:** El árbol binario debe estar correctamente organizado para garantizar inserciones y búsquedas eficientes. Las inserciones deben seguir manteniendo el orden alfabético en el árbol.

- **Uso de Estructuras de Datos Adecuadas:** Se sugiere el uso de ArrayList para almacenar temporalmente las palabras y Collections.sort() para ordenarlas según su frecuencia.

- **Manejo de Casos Extremos:** Se deben prever casos como archivos vacíos o con pocas palabras, así como la eliminación de caracteres o palabras no válidos.

- **Pruebas Exhaustivas:** Se deben realizar pruebas exhaustivas con archivos vacíos, pequeños, grandes y con palabras repetidas para asegurar el correcto funcionamiento del sistema.