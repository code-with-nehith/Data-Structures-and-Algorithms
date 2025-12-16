def even_numbers(start,end):
    for num in range(start,end+1):
        if num % 2 == 0:
           print(num)

even_numbers(1,20)