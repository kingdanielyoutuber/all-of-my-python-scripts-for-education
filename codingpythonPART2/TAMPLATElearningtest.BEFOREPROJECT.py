import tkinter as tk

# יצירת חלון המשחק
root = tk.Tk()
root.title("תבנית צבעים ב-Tkinter")
root.geometry("400x300")

# יצירת מסגרת
frame = tk.Frame(root, background="YELLOW", padx=10, pady=10) #you can also say instead of backgroud bg
frame.pack(expand=True, fill="both")

# יצירת תווית
label = tk.Label(frame, text="בחר צבע מהרשימה!", font=("Aharoni", 14)) #"Aharoni is basically a type of front witch is also used in poerpoint word etc,and right next to it is the size of all of the hole thing"
label.pack()

# פונקציה לשינוי צבע המסגרת
def change_color(color):
    frame.config(bg=color)
    label.config(text=f"הצבע הנוכחי: {color}")

# רשימת צבעים וכפתורים מתאימים
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
for color in colors:
    button = tk.Button(frame, text=color, bg=color, font=("Arial", 12), command=lambda c=color: change_color(c))
    button.pack(side="left", padx=5, pady=5)

# הפעלת הלולאה הראשית של Tkinter
root.mainloop()