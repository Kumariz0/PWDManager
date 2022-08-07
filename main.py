import random
import string
import sys
import time
from tkinter import *
from tkinter import font
from tkinter.messagebox import showinfo

# alphabets = list(string.ascii_letters)
# digits = list(string.digits)
# special_characters = list("!@#$%^&*()")
# characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# def main(file):


#         ans = input("Write 1 to set a new PWD, write 2 to search for a PWD\n")
#         #Set a new password
#         if(ans == "1"):
#             website = input("Website: ")
#             pWD = input("Password:      (write '-' to generate a random 20 character password)\n")
#             content = file.read()
#             if content == "":
#                 file.write(website + " " + pWD)
#             elif pWD == "-":
#                 pWD = ""
#                 for i in range(20):
#                     pWD = pWD + random.choice(characters)

#                 file.write('\n' + website+ " " + pWD)
#             else:
#                 file.write('\n' + website+ " " + pWD)

#         #Search the a password from the website
#         elif (ans == "2"):
#             website = input("Website:")
#             content = file.read()
#             content = content.split()
#             print(content)
#             for i in range(len(content)):
#                 if i % 2 != 0:
#                     if website == content[i]:
#                         print(content[i + 1])


#         file.close()
# # end main




def searchforpassword():
    """
    Purpose: Searches for a password in PWDs.txt
    """
    try:
        with open('PWDs.txt', 'r+') as file:
            #Search the a password from the website
            website = input("Website:")
            content = file.read()
            content = content.split()
            print(content)
            for i in range(len(content)):
                if i % 2 != 0:
                    if website == content[i]:
                        print(content[i + 1])
                        
            file.close()
    except:
        with open('PWDs.txt', 'w+') as file:
            showinfo("Alert", "Couldn't find the Password file. Created a new one")
    return
# end def


root = Tk()

# Get the screen size and set the window as the screen size divided by 3
w = int(root.winfo_screenwidth() / 3)
h = int(root.winfo_screenheight() / 3)
size = str(w) + "x" + str(h)
root.geometry(size)
root.resizable(False, False)
root.title("Password manager")

root.configure(background="#2e3440")
root.iconbitmap(r"lock.ico")


searchForPassword = Button(root, text="Search for a password", bg="#3b4252", fg="white", border=False,
                           activebackground="#434c5e", activeforeground="#ffffff", font=("Roboto"), command=searchforpassword)

newPassword = Button(root, text="Create a new password", bg="#3b4252", fg="white", border=False,
                     activebackground="#434c5e", activeforeground="#ffffff", font=("Roboto"))

searchForPassword.place(width=int((w/2) - (w/100 * 2)),
                        height=h-(h/100 * 2), relx=0.01, rely=0.01)
newPassword.place(width=int((w/2) - (w/100 * 2)), height=h -
                  (h/100 * 2), relx=0.51, rely=0.01)

root.mainloop()
