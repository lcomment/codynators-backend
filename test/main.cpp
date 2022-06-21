#include <cstdio>
#include <iostream>
using namespace std;

extern "C"
{
    int mul(int a, int b)
    {
        cout << a * b << endl;
        return a * b;
    }
}