#ifndef COPY_FILE_H
#define COPY_FILE_H

/**
 * @brief Copia el contenido de un archivo fuente a un archivo destino.
 * 
 * Esta función abre el archivo fuente en modo de lectura y el archivo destino en modo de escritura. Luego, copia cada carácter 
 * desde el archivo fuente al archivo destino hasta llegar al final del archivo. Si hay algún error al abrir cualquiera de los 
 * archivos, se imprime un mensaje de error y la función retorna sin realizar la copia.
 * 
 * @param sourceFileName El nombre del archivo fuente que será copiado.
 * @param destFileName El nombre del archivo destino donde se copiará el contenido.
 */
void copyFile(const char *sourceFileName, const char *destFileName);

#endif // COPY_FILE_H
