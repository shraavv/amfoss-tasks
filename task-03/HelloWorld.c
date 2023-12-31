//C program to print all the prime numbers upto n

# include <stdio.h>

int prime(int n);

int main()
{
    int n;
    printf("Enter a number - ");
    scanf("%i", &n);
    for (int i = 2; i <= n; i++)
        if (prime(i))
            printf("%d \n", i);
}

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

