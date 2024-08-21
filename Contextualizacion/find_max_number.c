#include "include/find_max_number.h"
#include <stdio.h>

/**
 * @brief Función que encuentra el número más grande en un archivo.
 *
 * Esta función permite al usuario especificar un archivo de texto que contiene una lista de números enteros.
 * Luego, la función lee cada número del archivo y determina cuál es el mayor. Si el archivo no se puede abrir,
 * se notifica al usuario con un mensaje de error. Al final, se imprime el número más grande encontrado en el archivo.
 */
void findMaxNumberInFile() {
    char filename[100];
    FILE *file;
    int number, maxNumber;

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

    // Inicializar maxNumber con un valor muy bajo para asegurar que cualquier número lo supere
    maxNumber = -9999;
    
    // Leer números del archivo y encontrar el más grande
    while (fscanf(file, "%d", &number) != EOF) {
        if (number > maxNumber) {
            maxNumber = number;  // Actualizar maxNumber si se encuentra un número mayor
        }
    }

    // Imprimir el número más grande encontrado en el archivo
    printf("El número más grande en el archivo '%s' es: %d\n", filename, maxNumber);

    // Cerrar el archivo para liberar recursos
    fclose(file);
}
