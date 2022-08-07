from tkinter import *
from tkinter import font

root = Tk()
root.title("Testing")
# setting the backgound of everything
root.configure(background='#2e3440')
root.iconbitmap(r'C:\Users\jodok\Documents\PWManager\lock.ico')


# creating a inputfield and packing it
e = Entry(root, bg="#3b4252", border=False, fg="#ffffff", font=("Roboto"))
e.grid(row=0, column=0, columnspan=3, padx=3, pady=3)


def myClick():
    label = Label(root, text=e.get(), fg="#ffffff",
                  bg="#2e3440", font=("Roboto"))
    label.grid(row=2)


button = Button(root, text="Click", command=myClick, bg="#3b4252", fg="white", border=False,
                activebackground="#434c5e", activeforeground="#ffffff", font=("Roboto"), width=5)
button.grid(row=1, column=0, pady=3)

exitButton = Button(root, text="Exit", command=exit, bg="#3b4252", fg="white", border=False,
                    activebackground="#434c5e", activeforeground="#ffffff", font=("Roboto"), width=5)
exitButton.grid(row=1, column=2, pady=3)


root.mainloop()
