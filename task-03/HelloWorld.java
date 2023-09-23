// Java program to print all the prime numbers upto n

import java.util.Scanner;

public class HelloWorld 
{
    public static void main(String[] args) 
    {
        Scanner number = new Scanner(System.in);
        System.out.println("Enter a number : ");
        int n = number.nextInt();
        number.close();

        for (int i = 2; i <= n; i++) 
        {
            if (prime(i)) 
            {
                System.out.println(i);
            }
        }
    }

    public static boolean prime(int n)
     {
        if (n < 2) 
        {
            return false;
        }
        for (int i = 2; i*i <= n; i++) 
        {
            if (n % i == 0) 
            {
                return false;
            }
        }
        return true;
    }
}