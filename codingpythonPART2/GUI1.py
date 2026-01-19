from tkinter import * #this is after hi15.py

root = Tk()
root.title("title my first GUI!")
root.geometry("350x200")
lp = Label(root,text= "Welcome to my first code!", font= ('Algerian',20,'bold'), bg = 'red',height = 2,fg = 'white',padx = 100,pady = 20)
lp.pack()
pkl = Button(root, text = 'click me!')
pkl.pack()
inp = Entry(root)
inp.pack()
txs = Text(root)
txs.pack()







root.mainloop()