def fer(list1,list2):
    num = []
    for i,j in zip(list1,list2):
        for num.append(i*j)
    return num
print(fer([5,6],[7,6]))