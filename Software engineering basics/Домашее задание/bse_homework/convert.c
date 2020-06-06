/*!
 @file
 @brief Базовые опреации для ообработки двоичного числа

 @details В этом файле описаны функции для перевода двоичного числа в шетснадцатеричну систему счисления.
 Блок А2 по декомпозиции IDEF0.
 */

#include "convert.h"
#include <string.h>


/*!
 * @brief Находит длину двоичного числа
 * @param [IN] bin - двоичное число
 * @return Длину доичного числа
 */
int get_length(const char *bin)
{
    int len = 0;

    while (bin[len] != '\0' && bin[len] != '\n')
    {
        len++;
    }

    return len;
}


/*!
 * @brief Проверка кратности 4.
 * @details Функция, проверящая кратность длины двоичного числа четырем
 * @param [IN] len - длина двоичного числа
 * @return 1, если кратно 4, 0 - если нет
 */
int is_len_multiple_of_four(int len)
{
    int bool = 0; // 0 is no and 1 is yes

    if (len % 4 == 0)
    {
        bool = 1;
    }

    return bool;
}


/*!
 * @brief Нормализует двоичное число
 * @details Функция добавляет необходимое количество нулей для кратоности числа четырем
 * @param [IN] bin - исходное двоичное число
 * @param [IN] add - количество добавляемых нулей
 * @param [IN] len - длина исходного двоичного числа
 * @param [OUT] ed - измененное двоичное число
 * @return Нормализированное двоичное число, готовое для перевода в шестнадцатеричную систему
 */
void normalization(const char *bin, int add, int len, char *ed)
{
    int n = 0;

    while (n < add)
    {
        ed[n] = '0';
        n++;
    }

    int i = 0;
    while (i < len)
    {
        ed[n + i] = bin[i];
        i++;
    }
}


/*!
 * @brief Разбивает двоичное число на тетрады
 * @param [IN] bin - двоичное число
 * @param [OUT] array_of_tetrads - массив тетрад
 * @return Количество тетрад
 */
int to_tetrads(char *bin, char array_of_tetrads[20][5])
{
    int len = get_length(bin);
    int n = 0, i = 0;
    int k;

    while (i < len)
    {
        k = 0;
        while (k < 4)
        {
            array_of_tetrads[n][k] = bin[i];
            i++;
            k++;
        }
        n++;
    }
    return n;
}


/*!
 * @brief Табличный перевод в 16ную систему
 * @details Функция преобразует тетраду двоичного числа в 16чное путем табличного перевода
 * @param tetrad - тетрада
 * @return Код ошибки - пустой символ
 */
char to_hex(char *tetrad)
{
    if (strncmp(tetrad, "0000", 4) == 0)
    {
        return '0';
    }
    if (strncmp(tetrad, "0001", 4) == 0)
    {
        return '1';
    }
    if (strncmp(tetrad, "0010", 4) == 0)
    {
        return '2';
    }
    if (strncmp(tetrad, "0011", 4) == 0)
    {
        return '3';
    }
    if (strncmp(tetrad, "0100", 4) == 0)
    {
        return '4';
    }
    if (strncmp(tetrad, "0101", 4) == 0)
    {
        return '5';
    }
    if (strncmp(tetrad, "0110", 4) == 0)
    {
        return '6';
    }
    if (strncmp(tetrad, "0111", 4) == 0)
    {
        return '7';
    }
    if (strncmp(tetrad, "1000", 4) == 0)
    {
        return '8';
    }
    if (strncmp(tetrad, "1001", 4) == 0)
    {
        return '9';
    }
    if (strncmp(tetrad, "1010", 4) == 0)
    {
        return 'A';
    }
    if (strncmp(tetrad, "1011", 4) == 0)
    {
        return 'B';
    }
    if (strncmp(tetrad, "1100", 4) == 0)
    {
        return 'C';
    }
    if (strncmp(tetrad, "1101", 4) == 0)
    {
        return 'D';
    }
    if (strncmp(tetrad, "1110", 4) == 0)
    {
        return 'E';
    }
    if (strncmp(tetrad, "1111", 4) == 0)
    {
        return 'F';
    }
    return '\0';
}

