import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')
vi = tkinter.IntVar()
label = tkinter.Label()
label.config(text='พิซซ่า', font=('Arial', 40, 'bold'))
label.pack()

def update_label():
    if vi.get() == 1:
        label['text'] = 'พิซซ่า + เพิ่มชีส'
    else:
        label['text'] = 'พิซซ่า'

check = tkinter.Checkbutton(text='เพิ่มชีส', command=update_label, variable=vi)
check.pack()
window.mainloop()
