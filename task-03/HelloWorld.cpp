// C++ program to print all the prime numbers upto n 

#include <bits/stdc++.h>
using namespace std;

int prime(int n)
{
    if (n == 0 || n == 1)
    {
        return 0;
    }
    for (int i = 2;i*i <= n ; i++)
    {
        if (n%i==0)
        {
            return 0;
        }
    }   
    return 1;   
}

int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    for (int i = 2; i <= n; i++)
        if (prime(i))
            cout << i << "\n";
}


