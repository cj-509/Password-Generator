import random
import string
import secrets
import pyperclip
from tkinter import *
from tkinter.ttk import *

# passwd calculation

def Low_strenght():
    entry.delete(0, END)
    
    # Get the lenght of the passwd from user
    lenght = var_1.get()
    lower = string.ascii_lowercase #lowercse letter a-z
    upper  = string.ascii_uppercase # uppercase letter A-Z
    letters = string.ascii_letters # concatanation between lower and Upper
    digits = string.digits
    symbol = string.punctuation
    password = ""
    
    # if the selected strenght is low
    if var.get() == 1:
        for i in range(0, lenght):
            password = password + secrets.choice(lower)
        return password
    
    # if the selected strenght is medium
    elif var.get() == 0:
        for i in range(0, lenght):
            password = password + secrets.choice(upper + lower)
        return password
    
    # if selected strenght is strong
    elif var.get() == 3:
        for i in range(0, lenght):
            password = password + secrets.choice(letters + digits + symbol)
        return password
    else:
        print("Please pick an option")
        

# to generate the passwd
def generate():
    password_1 = Low_strenght()
    entry.insert(10, password_1)


# copy function to cpy teh passwd

def copy1():
    random_passwrd = entry.get()
    pyperclip.copy(random_passwrd)
    

#GUI window
root = Tk()
var = IntVar()
var_1 = IntVar()


# Title
root.title("Random Password Generator")



#Showing the generated password onto the screen
random_password = Label(root, text="Password")
random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

# label for th lenght of the password
lenght_label = Label(root, text="Lenght")
lenght_label.grid(row=1)

#copy button to copy the password
copy_btn = Button(root, text="Copy", command=copy1)
copy_btn.grid(row=0, column=2)


#generate button to generate the password
generate_btn = Button(root, text="Generate", command=generate)
generate_btn.grid(row=0, column=3)


#option to picking the strenght of the password
rad_low = Radiobutton(root, text="Low", value=1, variable=var)
rad_low.grid(row=1, column=2, sticky="E")

#medium strenght button
rad_med = Radiobutton(root, text="Medium", value=0, variable=var) 
rad_med.grid(row=1, column=3, sticky="E")

#strong strenght
rad_strong = Radiobutton(root, text="Strong", value=3, variable=var)
rad_strong.grid(row=1, column=4, sticky="E")


combo = Combobox(root, textvariable=var_1)
# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 
                   15, 16,17, 18, 19, 20, 21,
                   22, 23, 24, 25,26, 27, 28, 
                   29, 30, 31, 32, 33, 34, 35)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)


root.mainloop()

