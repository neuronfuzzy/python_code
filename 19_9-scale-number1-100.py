import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')
vi = tkinter.IntVar()
vi.set(50)
label = tkinter.Label(text=vi.get())
label.config(font=('Arial', 40, 'bold'))
label.pack()

def update_label(value):
    label['text'] = value

spin = tkinter.Scale(from_=1, to=100, command=update_label, variable=vi)
spin.pack()

window.mainloop()
