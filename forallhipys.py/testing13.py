def calc(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum / len(lst)

grade1 = [76,98,23,54]
grade2 = [99,100,34,67,89,75]

average1 = calc(grade1)
print("classic",average1)

#average2 = calc(grade1)
print("class 2:",calc(grade2))