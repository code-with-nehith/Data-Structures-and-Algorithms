def find_number(lst):
    for num in lst:
        if num > 20:
            print("Found it!")
            break


numbers = [3, 8, 15, 20, 25, 30]
find_number(numbers)
