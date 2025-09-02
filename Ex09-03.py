#windows GUI tkinter background cyan + button
from tkinter import *

root = Tk()
root.title("GUI Example")
root.geometry("300x250")
root.option_add('*font', 'tahoma 10 bold')
frame = Frame(root)
frame.config(background="cyan")
frame.place(width=300, height=250, x=0, y=0)

button1 = Button(frame, text="Swap", width=12, height=2,foreground = "red")
button1.pack(padx=30, pady=30)
image1 = PhotoImage(file="./book.gif")
button2 = Button(frame, image=image1, text="button2", width="100", height=30, compound="left", bg="white", foreground="blue")
button2.pack(padx=30, pady=30)
root.mainloop()
