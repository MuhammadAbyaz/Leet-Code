#include <iostream>
#include <math.h>
#include <typeinfo>

using namespace std;
bool isPowerOfTwo(int n)
{
    if (n == 0 || n < 0)
        return false;
    double fractionalPart = log2(n) - int(log2(n));
    if (fractionalPart == 0.0)
        return true;
    else
        return false;
}

int main()
{
    cout << isPowerOfTwo(-16);
    return 0;
}