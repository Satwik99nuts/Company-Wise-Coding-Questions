#include <stdio.h>

int main()
{
    int x = 10;
    int *ptr;

    ptr = &x;
    // also explain the difference in
    // int* ptr = &x;

    printf("%d \n", &x);
    printf("%d \n", ptr);
    printf("%d \n", *&x);
    printf("%d \n", *ptr);
    printf("%d \n", &ptr);

    x = 20;
    *&x = 30;
    *ptr = 40;

    printf("%d \n", x);

    return 0;
}