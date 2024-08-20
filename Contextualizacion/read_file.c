// read_file.c
#include "include/read_file.h"
#include <stdio.h>

void readFile() {
    char filename[100];
    FILE *file;
    char ch;

    printf("Ingrese el nombre del archivo a leer: ");
    scanf("%s", filename);

    file = fopen(filename, "r");
    if (file == NULL) {
        printf("No se pudo abrir el archivo.\n");
        return;
    }

    printf("Contenido del archivo '%s':\n", filename);
    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    fclose(file);
}
