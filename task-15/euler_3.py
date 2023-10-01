def prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

t=int(input())
for i in range(t):
    n=int(input())
    print(prime_factor(n))