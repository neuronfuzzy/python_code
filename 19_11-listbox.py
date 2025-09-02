import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')

label = tkinter.Label()
label.config(font=('Arial', 14, 'bold'))
data = ['INFO212', 'INFO363', 'INFO262', 'INFO354']
computer_list = tkinter.Listbox(
    height=len(data),
    selectmode=tkinter.MULTIPLE
)

def list_selected(event):
    selected_list = computer_list.curselection()
    result = [data[selected] for selected in selected_list]
    label['text'] = ', '.join(result)

computer_list.bind("<<ListboxSelect>>", list_selected)

for mac in data:
    computer_list.insert(data.index(mac), mac)

computer_list.pack()
label.pack()

window.mainloop()
