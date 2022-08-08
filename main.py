import random
import string
from tkinter import *
from tkinter import font
import tkinter
from tkinter.messagebox import showinfo


phabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

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
            # Search the a password from the website
            search_window = Toplevel()
            search_window.geometry("330x65")
            search_window.configure(background="#2e3440")
            search_window.title("Search for password")
            search_window.resizable(False, False)
            search_window.iconbitmap(r"lock.ico")
            search_window.attributes('-topmost', True)
            search_window.update()

            searchEntry = Entry(search_window, font=(
                "Roboto"), background="#3b4252", fg="#ffffff", width=35, border=False, disabledbackground="#bf616a")
            searchEntry.grid(row=0, column=0,
                             padx=4, pady=4)
            searchEntry.insert(0, "Enter website")
            search_window.bind(
                '<FocusIn>', lambda x: searchEntry.delete(0, END))
            search_window.bind('<Return>', lambda x: enterbutton.invoke())

            contents = file.read()

            enterbutton = Button(search_window, text="Continue", bg="#3b4252", fg="white", border=False,
                                 activebackground="#434c5e", activeforeground="#ffffff", font=("Roboto"), width=35, command=lambda: [openSearchResults(contents, searchEntry.get()), search_window.destroy()])
            enterbutton.grid(row=1, column=0, padx=4, pady=4, sticky=W)

            file.close()
    except FileNotFoundError:
        with open('PWDs.txt', 'w+') as file:
            showinfo(
                "Alert", "Couldn't find the Password file. Created a new one.\nPlease try again")
    return


def openSearchResults(contents, websitesearch):
    searchresults = Toplevel()
    searchresults.resizable(False, False)
    searchresults.title("Password search result for: " + websitesearch)
    searchresults.configure(background="#2e3440")
    searchresults.iconbitmap(r"lock.ico")
    searchresults.attributes('-topmost', True)
    searchresults.update()

    contents = contents.split()
    results_website = ["Website"]
    results_password = ["Password"]
    for i in range(len(contents)):
        if i % 2 == 0:
            if websitesearch == contents[i]:
                results_website.append(contents[i])
                results_password.append(contents[i+1])
                
    results_website = tkinter.StringVar(value=results_website)
    results_password = tkinter.StringVar(value=results_password)
    
    listofresults = Listbox(searchresults, bg="#3b4252", fg="white", border=False,
                            font=("Roboto"), listvariable=results_website, selectmode='single')
    listofresults.grid(row=0,column=0)
    listofresults = Listbox(searchresults, bg="#3b4252", fg="white", border=False,
                            font=("Roboto"), listvariable=results_password, selectmode='single')
    listofresults.grid(row=0,column=1)


def generateRandomPassword():
    global randomgeneratedpassword
    randomgeneratedpassword = ""
    for i in range(20):
        randomgeneratedpassword = randomgeneratedpassword + random.choice(characters)

    ownPassword.delete(0, END)
    ownPassword.insert(0, randomgeneratedpassword)


def entryDisable(value, ownPassword):

    generateRandomPassword()

    entryDisabled = value
    if value == 0:
        ownPassword.config(state=NORMAL)
    if value == 1:
        ownPassword.config(state=DISABLED)

    return entryDisabled


def writeuserdataToFile():

    try:
        with open('PWDs.txt', 'r+') as file:

            username_ = username.get()
            userwebsite = website.get()
            if userwebsite == "Website":
                showinfo("Error", "Please enter a website")
                generatePasswordWindow.destroy()
                return
            userwebsite = list(userwebsite)
            for i in range(len(userwebsite)):
                if userwebsite[i] == " ":
                    showinfo(
                        "Error", "The website can not contain any empty spaces ' '.")
                    return
            userwebsite = website.get()

            pWD = ownPassword.get()
            filecontent = file.read()
            file.write
            file.write('\n' + userwebsite + " " + pWD)
            generatePasswordWindow.destroy()
            openpasswordcopywindow(pWD, username_)

    except FileNotFoundError:
        with open('PWDs.txt', 'w+') as file:
            showinfo(
                "Alert", "Couldn't find the Password file. Created a new one.\nPlease try again after adding some Passwords")
            exit()


def copytext(text):
    hiddenwindow = Toplevel()
    hiddenwindow.withdraw()
    hiddenwindow.clipboard_clear()
    hiddenwindow.clipboard_append(text)
    hiddenwindow.update()
    hiddenwindow.destroy()


