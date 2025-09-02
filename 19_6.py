import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')

multiline_box = tkinter.Text(master=window)
multiline_box.config(width=30, height=5)
multiline_box.focus()
multiline_box.insert(tkinter.END, 'The first line text.')
multiline_box.insert(tkinter.INSERT, '\nThe second line text.')
multiline_box.insert(tkinter.INSERT, '\nThe third line text.')
multiline_box.tag_add('third', '3.0', '3.9')
multiline_box.tag_config('third', background='red', foreground='white')
multiline_box.pack(expand=True)

window.mainloop()
