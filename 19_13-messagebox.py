import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.minsize(400, 300)
window.title('Messagebox')

def delete(data):
    if data == True:
        print('Confirm delete')
    else:
        print('Cancel delete')

def confirm_delete_handler():
    answer = messagebox.askokcancel(
        title='Delete',
        message='Confirm Delete',
        icon=messagebox.ERROR
    )
    delete(answer)

show = tkinter.Button(text='Delete', command=confirm_delete_handler)
show.pack(expand=True)

window.mainloop()
