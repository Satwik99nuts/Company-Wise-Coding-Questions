#include <bits/stdc++.h>
using namespace std;

string repeatString(const string &text, int n)
{
    string result;

    for (int i = 0; i < n; i++)
    {
        result += text;
    }

    return result;
}

int main()
{
    string text;
    int n;

    cout << "Enter the string: ";
    cin >> text;

    cout << "Enter how many times to repeat: ";
    cin >> n;

    if (n < 0)
    {
        cout << "Repeat count cannot be negative." << endl;
        return 1;
    }

    cout << repeatString(text, n) << endl;

    return 0;
}
