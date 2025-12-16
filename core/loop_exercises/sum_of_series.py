def series_sum(n):
    total = 0
    for i in range(1,n + 1):
        total = total+i
    return total
    
print(series_sum(10))