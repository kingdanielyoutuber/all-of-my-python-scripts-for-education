#1
def lok(w,r):
    print(w**r)
lok(5,8)

#2
def tyu(y,l):
    if y > l:
        print(l-y,"distance")
    else:
        print(y-l,"distance")
tyu(9,7)

#3
def tlo(a):
    print(a = input("wirte here:"))
    if a[0].isupper:
        print("yes")
    else:
        print("no")



num = int(input())
i=0
while i<=num:
    if i%2 ==0:
        print(i)
    i+=1