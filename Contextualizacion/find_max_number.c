// find_max_number.c
#include "include/find_max_number.h"
#include <stdio.h>

void findMaxNumberInFile() {
    char filename[100];
    FILE *file;
    int number, maxNumber;

    printf("Ingrese el nombre del archivo a leer: ");
    scanf("%s", filename);

    file = fopen(filename, "r");
    if (file == NULL) {
        printf("No se pudo abrir el archivo.\n");
        return;
    }

    maxNumber = -9999;
    while (fscanf(file, "%d", &number) != EOF) {
        if (number > maxNumber) {
            maxNumber = number;
        }
    }

    printf("El número más grande en el archivo '%s' es: %d\n", filename, maxNumber);

    fclose(file);
}
