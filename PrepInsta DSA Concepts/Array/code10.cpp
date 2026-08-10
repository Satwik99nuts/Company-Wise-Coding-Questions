#include <stdio.h>

int main()
{
    int arr[5];

    // Assume that base address of arr is 2000 and size of integer is 32 bit
    arr[0]++;

    printf("%d", arr);

    return 0;
}