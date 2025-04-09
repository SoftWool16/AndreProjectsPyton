from tkinter import *
from tkinter import ttk
window = Tk()
window.title("калькулятор")
window.geometry("1000x750")




ttk.Button(window, text="1", command=None).grid(column=0, row=0)
ttk.Button(window, text="2", command=None).grid(column=1, row=0)            
ttk.Button(window, text="3", command=None).grid(column=2, row=0)            
ttk.Button(window, text="4", command=None).grid(column=0, row=1)
ttk.Button(window, text="5", command=None).grid(column=1, row=1)
ttk.Button(window, text="6", command=None).grid(column=2, row=1)
ttk.Button(window, text="7", command=None).grid(column=0, row=2)
ttk.Button(window, text="8", command=None).grid(column=1, row=2)
ttk.Button(window, text="9", command=None).grid(column=2, row=2)
ttk.Button(window, text="+", command=None).grid(column=0, row=3)
ttk.Button(window, text="-", command=None).grid(column=1, row=3)
ttk.Button(window, text="*", command=None).grid(column=3, row=0)
ttk.Button(window, text="/", command=None).grid(column=3, row=1)
ttk.Button(window, text="%", command=None).grid(column=2, row=3)
ttk.Button(window, text="=", command=None).grid(column=3, row=2, rowspan=2)







window.mainloop()