from tkinter import * 
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import ttk
import pygame


def clicked():
    characters = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    input_text = text_enter.get()
    key = input_text + '-'
    for ch in input_text:
        key += characters[(characters.index(ch) + 3) % len(characters)]
    key += '-'
    for ch in input_text:
        key += characters[(characters.index(ch) - 5) % len(characters)]
    lbl = Label(tab1, text=f'Ваш ключ: {key}', font=('Arial Bold', 30), relief="groove")
    lbl.grid(row=4)
    lbl.place(anchor=CENTER, relx=0.5, rely=0.5)


def play():
    pygame.mixer.music.load("itmo_study/laba4/Glass.aiff")
    pygame.mixer.music.play()


window = Tk()
window.title('Key generator for minecraft :)')
window.maxsize(1600, 1000)
width = 1000
hight = 500
window.geometry(f"{width}x{hight}")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Основное')  
tab_control.add(tab2, text='Доп')  
tab_control.pack(expand=1, fill='both') 

image_game = PhotoImage(file="itmo_study/laba4/imgpreview.png")
background_label = Label(tab1, image=image_game)  
background_label.place(x=0, y=0, relwidth=1, relheight=1)

image_bg = PhotoImage(file="itmo_study/laba4/2731746.jpg.png")
background_label1 = Label(tab2, image=image_bg, border=50)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)

lbl_hi = Label(tab1, text='Введите первую часть вашего ключа!', font=('Arial Bold', 40), relief="groove")
lbl_hi.grid(column=0, row=0)
lbl_hi.place(anchor=CENTER, relx=0.5, rely=0.1)

text_enter = Entry(tab1, width=10, borderwidth=0)
text_enter.grid(column=0, row=0)
text_enter.place(anchor=CENTER, relx=0.5, rely=0.25)
text_enter.focus()

btn = Button(tab1, text='generate', bg='red', fg='black', command=clicked, border=0)
btn.grid(column=0)
btn.place(anchor=CENTER, relx=0.5, rely=0.35)

pygame.mixer.init()

my_button = Button(tab2, text="Play Song", font=("Helvetica", 32), command=play)
my_button.pack(pady=10)

window.mainloop()