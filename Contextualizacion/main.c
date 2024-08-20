#include <stdio.h>
#include <stdlib.h>
#include "include/copy_file.h"
#include "include/read_file.h"
#include "include/write_numbers.h"
#include "include/find_max_number.h"


// Prototipo de la función para mostrar el menú
void showMenu();

int main() {
    int choice;

    while (1) {
        showMenu();
        printf("Seleccione una opcion: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                // Opción para copiar el archivo
                copyFile("message.dat", "new.dat");
                break;

            case 2:
                // Opción para leer y mostrar el contenido de un archivo
                readFile();
                break;

            case 3:
                // Opción para escribir una lista de números en un archivo
                writeNumbersToFile();
                break;

            case 4:
                // Opción para encontrar el número más grande en un archivo
                findMaxNumberInFile();
                break;

            case 5:
                // Opción para salir del programa
                printf("Saliendo del programa...\n");
                exit(0);

            default:
                printf("Opcion no válida. Por favor, intente de nuevo.\n");
                break;
        }
    }

    return 0;
}

/**
 * Función que muestra el menú principal.
 * Ofrece al usuario varias opciones para interactuar con el programa.
 */
void showMenu() {
    printf("\n===== MENU PRINCIPAL =====\n");
    printf("1. Copiar archivo 'message.dat' a 'new.dat'\n");
    printf("2. Leer y mostrar el contenido de un archivo\n");
    printf("3. Ingresar una lista de numeros y guardarla en un archivo\n");
    printf("4. Leer un archivo de numeros e imprimir el numero mas grande\n");
    printf("5. Salir\n");
    printf("==========================\n");
}

