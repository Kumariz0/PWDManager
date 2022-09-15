import os
import shutil
import sys
import subprocess
import pkg_resources

required = {'cryptography', 'pyinstaller'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing])


from cryptography.fernet import Fernet
import urllib.request

url = "https://raw.githubusercontent.com/Kumariz0/PWDManager/master/lock.ico"
print ("download start!")
filename, headers = urllib.request.urlretrieve(url, filename="lock.ico")
print ("download complete!")
print ("download file location: ", filename)
print ("download headers: ", headers)


try:
    os.remove("PWD")
except FileNotFoundError:
    pass

with open ('main.py', "w+") as file:
    file.write("""import sys
import subprocess
import pkg_resources

required = {'cryptography'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed
if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    
from cryptography.fernet import Fernet
from tkinter.messagebox import showinfo
import tkinter
from tkinter import *
import string
import random

compatible = False
phabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

colors = {
    "fg": "#ffffff",
    "bg": "#2e3440",
    "AlertRed": "#bf616a",
    "ConfirmGreen": "#a3be8c"
}



class Encryption():
    global key
    key = """ + str(Fernet.generate_key()) + """
    
    def enrypt(d_content):
        f = Fernet(key)
        return f.encrypt(d_content.encode())
    
    def decrypt(location):
        with open('PWD', 'r+') as file:
            content = file.read().split()
            content[location] = content[location].replace("b", "", 1)
            content[location] = content[location].replace("'", "", 2)
            f = Fernet(key)
            return f.decrypt(content[location])
            
            
    def newfile(u_pwd):        
        f = Fernet(key)
        
        if compatible == True:
            with open('PWD', 'w+') as file:
                file.write(str(f.encrypt(u_pwd.encode())) + " " + str(f.encrypt(b"Hello")) + " " + str(f.encrypt(b"there")))
                exit()
        else: 
            pass
            
            
    def CheckPWD(upwd, parent, searchForPassword, newPassword):
        with open('PWD', 'r+') as file:
            content = file.read().split()
            content[0] = content[0].replace("b", "", 1)
            content[0] = content[0].replace("'", "", 2)
            
            f = Fernet(key)
            pwd = f.decrypt(content[0].encode())

            if pwd.decode() == upwd:
                parent.destroy()
                searchForPassword.config(state=NORMAL)
                newPassword.config(state=NORMAL)
            
class firstrunning:
    
    def checkfirstRun():
        try:
            # when the file exist its not the first run otherwise it is
            with open('PWD', 'r+') as file:
                file.close()
                return 1
        except FileNotFoundError:
            # when the file is not found it will create one and make it invisible. After that it runs firstRun()
            firstrunning.firstRun()

        return
    
    
    def checkCompatibility(content):
        global compatible
        match len(content):
            case 0:
                passwordEntry.config(fg=colors["AlertRed"])
                compatible = False
                return compatible
            case 1:
                passwordEntry.config(fg=colors["AlertRed"])
                compatible = False
                return compatible
            case 2:
                passwordEntry.config(fg=colors["AlertRed"])
                compatible = False
                return compatible
            case 3:
                passwordEntry.config(fg=colors["AlertRed"])
                compatible = False
                return compatible
            case 4:
                passwordEntry.config(fg=colors["AlertRed"])
                compatible = False
                return compatible
            case 5:
                passwordEntry.config(fg=colors["AlertRed"])
                compatible = False
                return compatible
            case 6:
                passwordEntry.config(fg=colors["AlertRed"])
                compatible = False
                return compatible
            case 7:
                passwordEntry.config(fg=colors["AlertRed"])
                compatible = False
                return compatible
            case 8:
                passwordEntry.config(fg=colors["ConfirmGreen"])
                compatible = True
                return compatible
            case 9:
                passwordEntry.config(fg=colors["ConfirmGreen"])
                compatible = True
                return compatible
            case 10:
                passwordEntry.config(fg=colors["ConfirmGreen"])
                compatible = True
                return compatible
            case 11:
                passwordEntry.config(fg=colors["ConfirmGreen"])
                compatible = True
                return compatible
            case 12:
                passwordEntry.config(fg=colors["ConfirmGreen"])
                compatible = True
                return compatible
            case 13:
                passwordEntry.config(fg=colors["ConfirmGreen"])
                compatible = True
                return compatible
            case 14:
                passwordEntry.config(fg=colors["ConfirmGreen"])
                compatible = True
                return compatible
            case 15:
                passwordEntry.config(fg=colors["ConfirmGreen"])
                compatible = True
                return compatible
            case 16:
                passwordEntry.config(fg=colors["ConfirmGreen"])
                compatible = True
                return compatible
            case 17:
                passwordEntry.config(fg=colors["ConfirmGreen"])
                compatible = True
                return compatible
        return compatible
                
                
    def firstRun():
        
        global createnewPassword
        createnewPassword = Tk()
        createnewPassword.configure(background=colors["bg"])
        createnewPassword.resizable(False, False)
        createnewPassword.title("Create manager password")
        createnewPassword.iconbitmap(r"lock.ico")
        createnewPassword.attributes('-topmost', True)
        createnewPassword.focus_force()
        # Adds event to close the window when ESC is pressed
        createnewPassword.bind('<Escape>', lambda x: createnewPassword.destroy())
        createnewPassword.update()
        
        
        global passwordEntry
        passwordEntry = Entry(createnewPassword, font=(
           "Roboto"), background=colors["bg"], fg=colors["fg"], width=35, border=False, disabledbackground=colors["bg"] )
        passwordEntry.grid(row=0, column=0,
                         padx=4, pady=4)
        passwordEntry.insert(0, "Enter Password here")
        createnewPassword.bind(
            '<FocusIn>', lambda x: passwordEntry.delete(0, END))

        note = Label(createnewPassword, text = "NOTE: the password can only contain 4, 8 or 16 characters""" + repr("\n") + """ and it can't contain any spaces", background=colors["bg"], fg=colors["fg"])
        note.grid(row = 1, column = 0)

        enterbutton = Button(createnewPassword, text="Continue", bg="#3b4252", fg="white", border=False,
                             activebackground="#434c5e", activeforeground=colors["fg"], font=("Roboto"), width=35, command=lambda:Encryption.newfile(passwordEntry.get()))
        enterbutton.grid(row=2, column=0, padx=4, pady=4, sticky=W)
        createnewPassword.bind('<Return>', lambda x: enterbutton.invoke())
        
        createnewPassword.bind("<Key>", lambda x: firstrunning.checkCompatibility(passwordEntry.get()))
        
        
        createnewPassword.mainloop()


def searchforpassword():
    try:
        with open('PWD', 'r+') as file:

            search_window = Toplevel()
            search_window.configure(background=colors["bg"])
            search_window.title("Search for password")
            search_window.resizable(False, False)
            search_window.iconbitmap(r"lock.ico")
            search_window.attributes('-topmost', True)
            search_window.focus_force()
            search_window.bind('<Escape>', lambda x: search_window.destroy())
            search_window.update()

            searchEntry = Entry(search_window, font=(
                "Roboto"), background="#3b4252", fg=colors["fg"], width=35, border=False, disabledbackground="#bf616a")
            searchEntry.grid(row=0, column=0,
                             padx=4, pady=4)
            searchEntry.insert(0, "Enter website")
            search_window.bind(
                '<FocusIn>', lambda x: searchEntry.delete(0, END))
            search_window.bind('<Return>', lambda x: enterbutton.invoke())

            contents = file.read()

            enterbutton = Button(search_window, text="Continue", bg="#3b4252", fg="white", border=False,
                                 activebackground="#434c5e", activeforeground=colors["fg"], font=("Roboto"), width=35, command=lambda: [openSearchResults(contents, searchEntry.get()), search_window.destroy()])
            enterbutton.grid(row=1, column=0, padx=4, pady=4, sticky=W)

            file.close()
    except FileNotFoundError:
        with open('PWD', 'w+') as file:
            showinfo(
                "Alert", "Couldn't find the Password file. Created a new one.""" + repr("\n") + """Please try again")
    return


def openSearchResults(contents, websitesearch):

    searchresults = Toplevel()
    searchresults.resizable(False, False)
    searchresults.title("Password search result for: " + websitesearch)
    searchresults.configure(background=colors["bg"])
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
            if websitesearch == Encryption.decrypt(i).decode():
                results_website.append(Encryption.decrypt(i).decode())
                results_username.append(Encryption.decrypt(i+1).decode())
                results_password.append(Encryption.decrypt(i+2).decode())

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
            if username_ == "Username" or username_ == "":
                showinfo(
                    "Error", "Please enter a Website(can also be a service)")
                generatePasswordWindow.destroy()
                return
            

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
            file.write(""" + repr("\n") + """ + str(Encryption.enrypt(userwebsite)) + " " + str(Encryption.enrypt(username_)) + " " + str(Encryption.enrypt(pWD)))
            generatePasswordWindow.destroy()
            openpasswordcopywindow(pWD, username_)

    except FileNotFoundError:
        with open('PWD', 'w+') as file:
            showinfo(
                "Alert", "Couldn't find the Password file. Created a new one.""" + repr("\n") + """Please try again after adding some Passwords")
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

    w = int(1280 / 4)
    h = int(853 / 12)
    size = str(w) + "x" + str(h)
    copypasswordwindow.geometry(size)
    copypasswordwindow.resizable(False, False)
    copypasswordwindow.title("Copy your password")

    copypasswordwindow.configure(background=colors["bg"])
    copypasswordwindow.iconbitmap(r"lock.ico")
    copypasswordwindow.bind('<Escape>', lambda x: copypasswordwindow.destroy())

    copypasswordwindow.after(
        1, lambda: copypasswordwindow.focus_force())

    copypasswordfield = Entry(copypasswordwindow, font=(
        "Roboto"), background="#3b4252", fg=colors["fg"], width=36, border=1, disabledbackground="#bf616a")
    copypasswordfield.grid(row=1, sticky=W, columnspan=2)
    copypasswordfield.insert(0, userpassword)
    copypasswordfield.bind('<1>', lambda text: copytext(userpassword))
    copypasswordfield.bind(
        '<FocusIn>', lambda x: copypasswordfield.selection_range(0, END))

    usernamefield = Entry(copypasswordwindow, font=(
        "Roboto"), background="#3b4252", fg=colors["fg"], width=36, border=1, disabledbackground="#bf616a")
    usernamefield.grid(row=0, columnspan=2, sticky=W)
    usernamefield.insert(0, username_)
    usernamefield.bind('<1>', lambda text: copytext(username_))
    usernamefield.bind(
        '<FocusIn>', lambda x: usernamefield.selection_range(0, END))

    continue_button = Button(copypasswordwindow, text="Continue", bg="#3b4252", fg="white", border=False,
                             activebackground="#434c5e", activeforeground=colors["fg"], font=("Roboto"), command=copypasswordwindow.destroy, width=17).grid(row=2, column=1, pady=0.5)

    exit_button = Button(copypasswordwindow, text="Exit", bg="#3b4252", fg="white", border=False,
                  activebackground="#434c5e", activeforeground=colors["fg"], font=("Roboto"), command=root.destroy, width=17).grid(row=2, column=0, pady=0.5)

    copypasswordwindow.attributes('-topmost', True)
    copypasswordwindow.update()


def createnewPassword():

    
    global generatePasswordWindow
    generatePasswordWindow = Toplevel()

    # Get the screen size and set the window as the screen size divided by 3
    w = int(1280 / 4)
    h = int(853 / 5.5)
    size = str(w) + "x" + str(h)
    generatePasswordWindow.geometry(size)
    generatePasswordWindow.resizable(False, False)
    generatePasswordWindow.title("Generate new Password")

    generatePasswordWindow.configure(background=colors["bg"])
    generatePasswordWindow.iconbitmap(r"lock.ico")
    generatePasswordWindow.bind(
        '<Escape>', lambda x: generatePasswordWindow.destroy())

    var = IntVar()

    global website
    website = Entry(generatePasswordWindow, font=(
        "Roboto"), background="#3b4252", fg=colors["fg"], width=36, border=1, disabledbackground="#bf616a")
    website.grid(row=0, column=0, sticky=W)
    website.insert(0, "Website")
    global clickedwebsite
    clickedwebsite = website.bind('<FocusIn>', clickWebsite)

    global username
    username = Entry(generatePasswordWindow, font=(
        "Roboto"), background="#3b4252", fg=colors["fg"], width=36, border=1, disabledbackground="#bf616a")
    username.grid(row=1, column=0, sticky=W)
    username.insert(0, "Username")
    global clickedusername
    clickedusername = username.bind('<FocusIn>', clickusername)

    global ownPassword
    ownPassword = Entry(generatePasswordWindow, font=(
        "Roboto"), background="#3b4252", fg=colors["fg"], width=36, border=False, disabledbackground="#bf616a")
    ownPassword.grid(row=2, sticky=W)

    useOwnPassword = Radiobutton(generatePasswordWindow, text="Use own password", variable=var, value=1, font=(
        "Roboto"), background=colors["bg"], fg=colors["fg"], width=35, selectcolor=colors["bg"], activebackground=colors["bg"], activeforeground=colors["fg"], anchor=W, command=lambda: entryDisable(0, ownPassword))
    useOwnPassword.grid(row=3)
    generatethepassword = Radiobutton(generatePasswordWindow, text="Generate a 20 char random password", variable=var, value=2, font=(
        "Roboto"), background=colors["bg"], fg=colors["fg"], width=35, selectcolor=colors["bg"], activebackground=colors["bg"], activeforeground=colors["fg"], anchor=W, command=lambda: entryDisable(1, ownPassword))
    generatethepassword.grid(row=4)

    generatethepassword.invoke()
    generatethepassword.select()

    createPassword = Button(generatePasswordWindow, text='Enter', bg="#3b4252", fg="white", border=False,
                            activebackground="#434c5e", activeforeground=colors["fg"], font=("Roboto"), width=35, command=lambda: writeuserdataToFile())
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


def logIn(parent, searchForPassword, newPassword):
    loginW = Toplevel()
    
    loginW.configure(background=colors["bg"])
    loginW.resizable(False, False)
    loginW.title("Login")
    loginW.iconbitmap(r"lock.ico")
    loginW.attributes('-topmost', True)
    loginW.focus_force()
    # Adds event to close the window when ESC is pressed
    loginW.bind('<Escape>', lambda x: loginW.destroy())
    loginW.update()
    
    
    passwordEntry = Entry(loginW, font=(
       "Roboto"), background=colors["bg"], fg=colors["fg"], width=35, border=False, disabledbackground=colors["bg"] )
    passwordEntry.grid(row=0, column=0,
                     padx=4, pady=4)
    passwordEntry.insert(0, "Enter Password here")
    loginW.bind(
        '<FocusIn>', lambda x: passwordEntry.delete(0, END))

    
    enterbutton = Button(loginW, text="Continue", bg="#3b4252", fg="white", border=False,
                         activebackground="#434c5e", activeforeground=colors["fg"], font=("Roboto"), width=35, command=lambda:Encryption.CheckPWD(passwordEntry.get(), loginW, searchForPassword, newPassword))
    enterbutton.grid(row=2, column=0, padx=4, pady=4, sticky=W)
    loginW.bind('<Return>', lambda x: enterbutton.invoke())
    parent.wait_window(loginW)
    
    

if firstrunning.checkfirstRun() == 1:
    root = Tk()


    w = 426
    h = 284
    size = str(w) + "x" + str(h)
    root.geometry(size)
    root.resizable(False, False)
    root.title("Password manager")

    root.configure(background=colors["bg"])
    root.iconbitmap(r"lock.ico")


    searchForPassword = Button(root, text="Search for a password", bg="#3b4252", fg="white", border=False, state=DISABLED,
                            activebackground="#434c5e", activeforeground=colors["fg"], font=("Roboto"), command=lambda: [searchforpassword(), root.attributes('-topmost', False)])

    newPassword = Button(root, text="Create a new password", bg="#3b4252", fg="white", border=False, state=DISABLED,
                        activebackground="#434c5e", activeforeground=colors["fg"], font=("Roboto"), command=lambda: [createnewPassword(), root.attributes('-topmost', False)])

    searchForPassword.place(width=int((w/2) - (w/100 * 2)),
                            height=h-(h/100 * 2), relx=0.01, rely=0.01)
    newPassword.place(width=int((w/2) - (w/100 * 2)), height=h -
                    (h/100 * 2), relx=0.51, rely=0.01)
    logIn(root, searchForPassword, newPassword)
    root.attributes('-topmost', True)
    root.bind('<Escape>', lambda x: root.destroy())
    root.update()

    root.mainloop()
               """)
    
    
os.system('pyinstaller -F --distpath . --name "PWDManager" --icon "lock.ico" "main.py"')
print("-------------------------------------")
os.remove('main.py')
os.remove("PWDManager.spec")
shutil.rmtree("./build")
os.remove("Installer.py")