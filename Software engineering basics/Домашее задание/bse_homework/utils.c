/*!
 \file
 \brief Основные функции

 @details Файл содерджит основные функции, обеспечивающие счивание строки, ее обработку и последующу запись в новый файл
 */

#include <stdio.h>
#include "utils.h"
#include "convert.h"
#include <string.h>

#define ERROR_INCORRECT_NUM -20 //!< Число не соответствует правилам записи двоичного числа
#define WARN_EMPTY_STRING -2 //!< Предупреждение о пустой строке
#define ERROR_CONVERT -30 //!< Ошибка при переводе из двоичной системы счисления в шестнадцатеричную
#define ERROR_IO -12 //!< Ошибка чтения/записи


/*!
 * @brief Считывает строку файла
 * @param [IN] file - файловая переменная
 * @param [OUT] bin - двоичное число из файла
 * @return Коды ошибок ERROR_INCORRECT_NUM и WARN_EMPTY_STRING
 */
int get_row(FILE *file, char bin[81])
{
    int i = 0;
    int rc = 0;

    fscanf(file, "%s\n", bin);
    int len = (int) strlen(bin);

    if (len > 80){
        return ERROR_INCORRECT_NUM;
    }

    while (i < len)
    {
        if (bin[i] != '0' && bin[i] != '1' && bin[i] != '\n')
        {
            return ERROR_INCORRECT_NUM;
        }
        else
        {
            i++;
        }
        if (i > 80)
        {
            return ERROR_INCORRECT_NUM;
        }
    }
    if (i == 0)
    {
        rc = WARN_EMPTY_STRING;
    }
    return rc;
}


/*!
 * @brief Функция перевода двоичного числа в шестнадцатеричную систему счисления. Блок А2
 * @param [IN] bin - двоичное число
 * @param [OUT] hex - шестнадцатеричное число
 * @return Код ошибки ERROR_CONVERT при ошибке перевода
 */
int bin_to_hex(char bin[], char hex[])
{
    int len = get_length(bin);
    char tetrads_array[20][5];
    char ed_bin[81] = {'\0'};
    int num_of_tetrads;

    if (is_len_multiple_of_four(len) == 0)
    {
        normalization(bin, 4 - len % 4, len, ed_bin);
        num_of_tetrads = to_tetrads(ed_bin, tetrads_array);
    }
    else
    {
        num_of_tetrads = to_tetrads(bin, tetrads_array);
    }

    int i = 0;
    while (i < num_of_tetrads)
    {
        hex[i] = to_hex(tetrads_array[i]);
        if (hex[i] == '\0')
        {
            return ERROR_CONVERT;
        }
        i++;
    }
    return 0;
}


/*!
 * @brief Записывает строку в новый файл
 * @param [IN] file - файловая переменная output-файла
 * @param [IN] hex - шетснадцатеричное число
 * @return Код ошибки ERROR_IO при пробелмах записи в файл
 */
int write_row(FILE *file, char hex[21])
{
    int rc;
    rc = fputs(hex, file);
    if (rc == EOF)
    {
        return ERROR_IO;
    }
    rc = fputc('\n', file);
    if (rc == EOF)
    {
        return ERROR_IO;
    }
    return 0;
}