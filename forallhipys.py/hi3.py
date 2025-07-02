#3
ah = int(input("number1 here:"))
ho = int(input("number2 here:"))
if ah < ho:
    print("number 2 is bigger")
elif ah > ho:
    print("number1 is bigger")
else:
    print("there equal")

#5
wop = int(input("birth year:"))
hm = 2024
age = hm - wop
if age <18:
    print(age,"years left until you can vote")
else:
    print("you at the right age to vote")