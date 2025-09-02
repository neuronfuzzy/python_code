import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')
window.config(padx=20, pady=20)
my_box = tkinter.Entry(width=30)

def add_handler():
    my_box.insert(tkinter.END, 'สวัสดี น.ศIT67-03!>> ')

def clear_handler():
    my_box.delete(0, tkinter.END)

add = tkinter.Button(text='Add', command=add_handler)
clear = tkinter.Button(text='Clear', command=clear_handler)
my_box.pack()
add.pack()
clear.pack()

window.mainloop()
