def reverse_list(lst):
    rev = []

    for i in range(len(lst)-1,-1,-1):
        print(i)
        rev.append(lst[i])
    return rev

print(reverse_list([1, 2, 3]))