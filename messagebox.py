import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.minsize(400, 300)
window.title('Messagebox')

def show_handler():
    messagebox.showinfo(title='Greeting', message='Hello World!!!!')

show = tkinter.Button(text='Show', command=show_handler)
show.pack(expand=True)

window.mainloop()