def openpasswordcopywindow(userpassword, username_):
    global copypasswordwindow
    copypasswordwindow = Toplevel()

    # Get the screen size and set the window as the screen size
    w = int(root.winfo_screenwidth() / 4)
    h = int(root.winfo_screenheight() / 12)
    size = str(w) + "x" + str(h)
    copypasswordwindow.geometry(size)
    copypasswordwindow.resizable(False, False)
    copypasswordwindow.title("Copy your password")

    copypasswordwindow.configure(background="#2e3440")
    copypasswordwindow.iconbitmap(r"lock.ico")

    copypasswordwindow.after(
        1, lambda: copypasswordwindow.focus_force())

    copypasswordfield = Entry(copypasswordwindow, font=(
        "Roboto"), background="#3b4252", fg="#ffffff", width=36, border=1, disabledbackground="#bf616a")
    copypasswordfield.grid(row=1, sticky=W, columnspan=2)
    copypasswordfield.insert(0, userpassword)
    copypasswordfield.bind('<1>', lambda text: copytext(userpassword))
    copypasswordfield.bind(
        '<FocusIn>', lambda x: copypasswordfield.selection_range(0, END))

    usernamefield = Entry(copypasswordwindow, font=(
        "Roboto"), background="#3b4252", fg="#ffffff", width=36, border=1, disabledbackground="#bf616a")
    usernamefield.grid(row=0, columnspan=2, sticky=W)
    usernamefield.insert(0, username_)
    usernamefield.bind('<1>', lambda text: copytext(username_))
    usernamefield.bind(
        '<FocusIn>', lambda x: usernamefield.selection_range(0, END))

    continue_button = Button(copypasswordwindow, text="Continue", bg="#3b4252", fg="white", border=False,
                             activebackground="#434c5e", activeforeground="#ffffff", font=("Roboto"), command=copypasswordwindow.destroy, width=17).grid(row=2, column=1, pady=0.5)

    exit = Button(copypasswordwindow, text="Exit", bg="#3b4252", fg="white", border=False,
                  activebackground="#434c5e", activeforeground="#ffffff", font=("Roboto"), command=root.destroy, width=17).grid(row=2, column=0, pady=0.5)

    copypasswordwindow.attributes('-topmost', True)
    copypasswordwindow.update()


def createnewPassword():
    global generatePasswordWindow
    generatePasswordWindow = Toplevel()

    # Get the screen size and set the window as the screen size divided by 3
    w = int(root.winfo_screenwidth() / 4)
    h = int(root.winfo_screenheight() / 5.5)
    size = str(w) + "x" + str(h)
    generatePasswordWindow.geometry(size)
    generatePasswordWindow.resizable(False, False)
    generatePasswordWindow.title("Generate new Password")

    generatePasswordWindow.configure(background="#2e3440")
    generatePasswordWindow.iconbitmap(r"lock.ico")

    var = IntVar()

    global website
    website = Entry(generatePasswordWindow, font=(
        "Roboto"), background="#3b4252", fg="#ffffff", width=36, border=1, disabledbackground="#bf616a")
    website.grid(row=0, column=0, sticky=W)
    website.insert(0, "Website")
    global clickedwebsite
    clickedwebsite = website.bind('<FocusIn>', clickWebsite)

    global username
    username = Entry(generatePasswordWindow, font=(
        "Roboto"), background="#3b4252", fg="#ffffff", width=36, border=1, disabledbackground="#bf616a")
    username.grid(row=1, column=0, sticky=W)
    username.insert(0, "Username")
    global clickedusername
    clickedusername = username.bind('<FocusIn>', clickusername)

    global ownPassword
    ownPassword = Entry(generatePasswordWindow, font=(
        "Roboto"), background="#3b4252", fg="#ffffff", width=36, border=False, disabledbackground="#bf616a")
    ownPassword.grid(row=2, sticky=W)

    useOwnPassword = Radiobutton(generatePasswordWindow, text="Use own password", variable=var, value=1, font=(
        "Roboto"), background="#2e3440", fg="#ffffff", width=35, selectcolor="#2e3440", activebackground="#2e3440", activeforeground="#ffffff", anchor=W, command=lambda: entryDisable(0, ownPassword))
    useOwnPassword.grid(row=3)
    generatethepassword = Radiobutton(generatePasswordWindow, text="Generate a 20 char random password", variable=var, value=2, font=(
        "Roboto"), background="#2e3440", fg="#ffffff", width=35, selectcolor="#2e3440", activebackground="#2e3440", activeforeground="#ffffff", anchor=W, command=lambda: entryDisable(1, ownPassword))
    generatethepassword.grid(row=4)

    generatethepassword.invoke()
    generatethepassword.select()

    createPassword = Button(generatePasswordWindow, text='Enter', bg="#3b4252", fg="white", border=False,
                            activebackground="#434c5e", activeforeground="#ffffff", font=("Roboto"), width=35, command=lambda: writeuserdataToFile())
    createPassword.grid(row=5, column=0, sticky=W)

    generatePasswordWindow.after(
        1, lambda: generatePasswordWindow.focus_force())

    generatePasswordWindow.attributes('-topmost', True)
    generatePasswordWindow.update()


def clickWebsite(event):
    website.configure(state=NORMAL)
    website.delete(0, END)
    website.unbind('<Button-1>', clickedwebsite)


def clickusername(event):
    username.config(state=NORMAL)
    username.delete(0, END)
    username.unbind('<button-1>', clickedusername)


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
                           activebackground="#434c5e", activeforeground="#ffffff", font=("Roboto"), command=lambda: [searchforpassword(), root.attributes('-topmost', False)])

newPassword = Button(root, text="Create a new password", bg="#3b4252", fg="white", border=False,
                     activebackground="#434c5e", activeforeground="#ffffff", font=("Roboto"), command=lambda: [createnewPassword(), root.attributes('-topmost', False)])

searchForPassword.place(width=int((w/2) - (w/100 * 2)),
                        height=h-(h/100 * 2), relx=0.01, rely=0.01)
newPassword.place(width=int((w/2) - (w/100 * 2)), height=h -
                  (h/100 * 2), relx=0.51, rely=0.01)
root.attributes('-topmost', True)
root.update()

root.mainloop()
