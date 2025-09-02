import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')
vi = tkinter.StringVar()
vi.set('กรุณาเลือกเพศ')
label = tkinter.Label(text=vi.get())
label.config(font=('Arial', 40, 'bold'))
label.pack()

def change_radio():
    label['text'] = f'เพศ {vi.get()}'

radio_1 = tkinter.Radiobutton(
    text='ชาย',
    value='ชาย',
    command=change_radio,
    variable=vi
)
radio_2 = tkinter.Radiobutton(
    text='หญิง',
    value='หญิง',
    command=change_radio,
    variable=vi
)
radio_3 = tkinter.Radiobutton(
    text='ไม่ระบุ',
    value='ไม่ระบุ',
    command=change_radio, variable=vi
)

radio_1.pack()
radio_2.pack()
radio_3.pack()
window.mainloop()
