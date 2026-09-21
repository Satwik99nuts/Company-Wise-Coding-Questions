#include <stdio.h>

/* function declaration */
void swap(int a, int b)
{
    int temp = a;
    a = b;
    b = temp;
}

int main()
{

    /* local variable definition */
    int a = 100;
    int b = 200;

    printf("Before swap, value of a : %d\n", a);
    printf("Before swap, value of b : %d\n", b);

    /* calling a function to swap the values */
    swap(a, b); // this is basically pass by value as we are calling a function 

    printf("After swap, value of a : %d\n", a);
    printf("After swap, value of b : %d\n", b);

    return 0;
}