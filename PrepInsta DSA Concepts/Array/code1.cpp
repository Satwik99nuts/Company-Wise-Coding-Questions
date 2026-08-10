#include <stdio.h>

int main()
{
    int arr[5];

    // Assume base address of arr is 2000 and size of integer is 32 bit

    printf("%u %u", arr + 1, &arr + 1);

    return 0;
}