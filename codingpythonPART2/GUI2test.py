import tkinter as tk
from tkinter import messagebox

def show_confetti():
    messagebox.showinfo("חגיגה!", "קונפטי 🎉")
def show_confetti2():
    messagebox.showinfo("xxx","to be honest....skibidi tollllllllllieeet")
# יצירת חלון
root = tk.Tk()
root.title("יישום כפתור כיף")

# יצירת כפתור
button = tk.Button(root, text="לחץ עליי!", command=show_confetti)
button.pack(pady=20)
#extra from daniel
button2 = tk.Button(root, text="לא ללחוץ עלי bruh", command=show_confetti2)
button2.pack(pady=20)
root.configure(bg= "yellow")
# הפעלת חלון
root.mainloop()