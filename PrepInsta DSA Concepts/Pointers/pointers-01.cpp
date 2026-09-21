#include <stdio.h>

int main()
{
    int x;

    printf("%d\n", &x);
    printf("%p\n", &x);

    x = 10;

    printf("The address in decimal: %d\n", &x);
    printf("The address in hexa: %p\n", &x);

    printf("The value at address: %p is : %d\n", &x, *&x);
    printf("The value at address: %p is : %d\n", &x, x);

    return 0;
}