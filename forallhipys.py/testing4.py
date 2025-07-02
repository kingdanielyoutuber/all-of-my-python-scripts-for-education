a = "hello"
x = len(a)
print(a[4])
print(a[x-1])

print("                    ")
a = "hello"
print(a.upper())
print(a.lower())



print("                          ")


a = "abcdefg"
print(a.find("ab"))
print(a.find("de"))
print(a.find("xyz"))

print("                       ")

word = "Hello wHrld"

print(word.replace("h","J"))





#1 and 2.
lpok = {"bob":45,"dad":89,"dan":100,"robie":67}
for value in lpok.values():
    if(value<80):
        print("grades under 80:",value)
    elif(value>90):
        print("garde above 90:",value)