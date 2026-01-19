import tkinter as tk
import random

# יצירת חלון המשחק
root = tk.Tk()
root.title("נחש את המספר!")
root.geometry("300x200")

# יצירת מספר אקראי
secret_number = random.randint(1, 51)

# תווית להצגת ההודעה
message_label = tk.Label(root, text="נחש מספר בין 1 ל-50", font=("Arial", 12))
message_label.pack(pady=10)

# שדה קלט לניחוש
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# פונקציה לטיפול בניחוש
def check_guess():
    guess = entry.get()
    if guess.isdigit(): #isdigit בודק אם המחרוזת בעל ספרות
        guess = int(guess)
        if guess < secret_number:
            message_label.config(text="נסה מספר גבוה יותר!")
        elif guess > secret_number:
            message_label.config(text="נסה מספר נמוך יותר!")
        else:
            message_label.config(text="כל הכבוד! ניחשת נכון!")
            guess_button.config(state="disabled")

# כפתור לניחוש
guess_button = tk.Button(root, text="בדוק ניחוש", font=("Arial", 12), command=check_guess)
guess_button.pack(pady=5)

# הפעלת הלולאה הראשית של Tkinter
root.mainloop()