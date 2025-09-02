import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')
window.config(pady=50)

class Data:
    def __init__(self):
        self.counter = 0

    def increase(self):
        self.counter += 1

data = Data()
my_text = tkinter.Label(text=data.counter, font=('AngsanaUPC', 80))
my_text.pack(expand=True)
my_button = tkinter.Button()
my_button.config(fg="green", text="Click")

def click_handler():
    data.increase()
    my_text.config(text=data.counter)

my_button.config(command=click_handler)
my_button.pack(expand=True, pady=20)

window.mainloop()
