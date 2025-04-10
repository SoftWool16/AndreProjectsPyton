from tkinter import *
from tkinter import ttk
window = Tk()
window.title("калькулятор")
window.geometry("327x225")

e1 = ttk.Entry(window)

def sd():
    num1 = float(btn1.get())
    num2 = float(btn2.get())
    result = num1 + num2
    ttk.Label(window, text=result,
                background="#FF8C00", foreground="#FFFFFF").place(relx=0, height=59, width=245)
        

ttk.Label(window, text="калькулятор\nдля\nмужиков", background="black",
           foreground="red").grid(ipady=5, column=3, row=0, ipadx=4)
btn1 = ttk.Button(window, text="1", command=sd()).grid(column=0, row=1, ipadx=3, ipady=8)
btn2 = ttk.Button(window, text="2", command=sd()).grid(column=1, row=1, ipadx=3, ipady=8)            
ttk.Button(window, text="3", command=None).grid(column=2, row=1, ipadx=3, ipady=8)            
ttk.Button(window, text="4", command=None).grid(column=0, row=2, ipadx=3, ipady=8)
ttk.Button(window, text="5", command=None).grid(column=1, row=2, ipadx=3, ipady=8)
ttk.Button(window, text="6", command=None).grid(column=2, row=2, ipadx=3, ipady=8)
ttk.Button(window, text="7", command=None).grid(column=0, row=3, ipadx=3, ipady=8)
ttk.Button(window, text="8", command=None).grid(column=1, row=3, ipadx=3, ipady=8)
ttk.Button(window, text="9", command=None).grid(column=2, row=3, ipadx=3, ipady=8)
ttk.Button(window, text="+", command=None).grid(column=0, row=4, ipadx=3, ipady=9)
ttk.Button(window, text="-", command=None).grid(column=1, row=4, ipadx=3, ipady=9)
ttk.Button(window, text="*", command=None).grid(column=3, row=1, ipadx=3, ipady=8)
ttk.Button(window, text="/", command=None).grid(column=3, row=2, ipadx=3, ipady=8)
ttk.Button(window, text="%", command=None).grid(column=2, row=4, ipadx=3, ipady=9)
ttk.Button(window, text="=", command=None).grid(column=3, row=3, rowspan=2, ipady=30, ipadx=3)










window.mainloop()