#include <stdio.h>
#include <stdlib.h>
#include "include/copy_file.h"  // Incluye la declaración de la función copyFile

/**
 * @brief Copia el contenido de un archivo fuente a un archivo destino.
 * 
 * La función copyFile se encarga de abrir un archivo fuente para lectura y un archivo destino para escritura, 
 * luego copia el contenido del archivo fuente al archivo destino carácter por carácter. 
 * Si ocurre algún error al abrir cualquiera de los archivos, se muestra un mensaje de error detallado.
 * 
 * @param source La ruta y nombre del archivo fuente que se va a copiar.
 * @param destination La ruta y nombre del archivo destino donde se copiará el contenido.
 */
void copyFile(const char *source, const char *destination) {
    FILE *srcFile, *destFile;
    char ch;

    // Imprimir la ruta del archivo fuente para depuración
    printf("Intentando abrir el archivo fuente: %s\n", source);

    // Intentar abrir el archivo fuente en modo lectura
    srcFile = fopen(source, "r");
    if (srcFile == NULL) {
        // Mostrar un mensaje de error si no se puede abrir el archivo fuente
        perror("Error al abrir el archivo fuente");
        return;
    }

    // Intentar abrir el archivo de destino en modo escritura
    destFile = fopen(destination, "w");
    if (destFile == NULL) {
        // Mostrar un mensaje de error si no se puede abrir el archivo de destino
        perror("Error al abrir el archivo de destino");
        fclose(srcFile);  // Cerrar el archivo fuente antes de retornar
        return;
    }

    // Copiar el contenido del archivo fuente al archivo de destino carácter por carácter
    while ((ch = fgetc(srcFile)) != EOF) {
        fputc(ch, destFile);
    }

    // Imprimir un mensaje de éxito una vez que la copia se ha completado
    printf("Archivo copiado exitosamente de %s a %s\n", source, destination);

    // Cerrar ambos archivos para liberar los recursos
    fclose(srcFile);
    fclose(destFile);
}
