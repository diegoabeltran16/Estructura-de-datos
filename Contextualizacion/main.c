#include <stdio.h>
#include <stdlib.h>
#include <direct.h>  // Incluye la biblioteca para utilizar _getcwd en Windows
#include "include/copy_file.h"
#include "include/read_file.h"
#include "include/write_numbers.h"
#include "include/find_max_number.h"

// Prototipo de la función para mostrar el menú
void showMenu();

int main() {
    int choice;

    // Ciclo principal del programa, que continúa hasta que el usuario elige salir
    while (1) {
        // Muestra el menú de opciones al usuario
        showMenu();
        printf("Seleccione una opción: ");
        
        // Captura la opción seleccionada por el usuario
        scanf("%d", &choice);

        // Obtiene y muestra el directorio de trabajo actual
        char cwd[1024];
        if (_getcwd(cwd, sizeof(cwd)) != NULL) {
            printf("Directorio actual: %s\n", cwd);
        } else {
            // Muestra un mensaje de error si no se puede obtener el directorio actual
            perror("_getcwd() error");
        }

        // Evalúa la opción seleccionada y ejecuta la función correspondiente
        switch (choice) {
            case 1:
                // Copia el archivo 'message.dat' a 'output.dat' usando una ruta simplificada
                copyFile("data\\message.dat", "data\\output.dat");
                break;

            case 2:
                // Llama a la función que lee y muestra el contenido de un archivo
                readFile();
                break;

            case 3:
                // Llama a la función que escribe una lista de números en un archivo
                writeNumbersToFile();
                break;

            case 4:
                // Llama a la función que encuentra e imprime el número más grande en un archivo
                findMaxNumberInFile();
                break;

            case 5:
                // Sale del programa
                printf("Saliendo del programa...\n");
                exit(0);

            default:
                // Maneja entradas inválidas mostrando un mensaje y repitiendo el ciclo
                printf("Opción no válida. Por favor, intente de nuevo.\n");
                break;
        }
    }

    return 0;
}

/**
 * Función que muestra el menú principal al usuario.
 * Este menú ofrece al usuario varias opciones para interactuar con el programa.
 * La función encapsula la presentación del menú para mejorar la modularidad y la legibilidad del código.
 */
void showMenu() {
    printf("\n===== MENU PRINCIPAL =====\n");
    printf("1. Copiar archivo 'message.dat' a 'new.dat'\n");
    printf("2. Leer y mostrar el contenido de un archivo\n");
    printf("3. Ingresar una lista de números y guardarla en un archivo\n");
    printf("4. Leer un archivo de números e imprimir el número más grande\n");
    printf("5. Salir\n");
    printf("==========================\n");
}
