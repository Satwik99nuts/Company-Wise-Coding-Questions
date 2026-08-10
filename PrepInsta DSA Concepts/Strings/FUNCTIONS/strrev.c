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

void my_strrev(char *s)
{
    int start = 0, end = my_strlen(s) - 1;
    while (start < end)
    {
        char temp = s[start];
        s[start] = s[end];
        s[end] = temp;
        start++;
        end--;
    }
}

int main()
{
    char sample[] = "cat";
    my_strrev(sample);
    printf("Reversed string is %s\n", sample);
    return 0;
}

// my_strrev("cat") -> "tac"
