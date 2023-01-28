import secrets
import string
from tkinter import * 
from tkinter.ttk import *
import pyperclip

#passwd calculation
def low():
    entry.delete(0, END)

    # Get length of passwd
    lenght = var_1.get()
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    
      # combination of numbers and symbol
    digit_symb = string.digits + string.punctuation
    
    password = ""
    #if selected low strenght
    if var.get() == 1:
        for i in range(0, lenght):
            password = password + secrets.choice(lower)
        return password
    
    # medium strenght
    elif var.get() == 0:
        for i in range(0,lenght):
            password = password + secrets.choice(upper)
        return password
    
    # strong strenght
    elif var.get() == 3:
        for i in range(0, lenght):
            password = password + secrets.choice(digit_symb)
        return password
    else:
        print("Please pick an option")
    
# passwd generator
def generate():
    password1 = low()
    entry.insert(10, password1)
    
#coppying passwd to clipboard
def copy_():
    random_passwd = entry.get()
    pyperclip.copy(random_passwd)
    

#GUI window

root = Tk()
var = IntVar()
var_1 = IntVar()

#Tittle
root.title("Passwd Generator")

#passwd gererated
random_passwd = Label(root, text="Lenght")
random_passwd.grid(row=0, column=1)

#label for passwd lenght
c_label = Label(root, text="Lenght")
c_label.grid(row=1)


#create Buttons that copy
#will copy the passwd to clipboard and Generate
#which will then generate the passwd
copy_btn = Button(root, text="Copy", command=copy_)
copy_btn.grid(row=0, column=2)

generate_btn = Button(root, text='Generate', command=generate)
generate_btn.grid(row=0, column=3)

#radio button for choosing the lenght of passwd
#Default strenght is Medium
radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=1, column=3, sticky="E")

#medium button
radio_med = Radiobutton(root, text="Medium", variable=var, value=0)
radio_med.grid(row=1, column=3, sticky="E")

#strong button

radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=4, sticky="E")
combo = Combobox(root, textvariable=var_1)

#combo Box for the lenght of usr passwd
combo["values"] = (8, 9, 10, 11, 12,
                    13, 14, 15, 16, 17,
                    18, 19, 20, 21, 22,
                    23, 24, 25, 26, 27,
                    28, 29, 30, 31, 32, "lenght")
combo.current(0)
combo.bind("<<ComboboxSelected>>")
combo.grid(column=1, row=1)

# Main loop
root.mainloop()