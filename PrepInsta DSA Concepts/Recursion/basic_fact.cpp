#include <iostream>
using namespace std;

int factorial(int n)
{
    if (n > 1)
    {
        return n * factorial(n - 1);
    }
    else
    {
        return 1;
    }
}

int main()
{
    // Write C++ code here
    int n = 5;
    cout << factorial(n);

    return 0;
}