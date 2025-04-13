from tkinter import *
from tkinter import ttk
window = Tk()
window.title("калькулятор")
#window.geometry("327x225")

e1 = ttk.Entry(window)


string = ''

def command_1():
    global string
    string += "1"
def command_2():
    global string
    string += "2"
def command_3():
    global string
    string += "3"
def command_multiplication():
    global string
    string += "*"

def command_4():
    global string
    string += "4"
def command_5():
    global string
    string += "5"
def command_6():
    global string
    string += "6"
def command_division():
    global string
    string += "/"

def command_7():
    global string
    string += "7"
def command_8():
    global string
    string += "8"
def command_9():
    global string
    string += "9"
def command_equals():
    global string
    #string += "="
    print(string)
    print(eval(string))

    ttk.Label(window, text=eval(string),
           foreground="red").grid(ipady=5, column=1, row=0, ipadx=4, columnspan=2)
    
    ttk.Label(window, text=(string + "="),
           foreground="red").grid(ipady=5, column=0, row=0, ipadx=4)

def command_plus():
    global string
    string += "+"
def command_minus():
    global string
    string += "-"
def command_percent():
    global string
    string += "%"
def command_zero():
    global string
    string += "0"


ttk.Label(window, text="калькулятор\nдля\nмужиков", background="black",
           foreground="red").grid(ipady=5, column=3, row=0, ipadx=4)
           
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
ttk.Button(window, text="=", command=command_equals),

ttk.Button(window, text="+", command=command_plus),
ttk.Button(window, text="-", command=command_minus),
ttk.Button(window, text="%", command=command_percent),
ttk.Button(window, text="0", command=command_zero)]

for i in range(0, 4):
    for j in range(0, 4):
        buttons[i*4+j].grid(column=j, row=i+1, ipadx=3, ipady=8)


window.mainloop()