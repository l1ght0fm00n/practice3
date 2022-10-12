def choosefile_test():
    global filename
    Tk().withdraw()
    filename = askopenfilename()
    title2.config(text='Выбранный файл: '+ filename)




