def pick_alternate(lst):
    result = []

    # range(9, 9, 2)
    for i in range(1, len(lst), 2):
        print(i)
        result.append(lst[i])

    return result


lst= [9, 2, 3, 4, 5, 6, 7, 11, 9, 10]

output = pick_alternate(lst)

print("Alternate elements starting from 2:", output)

