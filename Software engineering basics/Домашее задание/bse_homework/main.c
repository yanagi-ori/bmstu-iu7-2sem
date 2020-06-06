/*!
 \file
 \brief Основной файл программы

 Основной файл программы, содержащий в себе первый уровень декомпозиции
 */


#include <stdio.h>
#include "convert.h"
#include "utils.h"

#define ERROR_INVALID_FILE -10 //!< Файл не существет
#define WARN_EMPTY_FILE -11 //!< Предупреждение о пустом файле
#define ERROR_IO -12 //!< Ошибка чтения/записи
#define ERROR_INCORRECT_NUM -20 //!< Число не соответствует правилам записи двоичного числа
#define ERROR_CONVERT -30 //!< Ошибка при переводе из двоичной системы счисления в шестнадцатеричную


int main()
{
    char path[256];
    char *out_path = "out_hex.txt";
    char temp[16];
    char bin[81] = {'\0'};
    char hex[21] = {'\0'};


    printf("Hello! It is the homework program of Bogatyrev Ivan IU7-22B\n");
    printf("Please, enter the path to your file: \n");

    scanf("%s", path);
    FILE *file = fopen(path, "r");
    if (file == NULL)
    {
        printf("File is not exists");
        return ERROR_INVALID_FILE;
    }

    FILE *file_out = fopen(out_path, "w");
    if (file == NULL)
    {
        printf("File is not exists");
        return ERROR_IO;
    }

    fgets(temp, 2, file);
    if (temp[0] == '\0')
    {
        printf("Empty File");
        return WARN_EMPTY_FILE;
    }
    rewind(file);
    int rc;

    do
    {
        rc = get_row(file, bin);
        if (rc == 0)
        {

            bin_to_hex(bin, hex);
            if (hex[0] == -3)
            {
                printf("There was an unexpected error while converting binary number to hex.");
                return ERROR_CONVERT;
            }
            rc = write_row(file_out, hex);
            if (rc == ERROR_IO)
            {
                printf("I/O error was caused.");
                return ERROR_IO;
            }
        }
        else if (rc == ERROR_INCORRECT_NUM)
        {
            printf("The file contains incorrect data.");
            return ERROR_INCORRECT_NUM;
        }
        else if (rc == -2)
        {
            get_row(file, bin);
        }

    } while (!feof(file));

    fclose(file);
    fclose(file_out);
    return 0;
}
