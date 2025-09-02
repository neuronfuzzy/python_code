import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')
window.config(pady=30)

my_title = tkinter.Label()
my_title.config(font=('Helvetica', 30, 'bold'), fg='orange')
my_title.config(text='Default Text')
my_title.pack()
sv = tkinter.StringVar()
sv.set('')
my_box = tkinter.Entry()
my_box.config(width=20, textvariable=sv)
my_box.pack(expand=True)

def callback(*args):
    my_title['text'] = sv.get()

sv.trace_add('write', callback=callback)
window.mainloop()
