#include <stdio.h>

void my_strcpy(char *dest, char *src)
{
    int i = 0;
    while (src[i] != '\0')
    {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}

int main()
{
    char dest[20];
    my_strcpy(dest, "cat");
    printf("Copied string is %s\n", dest);
    return 0;
}

// my_strcpy(dest, "cat") -> dest becomes "cat"
