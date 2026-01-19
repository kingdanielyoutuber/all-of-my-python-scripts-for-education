import tkinter as tk

# יצירת חלון ראשי
root = tk.Tk()
root.title("Tkinter Template")
root.geometry("300x200")

# יצירת מסגרת
frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame.pack(pady=70)

# יצירת תווית
label = tk.Label(frame, text="ברוך הבא לטקינטר!", font=("Arial", 12))
label.pack()

# יצירת כפתור
def on_but(): #on_but איך שקראתי לנעלם
    label.config(text="לחצת על הכפתור!")

button = tk.Button(frame, text="לחץ כאן", command=on_but)
button.pack(pady=10)

# הפעלת הלולאה הראשית של Tkinter
root.mainloop()