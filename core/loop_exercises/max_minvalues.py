def get_minimum_value(lst):
    min_value = lst[0]

    for number in lst:
        if number < min_value:
            min_value = number
    
    return min_value

def get_maximum_value(numbers):
    max_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number
    
    return max_value

print(get_minimum_value([1, 2, 5, 9]))

print(get_maximum_value([1, 2, 3, 4, 10]))