#include "include/write_numbers.h"
#include <stdio.h>

void writeNumbersToFile() {
    FILE *file;
    char filename[100];
    int number;

    // Solicitar al usuario el nombre del archivo
    printf("Ingrese el nombre del archivo donde se guardará la lista de números: ");
    scanf("%s", filename);

    // Abrir el archivo para escritura
    file = fopen(filename, "w");
    if (file == NULL) {
        printf("No se pudo abrir el archivo para escribir.\n");
        return;
    }

    printf("Ingrese números enteros para guardar en el archivo (ingrese -9999 para finalizar):\n");

    // Leer números del usuario y escribirlos en el archivo
    while (1) {
        scanf("%d", &number);
        if (number == -9999) {
            break;
        }
        fprintf(file, "%d ", number);
    }

    // Cerrar el archivo
    fclose(file);
    printf("Los números fueron guardados en el archivo '%s'.\n", filename);
}
