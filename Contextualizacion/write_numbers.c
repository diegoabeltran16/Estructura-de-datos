#include "include/write_numbers.h"
#include <stdio.h>

/**
 * @brief Solicita al usuario ingresar una lista de números y los guarda en un archivo.
 *
 * Esta función permite al usuario ingresar una lista de números enteros que serán guardados en un archivo 
 * especificado. El usuario continúa ingresando números hasta que decide detenerse ingresando el número -9999. 
 * Este número es utilizado como un indicador de finalización y no se guarda en el archivo.
 */
void writeNumbersToFile() {
    FILE *file;
    char filename[100];
    int number;

    // Solicitar al usuario el nombre del archivo donde se guardarán los números
    printf("Ingrese el nombre del archivo donde se guardará la lista de números: ");
    scanf("%s", filename);

    // Intentar abrir el archivo en modo escritura
    file = fopen(filename, "w");
    if (file == NULL) {
        // Mostrar un mensaje de error si el archivo no se puede abrir para escribir
        printf("No se pudo abrir el archivo para escribir.\n");
        return;
    }

    // Instrucciones al usuario para ingresar números
    printf("Ingrese números enteros para guardar en el archivo (ingrese -9999 para finalizar):\n");

    // Leer números del usuario y escribirlos en el archivo hasta que se ingrese -9999
    while (1) {
        scanf("%d", &number);
        if (number == -9999) {
            break;  // Salir del bucle si se ingresa -9999
        }
        fprintf(file, "%d ", number);  // Escribir el número en el archivo
    }

    // Cerrar el archivo para asegurar que los datos se guarden correctamente
    fclose(file);
    printf("Los números fueron guardados en el archivo '%s'.\n", filename);
}
