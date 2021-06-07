from tkinter import *
root = Tk()
root.title("Currency Converter Login Form")
root.geometry("500x400")
canvas = Canvas(bg='#17BEBB', height=250, width=300)
canvas.pack(expand= YES, fill=BOTH)
# adding label widgets

l1 = Label(root, text="Please Enter Username")
l1.place(x=5, y=5)
e1 = Entry(root)
e1.place(x=200, y=5)

l2 = Label(root, text="Please Enter Password")
l2.place(x=5, y=50)
e2 = Entry(root, show="*")
e2.place(x=200, y=50)




def login():
    # importing message box
    from tkinter import messagebox
    Username = ["Zipho", "Masimthembe", "Lihle", "Karabo", "Thandokazi"]
    Password = ["555", "333", "200", "1234", "221"]
    # boolean variable
    found = False
    for x in range(len(Username)):
        if e1.get()==Username[x] and e2.get()==Password[x]:
            found=True
    if found==True:
        messagebox.showinfo("PERMISSION", "Access Granted")
        root.destroy()
        import main
    else:
        messagebox.showinfo("ERROR INFO", "Access Denied")


def clear():
    e1.delete(0,END)
    e2.delete(0, END)

btn1 = Button(root, text="Verify", borderwidth=5, command=login)
btn1.place(x=5, y=250)

btn2 = Button(root, text="Clear", borderwidth=5, command=clear)
btn2.place(x=300, y=250)
root.mainloop()





