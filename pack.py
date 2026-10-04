from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("tkinter")
root.geometry("500x500")




MainTitle = Label(root,text="Tkinter GUI Programme", bg="black", fg="white", font=("Arial", 100 , "bold"))
MainTitle.pack(fill=BOTH , expand=True , pady=200)


Title1 = Label(root,text="account")
Title1.pack()

Input = Entry(root , width=50 , bg="white" , fg="blue")
Input.pack()

Title2 =  Label(root , text="password")
Title2.pack()

Input = Entry(root , width=50 , bg="white" , fg="blue")
Input.pack()

def handleClick() :
    pass

button = Button(root,text="login",command=handleClick)
button.pack







def handleClick() : 
    messagebox.showinfo("notification","good luck")

button = Button(root,text="click",command=handleClick)
button.pack()






























root.mainloop()