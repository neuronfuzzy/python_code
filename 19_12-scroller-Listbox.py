import tkinter

window = tkinter.Tk()
window.minsize(400, 500)
window.title('App Scroller Listbox')

label = tkinter.Label()
label.config(font=('Comic Sans MS', 14, 'bold'))

frame = tkinter.Frame(window)
scrollbar = tkinter.Scrollbar(frame, orient=tkinter.VERTICAL)
my_list = tkinter.Listbox(frame, height=5, selectmode=tkinter.MULTIPLE)
data = ['เทคโนโลยีเชิงวัตถุ', 'เทคโนโลยีพาณิชย์อิเล็กทรอนิกส์', 'ความปลอดภัยระบบสารสนเทศ', 'เทคโนโลยีเว็บเซอร์วิส', 'การจัดการโครงการเทคโนโลยีสารสนเทศ']


def list_selected(event):
    selected_list = my_list.curselection()
    result = [data[selected] for selected in selected_list]
    label['text'] = ', '.join(result)


scrollbar.config(command=my_list.yview)
my_list.bind("<<ListboxSelect>>", list_selected)
my_list.config(yscrollcommand=scrollbar.set, borderwidth=0)
for mac in data:
    my_list.insert(data.index(mac), mac)


scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
frame.pack()
my_list.pack()
label.pack()

window.mainloop()
