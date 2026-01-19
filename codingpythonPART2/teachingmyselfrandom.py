import random #random הוא ספרייה שצריך להכניס

# יצירת מספר אקראי בין 1 ל-100
random_number = random.randint(1, 100)
print(f"מספר אקראי: {random_number}")

# בחירת פריט אקראי מתוך רשימה
items = ["תפוח", "בננה", "ענבים", "אבטיח"]
random_item = random.choice(items)
print(f"פריט אקראי: {random_item}")

# ערבוב רשימה
random.shuffle(items)
print(f"רשימה מעורבבת: {items}")