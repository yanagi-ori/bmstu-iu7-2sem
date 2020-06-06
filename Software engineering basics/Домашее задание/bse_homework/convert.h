/*!
 * @file Заголовочный файл convert
 */


int get_length(const char *bin);

int is_len_multiple_of_four(int len);

void normalization(const char *bin, int add, int len, char *ed);

int to_tetrads(char *bin, char array_of_tetrads[20][5]);

char to_hex(char tetrad[5]);