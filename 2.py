from tkinter import *
from tkinter.ttk import *


window = Tk()
Progress_Bar = Progressbar(window, orient=HORIZONTAL, length=250, mode='determinate')


def Slide():
    import time
    Progress_Bar['value'] = 20
    window.update_idletasks()
    
    time.sleep(0.6)
    Progress_Bar['value'] = 50
    window.update_idletasks()

    time.sleep(0.6)
    Progress_Bar['value'] = 80
    window.update_idletasks() 

    time.sleep(0.6)
    Progress_Bar['value'] = 100

Progress_Bar.pack()
Button(window, text='Run', command=Slide).pack(pady=10)
mainloop()