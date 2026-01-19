import tkinter as tk
root = tk.Tk()
root.title("MYfirst project")
root.geometry("400x200")

BACKGROUNDframe = tk.Frame(root, background="yellow", padx=10, pady=10) #you can also say instead of backgroud bg
BACKGROUNDframe.pack(expand=True,fill="both")
button = tk.Button(BACKGROUNDframe, text="לחץ כאן")
button.pack(padx=10, pady=5)  # הוספת מרווחים
root.mainloop()