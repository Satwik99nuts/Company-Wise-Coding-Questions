#include <stdio.h>

int main()
{
    int arr[5] = {
        10,
        20,
        30,
        40,
        50};

    // Assume base address of arr is 2000 and size of integer is 32 bit

    printf("%d", arr[1 + 3]);

    return 0;
}