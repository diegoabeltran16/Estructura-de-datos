Plan de Desarrollo
1.	Fase de Análisis:
- Identificar las funciones clave a implementar: manejo de archivos, entrada/salida estándar, manipulación de datos.
- Especificar los requisitos funcionales del sistema y cómo deben interactuar entre sí.
2.	Fase de Diseño:
- Definir la estructura del menú principal.
- Crear el diseño modular del código, identificando qué funciones estarán en cada módulo.
- Esbozar los algoritmos necesarios para cada función.
3.	Fase de Implementación:
- Implementar cada módulo por separado, siguiendo la estructura de diseño.
- Desarrollar y probar la función para copiar archivos.
- Implementar la lectura de archivos y mostrar su contenido.
- Desarrollar la función para tomar una lista de números y guardarla en un archivo.
- Implementar la función que lee números desde un archivo y encuentra el mayor.
- Integrar los módulos en el menú principal.
4.	Fase de Pruebas:
- Realizar pruebas unitarias de cada módulo para asegurarse de que funcionan de manera independiente.
- Realizar pruebas integradas para asegurar que el flujo de la interacción del usuario sea correcto.
- Realizar pruebas de casos límite (e.g., archivo no existente, números negativos).
5.	Fase de Documentación:
- Documentar el código fuente con comentarios claros.
- Crear una guía de usuario básica que explique cómo utilizar cada función del programa.

----------------------------------------------------------------------------------------------------
1. Desarrollo del Archivo Principal (main.c):
•Objetivo: Este archivo manejará la interacción con el usuario y llamará a las funciones implementadas en los otros archivos.
•Pasos:
- Implementar la función main().
- Configurar un menú simple para que el usuario seleccione la opción que desea ejecutar.
- Incluir los encabezados necesarios (#include "copy_file.h", #include "read_file.h", etc.).
2. Desarrollo de los Módulos Secundarios:
•	Comienza con los módulos que no dependen de otros y progresivamente pasa a los que sí dependen. Esto asegura que las funciones necesarias estén disponibles al momento de usarlas.
Orden sugerido:
A. copy_file.c y copy_file.h:
•Objetivo: Crear la funcionalidad para copiar message.dat a new.dat.
•Pasos:
- Implementa la función copyFile() que realice la copia.
- Añade validaciones para asegurar que los archivos se abran correctamente.
- Incluir esta función en el menú de main.c.
B. read_file.c y read_file.h:
•Objetivo: Desarrollar la función que lea y muestre el contenido de un archivo.
•Pasos:
- Implementar la función readFile() que solicita el nombre del archivo al usuario y muestra su contenido.
- Asegúrate de manejar errores si el archivo no existe o no se puede abrir.
- Conectar esta función en main.c.
C. write_numbers.c y write_numbers.h:
•Objetivo: Recibir una lista de números del usuario y guardarlos en un archivo.
•Pasos:
- Implementar la función writeNumbersToFile() que pide al usuario ingresar números y los guarda en un archivo.
- Asegurar que el archivo se maneje correctamente y se informe al usuario de cualquier error.
- Integrar esta funcionalidad en main.c.
D. find_max_number.c y find_max_number.h:
•Objetivo: Leer números desde un archivo y determinar el mayor.
•Pasos:
- Implementar la función findMaxNumberInFile() que lee los números de un archivo y encuentra el más grande.
- Validar que el archivo contenga números y manejar posibles errores.
- Conectar esta funcionalidad al menú en main.c.
3. Integración y Pruebas:
- Una vez que cada módulo esté implementado y probado individualmente, verifica que todas las funciones trabajen bien en conjunto.
- Realiza pruebas de casos límite (e.g., archivos que no existen, archivos vacíos, entrada de datos incorrecta).
4. Documentación y Limpieza:
•Asegúrate de que todo el código esté bien documentado con comentarios.
•Revisa que todos los archivos están bien organizados y limpios.
Resumen del Orden de Desarrollo:
1.Desarrollo de main.c con menú básico.
2.Desarrollo de copy_file.c y su integración en main.c.
3.Desarrollo de read_file.c y su integración en main.c.
4.Desarrollo de write_numbers.c y su integración en main.c.
5.Desarrollo de find_max_number.c y su integración en main.c.
6.Pruebas de integración y casos límite.
7.Documentación final y limpieza del código.
