import sys
import subprocess
import pkg_resources

required = {'cryptography'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import random
import string
from tkinter import *
from tkinter import font
import tkinter
from tkinter.messagebox import showinfo
import cryptography


phabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def firstRun():
    try:
        with open('.temp', 'r+') as file:
            file.close()
            return
    except FileNotFoundError:
        with open('.temp', 'w+') as file:
            subprocess.check_call(["attrib","+H",".temp"])
            file.write("firstRun(True)")
            file.close()
            
            
            
    return

firstRun()

def searchforpassword():
    try:
        with open('PWD', 'r+') as file:
            # Search the a password from the website
            search_window = Toplevel()
            search_window.geometry("330x65")
            search_window.configure(background="#2e3440")
            search_window.title("Search for password")
            search_window.resizable(False, False)
            search_window.iconbitmap(r"lock.ico")
            search_window.attributes('-topmost', True)
            search_window.focus_force()
            search_window.bind('<Escape>', lambda x: search_window.destroy())
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
        with open('PWD', 'w+') as file:
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
    searchresults.focus_force()
    searchresults.bind('<Escape>', lambda x: searchresults.destroy())
    searchresults.update()

    contents = contents.split()
    results_website = ["Website:"]
    results_password = ["Password:"]
    results_username = ["Username:"]
    for i in range(len(contents)):
        if i % 3 == 0:
            if websitesearch == contents[i]:
                results_website.append(contents[i])
                results_username.append(contents[i+1])
                results_password.append(contents[i+2])

    results_website = tkinter.StringVar(value=results_website)
    results_username = tkinter.StringVar(value=results_username)
    results_password = tkinter.StringVar(value=results_password)

    listofresults_website = Listbox(searchresults, bg="#3b4252", fg="white", border=False,
                                    font=("Roboto"), listvariable=results_website, selectmode='single')
    listofresults_website.grid(row=0, column=0)
    listofresults_username = Listbox(searchresults, bg="#3b4252", fg="white", border=False,
                                     font=("Roboto"), listvariable=results_username, selectmode='single')
    listofresults_username.grid(row=0, column=1)
    listofresults_password = Listbox(searchresults, bg="#3b4252", fg="white", border=False,
                                     font=("Roboto"), listvariable=results_password, selectmode='single')
    listofresults_password.grid(row=0, column=2)


def generateRandomPassword():
    global randomgeneratedpassword
    randomgeneratedpassword = ""
    for i in range(20):
        randomgeneratedpassword = randomgeneratedpassword + \
            random.choice(characters)

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
        with open('PWD', 'r+') as file:

            username_ = username.get()
            userwebsite = website.get()

            # Check if the given Website is valid (not Website or doesn't have any spaces)
            if userwebsite == "Website" or userwebsite == "":
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

            # Check the same things exept for the Username
            if username_ == "Username" or username_ == "":
                showinfo(
                    "Error", "Please enter a username (can also be a E-Mail adress)")
                generatePasswordWindow.destroy()
                return
            username_ = list(username_)
            for i in range(len(username_)):
                if username_[i] == " ":
                    showinfo(
                        "Error", "The Username can not contain any empty spaces ' '.")
                    return
            username_ = username.get()

            pWD = ownPassword.get()
            filecontent = file.read()
            file.write('\n' + userwebsite + " " + username_ + " " + pWD)
            generatePasswordWindow.destroy()
            openpasswordcopywindow(pWD, username_, userwebsite)

    except FileNotFoundError:
        with open('PWD', 'w+') as file:
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


def openpasswordcopywindow(userpassword, username_, userwebsite):
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
    copypasswordwindow.bind('<Escape>', lambda x: copypasswordwindow.destroy())

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
    generatePasswordWindow.bind(
        '<Escape>', lambda x: generatePasswordWindow.destroy())

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
root.bind('<Escape>', lambda x: root.destroy())
root.update()

root.mainloop()
