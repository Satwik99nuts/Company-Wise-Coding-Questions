#include <stdio.h>

int my_strlen(char *s)
{
    int count = 0;
    while (s[count] != '\0')
    {
        count++;
    }
    return count;
}

int main()
{
    char sample[] = "cat";
    printf("Length of %s is %d\n", sample, my_strlen(sample));
    return 0;
}

// my_strlen("cat") -> 3
