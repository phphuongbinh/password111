from tkinter import *



root = Tk()
root.title("list box")
root.geometry("500x500")

listbox = Listbox(root, bg = "black", fg = "white", width = 50 , heigh = 30)
listbox.pack()


listbox.insert(0,"")

input = Entry(root, width = 50 )
input.pack()

def handleClick() : 
    text = input.get()
    listbox.insert(END, text)

press = Button(root, text = "add list", command = handleClick , height = 5 , width = 10 )
press.pack()



def handleDelete() : 
    selected = listbox.curselection()
    listbox.delete(END)




delete = Button(root, text = "delete", command = handleDelete)
delete.pack()


root.mainloop()