#include <iostream>
using namespace std;

// CALL BY VALUE: x is a copy, the caller's variable is untouched.
void byValue(int x) { x += 10; }

// CALL BY REFERENCE: x is an alias for the caller's variable.
void byReference(int &x) { x += 10; }

// Technically CALL BY VALUE (the address is copied), but dereferencing
// that address modifies the original, so the effect matches by-reference.
void byPointer(int *x) { *x += 10; }

// CALL BY VALUE swap: swaps copies only, does nothing useful.
void swapByValue(int a, int b)
{
    int t = a;
    a = b;
    b = t;
}

// CALL BY REFERENCE swap: actually swaps the caller's variables.
void swapByRef(int &a, int &b)
{
    int t = a;
    a = b;
    b = t;
}

int main()
{
    int n = 5;

    byValue(n);
    cout << "after byValue: " << n << endl; // 5

    byReference(n);
    cout << "after byReference: " << n << endl; // 15

    byPointer(&n);
    cout << "after byPointer: " << n << endl; // 25

    int a = 1, b = 2;
    swapByValue(a, b);
    cout << "after swapByValue: " << a << " " << b << endl; // 1 2

    swapByRef(a, b);
    cout << "after swapByRef: " << a << " " << b << endl; // 2 1

    return 0;
}