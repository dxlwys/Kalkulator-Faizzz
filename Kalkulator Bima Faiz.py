from tkinter import *
from functools import partial

def bersih_all():
    layar.delete(0, len(layar.get()))
    layar.insert(0, 0)

def bersih():
    layar.delete(len(layar.get())-1)
    if layar.get() == '':
        layar.insert(0, 0)

def angka(value):
    if layar.get() == '0' or layar.get() == "Invalid":
        layar.delete(0, len(layar.get()))
    layar.insert(len(layar.get()), value)

def place_operator(value):
    if layar.get()[-1] in operators:
        layar.delete(len(layar.get())-1)
    if layar.get() == 'Invalid':
        layar.delete(0, len(layar.get()))
        layar.insert(len(layar.get()), 0)
    layar.insert(len(layar.get()), value)

def layar_answer():
    exp = layar.get()
    try:
        value = eval(exp)
    except:
        value = 'Invalid'
    layar.delete(0 , len(layar.get()))
    layar.insert(0, value)

kalkulator = Tk()
kalkulator.title('Kalkulator Faizzz')
kalkulator.resizable(False, False)
kalkulator.config(bg='Black')

numbers = '789456123'
operators = '/*-+'

layar = Entry(kalkulator, width=16, font=('Helvetica', 26, 'bold'), bg='black', fg='white', bd=0, justify=RIGHT)
layar.grid(row=0, column=0, columnspan=4)
layar.insert(0, 0)

btn_ac = Button(kalkulator, text='CLEAR', width=16, font=('helvetica', 20), bg='#A5A5A5', activebackground='white',
fg='#000000', bd=0, relief=FLAT, command=bersih_all)
btn_ac.grid(row=1, column=0, padx=1, pady=1, columnspan=3)

btn_bersih = Button(kalkulator, text='←', width=5, font=('helvetica', 20), bg='#343434', activebackground='white',
fg='#F9F9F9', bd=0, relief=FLAT, command=bersih)
btn_bersih.grid(row=5, column=2, padx=1, pady=1)

btn_equal = Button(kalkulator, text='= ', width=5 , font=('helvetica', 20), bg='#FF9F0A', activebackground='white',
fg='#F9F9F9', bd=0, relief=FLAT, command=layar_answer,)
btn_equal.grid(row=5, column=3, padx=1, pady=1)

for i in range(9):
    btn = Button(kalkulator, text=numbers[i], width=5, font=('helvetica', 20), bg='#343434', fg='white', bd=0, relief=FLAT,
    command=partial(angka, numbers[i]))
    btn.grid(row=i//3+2, column=i%3, padx=1, pady=1)

for i in range(4):
    btn = Button(kalkulator, text=operators[i], width=5, font=('helvetica', 20), bg='#FF9F0A', activebackground='white', fg='#F9F9F9', bd=0, relief=FLAT,
    command=partial(place_operator, operators[i]))
    btn.grid(row=i+1, column=3, padx=1, pady=1)

btn_dot = Button(kalkulator, text='.', width=5, font=('helvetica', 20), bg='#343434', activebackground='white',
fg='white', bd=0, relief=FLAT, command=partial(angka, '.'))
btn_dot.grid(row=5, column=0, padx=1, pady=1)

btn_zero = Button(kalkulator, text='0', width=5, font=('helvetica', 20), bg='#343434', activebackground='white',
fg='white', bd=0, relief=FLAT, command=partial(angka, 0))
btn_zero.grid(row=5, column=1, padx=1, pady=1)
    
kalkulator.mainloop()