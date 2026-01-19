import tkinter as tk
import random

# יצירת החלון הראשי
root = tk.Tk()
root.title("תפריט ראשי")
root.geometry("300x200")

# פונקציה לפתיחת חלון המשחק בתוך Toplevel
def open_game():
    game_window = tk.Toplevel(root)
    game_window.title("נחש את המספר!")
    game_window.geometry("300x200")

    # יצירת מספר אקראי
    secret_number = random.randint(1, 50)

    # תווית להצגת הודעות
    message_label = tk.Label(game_window, text="נחש מספר בין 1 ל-50", font=("Arial", 12))
    message_label.pack(pady=10)

    # שדה קלט לניחוש
    entry = tk.Entry(game_window, font=("Arial", 12))
    entry.pack(pady=5)

    # פונקציה לטיפול בניחוש
    def check_guess():
        guess = entry.get()
        if guess.isdigit():
            guess = int(guess)
            if guess < secret_number:
                message_label.config(text="נסה מספר גבוה יותר!")
            elif guess > secret_number:
                message_label.config(text="נסה מספר נמוך יותר!")
            else:
                message_label.config(text="כל הכבוד! ניחשת נכון!")
                guess_button.config(state="disabled")
                restart_button.pack(pady=5)  # הצגת כפתור האיפוס

    # פונקציה לאיפוס המשחק
    def restart_game():
        nonlocal secret_number
        secret_number = random.randint(1, 50)
        message_label.config(text="נחש מספר בין 1 ל-50")
        entry.delete(0, tk.END)
        guess_button.config(state="normal")
        restart_button.pack_forget()  # הסתרת כפתור האיפוס

    # כפתור לבדיקה
    guess_button = tk.Button(game_window, text="בדוק ניחוש", font=("Arial", 12), command=check_guess)
    guess_button.pack(pady=5)

    # כפתור לאיפוס (נסתר בהתחלה)
    restart_button = tk.Button(game_window, text="איפוס המשחק", font=("Arial", 12), command=restart_game)

# כפתור לפתיחת חלון המשחק
open_button = tk.Button(root, text="הפעל את המשחק", font=("Arial", 12), command=open_game)
open_button.pack(pady=20)

# הפעלת הלולאה הראשית של Tkinter
root.mainloop()