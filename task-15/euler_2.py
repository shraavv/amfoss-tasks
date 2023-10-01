def fibonacci(fib_list):
    sum=0
    for i in fib_list:
        if i % 2 == 0 and i <= n :
            sum+=i
    print(sum)

t=int(input())
for i in range(t):
    n=int(input())
    fib_list = [0, 1]
    while len(fib_list) < n + 1:
        fib_list.append(fib_list[-1] + fib_list[-2])
    fibonacci(fib_list)
    