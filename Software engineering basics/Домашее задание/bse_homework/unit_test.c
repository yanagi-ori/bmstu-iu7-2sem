//
// Created by yanag on 6/5/2020.
//

#include <stdio.h>
#include <string.h>
#include "convert.h"

void test_get_length()
{
    int error_cnt = 0;
    if (get_length("110101") != 6)
    {
        error_cnt++;
    }
    if (get_length("1110") != 4)
    {
        error_cnt++;
    }
    if (get_length("111") != 3)
    {
        error_cnt++;
    }
    if (get_length("0") != 1)
    {
        error_cnt++;
    }

    printf("%s: %s\n", __func__, error_cnt ? "FAILED" : "OK");
}

void test_is_len_multiple_of_four()
{
    int error_cnt = 0;
    if (is_len_multiple_of_four(6) != 0)
    {
        error_cnt++;
    }
    if (is_len_multiple_of_four(4) != 1)
    {
        error_cnt++;
    }
    if (is_len_multiple_of_four(1) != 0)
    {
        error_cnt++;
    }
    printf("%s: %s\n", __func__, error_cnt ? "FAILED" : "OK");
}

void test_normalization()
{
    int error_cnt = 0;
    char ed[81] = {'\0'};
    {
        normalization("110101", 2, 6, ed);
        if (strcmp("00110101", ed) != 0)
        {
            error_cnt++;
        }
    }
    char ed1[20] = {'\0'};
    {
        normalization("0", 3, 1, ed1);
        if (strcmp("0000", ed1) != 0)
        {
            error_cnt++;
        }
    }
    printf("%s: %s\n", __func__, error_cnt ? "FAILED" : "OK");
}

void test_to_tetrads()
{
    int error_cnt = 0;
    char tetrad_array[20][5] = {{'\0'}};
    if (to_tetrads("00110101", tetrad_array) != 2)
    {
        error_cnt++;
    }
    if (to_tetrads("1110", tetrad_array) != 1)
    {
        error_cnt++;
    }
    if (to_tetrads("0000", tetrad_array) != 1)
    {
        error_cnt++;
    }
    printf("%s: %s\n", __func__, error_cnt ? "FAILED" : "OK");
}

void test_to_hex()
{
    int error_cnt = 0;
    if (to_hex("0011") != '3')
    {
        error_cnt++;
    }
    if (to_hex("1111") != 'F')
    {
        error_cnt++;
    }
    if (to_hex("0000") != '0')
    {
        error_cnt++;
    }
    printf("%s: %s\n", __func__, error_cnt ? "FAILED" : "OK");
}

int main()
{
    test_get_length();
    test_is_len_multiple_of_four();
    test_normalization();
    test_to_tetrads();
    test_to_hex();
}