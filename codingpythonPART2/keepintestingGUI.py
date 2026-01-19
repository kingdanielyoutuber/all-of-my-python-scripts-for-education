import tkinter as tk

# יצירת חלון המשחק
root = tk.Tk()
root.title("תבנית צבעים ב-Tkinter")
root.geometry("400x300")

# יצירת מסגרת
frame = tk.Frame(root, bg="white", padx=10, pady=10)
frame.pack(expand=True, fill="both")

# יצירת תווית
label = tk.Label(frame, text="בחר צבע מהרשימה!", font=("Arial", 14))
label.pack()

# פונקציה לפתיחת חלון לבחירת צבע
def open_color_picker():
    picker = tk.Toplevel(root)
    picker.title("בחר צבע")
    picker.geometry("250x150")

    tk.Label(picker, text="בחר צבע:", font=("Arial", 12)).pack(pady=5)

    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    for color in colors:
        button = tk.Button(picker, text=color, bg=color, font=("Arial", 12), command=lambda c=color: change_color(c))
        button.pack(side="left", padx=5, pady=5)

# פונקציה לשינוי צבע הרקע
def change_color(color):
    frame.config(bg=color)

# יצירת כפתור לפתיחת בוחר הצבעים
open_picker_button = tk.Button(frame, text="בחר צבע", font=("Arial", 12), command=open_color_picker)
open_picker_button.pack(pady=10)

# הפעלת הלולאה הראשית של Tkinter
root.mainloop()