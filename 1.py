from tkinter import * 
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import ttk
import pygame



def clicked():
    ch = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = txt.get()
    ans = res + '-'
    for x in res:
        ans += ch[(ch.index(x) + 3) % len(ch)]
    ans += '-'
    for x in res:
        ans += ch[(ch.index(x) - 5) % len(ch)]
    lbl = Label(tab1, text=f'Ваш ключ: {ans}', font=('Arial Bold', 30), relief="groove")
    lbl.grid(row=4)
    lbl.place(anchor=CENTER, relx=0.5, rely=0.5)


def play():
    pygame.mixer.music.load("itmo_study/laba4/Glass.aiff")
    pygame.mixer.music.play()


window = Tk()
window.title('Key generator for minecraft :)')
window.maxsize(1000, 500)
w = 1600
h = 1100
window.geometry(f"{w}x{h}")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Основное')  
tab_control.add(tab2, text='Доп')  
tab_control.pack(expand=1, fill='both') 

filename = PhotoImage(file="itmo_study/laba4/imgpreview.png")
background_label = Label(tab1, image=filename)  
background_label.place(x=0, y=0, relwidth=1, relheight=1)

filename1 = PhotoImage(file="itmo_study/laba4/2731746.jpg.png")
background_label1 = Label(tab2, image=filename1, border=50)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)

lbl_hi = Label(tab1, text='Введите первую часть вашего ключа!', font=('Arial Bold', 40), relief="groove")
lbl_hi.grid(column=0, row=0)
lbl_hi.place(anchor=CENTER, relx=0.5, rely=0.1)

txt = Entry(tab1, width=10, borderwidth=0)
txt.grid(column=0, row=0)
txt.place(anchor=CENTER, relx=0.5, rely=0.25)
txt.focus()

btn = Button(tab1, text='do this', bg='red', fg='black', command=clicked, border=0)
btn.grid(column=0)
btn.place(anchor=CENTER, relx=0.5, rely=0.35)

pygame.mixer.init()

my_button = Button(tab2, text="Play Song", font=("Helvetica", 32), command=play)
my_button.pack(pady=10)

window.mainloop()