import tkinter as tk
from tkinter import messagebox as mb

def add_lbl_1():
    convertor = sh_poryadok()
    label = tk.Label(win, text=convertor)
    label.pack()
def sh_poryadok():
    alph = 'абвгдеёжзийклмнопрстуфхццшщъыьэюя ,:;?!.()'
    row = txt.get()
    row.lower()
    res = ''
    if row:
        for s in row:
            for i in range(len(alph)):
                if s == alph[i]:
                    res += str(i + 1) + ' '
    else:
        mb.showerror("Ошибка",
                     "Должен быть введен текст")
    return res
def add_lbl_2():
    convertor = sh_cesar()
    label = tk.Label(win, text=convertor)
    label.pack()
def sh_cesar():
    alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ,:;?!.()абвгдеёжзийклмнопрстуфхццшщъыьэюя'
    row = txt.get()
    res = ''
    if row:
        for s in row:
            for i in range(len(alph)):
                if (s == alph[i]) and (i != 72) and (i != 73) and (i != 74):
                    res += alph[i + 3]
                elif (s == alph[i]) and (i == 72):
                    res += 'a'
                elif (s == alph[i]) and (i == 73):
                    res += 'б'
                elif (s == alph[i]) and (i == 74):
                    res += 'в'
    else:
        mb.showerror("Ошибка",
                     "Должен быть введен текст")
    return res
def add_lbl_3():
    convertor = sh_atbash()
    label = tk.Label(win, text=convertor)
    label.pack()
def sh_atbash():
    alph = 'абвгдеёжзийклмнопрстуфхццшщъыьэюя'
    row = txt.get()
    res = ''
    if row:
        for s in row:
            for i in range(len(alph)):
                if s == alph[i]:
                    res += alph[len(alph) - i - 1]
    else:
        mb.showerror("Ошибка",
                     "Должен быть введен текст")
    return res

#window settings
win = tk.Tk()
win.title('Шифратор сообщений')
win.geometry("500x600")
win.config(bg='#a2d2ff')
photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)
win.resizable(False, False)

tittle1 = tk.Label(win, text='Введите шифруемое сообщение',
                   bg='#a2d2ff',
                   font=('Arial', 16, 'bold'))
tittle1.pack()

txt = tk.Entry(win)
txt.pack()

tittle1 = tk.Label(win, text='Выберите метод', bg='#a2d2ff',font=('Arial', 16, 'bold'))
tittle1.pack()

#button settings
numbers = tk.Button(win, padx= 50, pady=20, text='Порядковый', command=add_lbl_1,
                    activebackground='#FFAFCC', bg='#FFC8DD')
cesar = tk.Button(win, padx= 50, pady=20, text='Цезаря', command=add_lbl_2,
                  activebackground='#FFAFCC', bg='#FFC8DD')
atbsh = tk.Button(win, padx= 50, pady=20, text='Атбаш', command=add_lbl_3,
                  activebackground='#FFAFCC', bg='#FFC8DD')
numbers.pack()
cesar.pack()
atbsh.pack()

win.mainloop()

