n = int(input())  

time = list(map(int, input().split())) 


min_time = min(time)
min_time_indices = [i for i, time in enumerate(time) if time == min_time]

if len(min_time_indices) > 1:
    print("Still Aetheria")  
else:
    print(min_time_indices[0] + 1)  
