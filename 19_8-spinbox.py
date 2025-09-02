#spinner
import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')

vi = tkinter.StringVar()
vi.set('9')
label = tkinter.Label(text=vi.get())
label.config(font=('Arial', 40, 'bold'))
label.pack()

def update_label():
    label['text'] = vi.get()  

spin = tkinter.Spinbox(from_=1, to=10, command=update_label, textvariable=vi)
spin.pack()

window.mainloop()
