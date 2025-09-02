import tkinter

root = tkinter.Tk()
root.minsize(400, 300)
root.title('My App')

label_1 = tkinter.Label(master=root, text='First')
label_1.config(font=('Arial', 14, 'bold'), width=20)
label_2 = tkinter.Label(master=root, text='Second')
label_2.config(font=('Arial', 20, 'bold'), width=10)
label_3 = tkinter.Label(master=root, text='Third')
label_3.config(font=('Arial', 30, 'bold'), width=10)
label_4 = tkinter.Label(master=root, text='Forth')
label_4.config(font=('Arial', 25, 'italic'), width=20)

label_1.grid(column=0, row=0)
label_2.grid(column=1, row=1)
label_3.grid(column=2, row=2)
label_4.grid(column=3, row=3)

root.mainloop()
