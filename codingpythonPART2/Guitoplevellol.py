import tkinter as tk

# יצירת החלון הראשי
root = tk.Tk()
root.title("חלון ראשי")
root.geometry("300x200")

# פונקציה לפתיחת חלון חדש
def open_toplevel():
    new_window = tk.Toplevel(root)
    new_window.title("חלון נוסף")
    new_window.geometry("200x150")

    label = tk.Label(new_window, text="זהו חלון Toplevel!", font=("Arial", 12))
    label.pack(pady=10)

    close_button = tk.Button(new_window, text="סגור", command=new_window.destroy)
    close_button.pack(pady=10)

# כפתור לפתיחת חלון נוסף
open_button = tk.Button(root, text="פתח חלון נוסף", font=("Arial", 12), command=open_toplevel)
open_button.pack(pady=20)

# הפעלת הלולאה הראשית של Tkinter
root.mainloop()