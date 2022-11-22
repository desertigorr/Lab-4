from tkinter import *


def start():
    generate_key(str(entry.get()))


def generate_key(input):
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWZYX0123456789'
    key = ''

    block = input.upper()

    flag = True

    if len(block) != 5:
        flag = False
    else:
        for i in block:
            if i not in symbols:
                flag = False
    if flag:
        key += f'{block}-'

    for symbol in block:
        key += f'{symbols[((symbols.find(symbol)+3)%36)]}'
    key += '-'
    for symbol in block:
        key += f'{symbols[((symbols.find(symbol)-5)%36)]}'

    if flag:
        label2['text'] = key
    else:
        label2['text'] = 'Try again...'


def close():
    window.destroy()



window = Tk()
window.title("Keygen for Mirror's Edge: Catalyst v.0.2.4")
window.geometry('750x442')

bg = PhotoImage(file="art.png")
label1 = Label(window, image = bg)
label1.place(x = 0, y = 0)

label2 = Label(window, text = "Input first 5 letters, then click 'Generate key'")
label2.pack(pady = 10)

entry = Entry(window)
entry.pack(pady=30)

button1 = Button(window,text="Generate key", command=start)
button1.pack(pady=0)


label2 = Label(window, text = "XXXXX-XXXXX-XXXXX")
label2.pack(pady = 50)


window.mainloop()
