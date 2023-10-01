s = input()  
x= 0


for i in s:
    if i == "h" and x == 0:
        x += 1
    elif i == "e" and x == 1:
        x += 1
    elif i == "l" and x == 2:
        x += 1
    elif i== "l" and x == 3:
        x += 1
    elif i == "o" and x == 4:
        x += 1


if x == 5:
    print("YES")  
else:
    print("NO")  

