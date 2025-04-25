from tkinter import *
from tkinter import ttk
from tkinter import font
window = Tk()
window.title("калькулятор")

e1 = ttk.Entry(window)

string = ''

def command_1():
    global string
    string += "1"
    command_equals()

def command_2():
    global string
    string += "2"
    command_equals()

def command_3():
    global string
    string += "3"
    command_equals()

def command_multiplication():
    global string
    string += "*"
    command_equals()

def command_4():
    global string
    string += "4"
    command_equals()

def command_5():
    global string
    string += "5"
    command_equals()

def command_6():
    global string
    string += "6"
    command_equals()

def command_division():
    global string
    string += "/"
    command_equals()

def command_7():
    global string
    string += "7"
    command_equals()

def command_8():
    global string
    string += "8"
    command_equals()

def command_9():
    global string
    string += "9"
    command_equals()

def command_eq():
    global string
    string += "."
    command_equals()


    command_equals()
def command_plus():
    global string
    string += "+"
    command_equals()
def command_minus():
    global string
    string += "-"
    command_equals()
def command_percent():
    global string
    string += "%"
def command_zero():
    global string
    string += "0"
    command_equals()

def command_l():
    global string
    string += "("
    command_equals()

def command_r():
    global string
    string += ")"
    command_equals()

    
def command_del():
    global string
    string = ''
    command_equals()


def command_equals():
    global string
    print(string)
    print(eval(string))


    custom_font = font.Font(family="Algerian", size=20)
    ttk.Label(window, text=eval(string),
           foreground="black", font=custom_font).grid(ipady=5, column=2, row=0, ipadx=4)
    
    ttk.Label(window, text=(string + "="),
           foreground="black",font=custom_font).grid(ipady=5, column=0, row=0, ipadx=4, columnspan=2)




ttk.Button(window, text="DelAll", command=command_del).grid(ipady=10, column=3, row=0, ipadx=4)
ttk.Button(window, text="(", command=command_l).grid(ipady=10, column=4, row=0)
ttk.Button(window, text=")", command=command_r).grid(ipady=9, column=4, row=1)

           
buttons = [
ttk.Button(window, text="1", command=command_1),
ttk.Button(window, text="2", command=command_2),
ttk.Button(window, text="3", command=command_3),
ttk.Button(window, text="*", command=command_multiplication),

ttk.Button(window, text="4", command=command_4),
ttk.Button(window, text="5", command=command_5),
ttk.Button(window, text="6", command=command_6),
ttk.Button(window, text="/", command=command_division),

ttk.Button(window, text="7", command=command_7),
ttk.Button(window, text="8", command=command_8),
ttk.Button(window, text="9", command=command_9),
ttk.Button(window, text=".", command=command_eq),

ttk.Button(window, text="+", command=command_plus),
ttk.Button(window, text="-", command=command_minus),
ttk.Button(window, text="%", command=command_percent),
ttk.Button(window, text="0", command=command_zero)]


for i in range(0, 4):
    for j in range(0, 4):
        buttons[i*4+j].grid(column=j, row=i+1, ipadx=3, ipady=8)
        


window.mainloop()