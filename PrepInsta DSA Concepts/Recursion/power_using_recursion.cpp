#include <iostream>
using namespace std;

int power(int x, int n)
{
    if (n != 0)
    {
        return x * power(x, n - 1);
    }
    else
    {
        return 1;
    }
}

int main()
{

    int n = 5;
    int x = 2;
    cout << power(x, n);

    return 0;
}