from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image


def choosefile():
    global filename
    Tk().withdraw()
    filename = askopenfilename()
    title2.config(text='Выбранный файл: '+ filename)


def convert():
    try:
        global filename
        image = Image.open(filename)
        filename = filename.replace(".jpg", "")
        filename = filename.replace(".png", "")
        filename = filename.replace(".bmp", "")
        filename = filename.replace(".gif", "")
        if vkladka.get() == 'png':
            image.save(filename + ".png")
        elif vkladka.get() == 'jpg':
            image.save(filename + ".jpg")
        elif vkladka.get() == 'bmp':
            image.save(filename + ".bmp")
        elif vkladka.get() == 'gif':
            image.save(filename + ".gif")
    except:
        mb.showerror(
            "Ошибка",
            "Выберите изображение и укажите формат")

root = Tk()
root.title('Конвертатор')
root.wm_attributes('-alpha', 1)
root.geometry('500x300')

title = Label(root, text="Выберите файл, который хотите конвертировать", )
title.pack()

btn = Button(root, text='Выбрать файл', command=choosefile)
btn.pack(pady=10)

title2 = Label(root, text='Выбранный файл:')
title2.pack(pady=10)

title3 = Label(root, text='Выберите формат')
title3.pack(pady=10)

vkladka = ttk.Combobox(root, values=['png', 'jpg', 'bmp', 'gif'])
vkladka.pack(pady=10)

btn2 = Button(root, text='Конвертировать', command=convert)
btn2.pack(pady=10)


root.mainloop()

