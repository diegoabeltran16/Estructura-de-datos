# Flujo de la Interacción
1.	Inicio del Programa:
- El usuario ejecuta el programa.
- Se muestra un menú principal con las opciones:
1.Copiar archivo message.dat a new.dat.
2.Leer y mostrar el contenido de un archivo.
3.Ingresar una lista de números y guardarla en un archivo.
4.Leer un archivo de números e imprimir el número más grande.
5.Salir.

2.	Selección de la Opción:
- El usuario elige una opción del menú.
- Según la opción seleccionada, se ejecuta el módulo correspondiente.

3.	Flujo de cada Opción:
Opción 1: Copiar archivo
- El programa abre message.dat para lectura.
- Verifica si el archivo se abrió correctamente.
- Crea o sobreescribe new.dat y copia el contenido de message.dat en él.
- Informa al usuario sobre el éxito o fracaso de la operación.
Opción 2: Leer archivo
- El programa solicita al usuario el nombre del archivo que desea leer.
- Abre el archivo en modo lectura.
- Si el archivo se abre correctamente, muestra su contenido en la consola.
- Informa al usuario en caso de error.
Opción 3: Ingresar lista de números
- El programa solicita al usuario que ingrese números hasta que se ingrese -9999.
- Escribe los números ingresados en un archivo cuyo nombre es solicitado al usuario.
- Confirma la escritura exitosa de los datos en el archivo.
Opción 4: Leer lista de números y encontrar el mayor
- El programa solicita al usuario el nombre del archivo que contiene la lista de números.
- Lee los números del archivo y los almacena en un array.
- Encuentra e imprime el número más grande en la consola.
Opción 5: Salir
- El programa finaliza su ejecución.
