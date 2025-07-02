grades = {"avi":90, "yonatan":87, "bob":11, "moria":70}
print(grades["bob"])
print(grades.keys())
print(grades.values())
print(grades.get("moria"))
print(grades.get("israel"))
print("avi" in grades)
print("yosi" in grades)
print(grades)
grades.pop("bob")


print("               ")



d = {"ariel":92, "yosi":78, "israel":88, "bob":99, "moria":100}
for value in d.values():
    if value > 90:
        print("all of those grades are above 90:",value)