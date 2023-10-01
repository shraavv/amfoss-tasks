t=int(input())

for _ in range(t):
    r="amfoss"
    diff=0
    s=input()
    for i in range(6):
        if r[i] != s[i]:
            diff=diff+1
        
    print(diff)
