def vector_sub(list1,list2):
    if len(list1) != len(list2):
        Exception("both list doesn't have same size")
    
    output = [] 
      
    for i in range(len(list1)):
        output.append(list1[i]-list2[i])

    return output

print(vector_sub([1, 2, 3], [4, 5, 6]))