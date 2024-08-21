#include "include/read_file.h"
#include <stdio.h>

/**
 * @brief Función que lee y muestra el contenido de un archivo.
 *
 * Esta función solicita al usuario que ingrese el nombre de un archivo. A continuación, intenta abrir 
 * el archivo en modo de lectura. Si tiene éxito, la función lee el archivo carácter por carácter y 
 * muestra su contenido en la consola. Si no se puede abrir el archivo, se imprime un mensaje de error.
 */
void readFile() {
    char filename[100];
    FILE *file;
    char ch;

    // Solicitar al usuario que ingrese el nombre del archivo que se va a leer
    printf("Ingrese el nombre del archivo a leer: ");
    scanf("%s", filename);

    // Intentar abrir el archivo en modo lectura
    file = fopen(filename, "r");
    if (file == NULL) {
        // Mostrar un mensaje de error si el archivo no se puede abrir
        printf("No se pudo abrir el archivo.\n");
        return;
    }

    // Mostrar el contenido del archivo al usuario
    printf("Contenido del archivo '%s':\n", filename);
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);  // Imprimir cada carácter en la consola
    }

    // Cerrar el archivo para liberar recursos
    fclose(file);
}
