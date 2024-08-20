#include <stdio.h>
#include "copy_file.h"

/**
 * Función que copia el contenido de un archivo fuente a un archivo destino.
 *
 * @param sourceFileName El nombre del archivo fuente que será copiado.
 * @param destFileName El nombre del archivo destino donde se copiará el contenido.
 */
void copyFile(const char *sourceFileName, const char *destFileName) {
    FILE *sourceFile, *destFile;
    char ch;

    // Abrir el archivo de origen en modo lectura
    sourceFile = fopen(sourceFileName, "r");
    if (sourceFile == NULL) {
        printf("No se pudo abrir el archivo fuente %s\n", sourceFileName);
        return;
    }

    // Abrir el archivo de destino en modo escritura (crear o sobrescribir)
    destFile = fopen(destFileName, "w");
    if (destFile == NULL) {
        printf("No se pudo crear el archivo destino %s\n", destFileName);
        fclose(sourceFile);
        return;
    }

    // Leer el contenido del archivo fuente y escribirlo en el archivo destino
    while ((ch = fgetc(sourceFile)) != EOF) {
        fputc(ch, destFile);
    }

    // Cerrar ambos archivos
    fclose(sourceFile);
    fclose(destFile);

    printf("Archivo copiado exitosamente de %s a %s\n", sourceFileName, destFileName);
}
