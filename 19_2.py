import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')

my_text = tkinter.Label(text="Original", font=('AngsanaUPC', 20))
my_text.pack()
my_button = tkinter.Button()
my_button.config(fg="green", text="Swap")

def click_handler():
    text = my_text['text']
    updated_text = 'New Text' if text == 'Original' else 'Original'
    my_text.config(text=updated_text)

my_button.config(command=click_handler)
my_button.pack()

window.mainloop()
