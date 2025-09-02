import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App ajรติวัฒน์')

my_text = tkinter.Label(text="ajรติวัฒน์", font=('Comic Sans MS', 20))
my_text.pack()
my_button = tkinter.Button()
my_button.config(fg="red", text="Swap")

def click_handler():
    text = my_text['text']
    updated_text = 'สาขา IT' if text == 'ajรติวัฒน์' else 'ajรติวัฒน์'
    my_text.config(text=updated_text)

my_button.config(command=click_handler)
my_button.pack()

window.mainloop()
