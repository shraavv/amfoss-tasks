def is_equilibrium(vectors):
    
    sum_x = sum_y = sum_z = 0
    
    
    for i in vectors:
        sum_x += i[0]
        sum_y += i[1]
        sum_z += i[2]
    
    if sum_x == sum_y == sum_z == 0:
        return "YES"  
    else:
        return "NO"   

n = int(input())


vectors= []
for j in range(n):
   i= list(map(int, input().split()))
   vectors.append(i)


result = is_equilibrium(vectors)
print(result)
