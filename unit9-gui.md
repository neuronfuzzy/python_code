```python
import tkinter

root = tkinter.Tk()
root.minsize(400, 300)
root.title('My App รติวัฒน์')

label_1 = tkinter.Label(master=root, text='สาขา IT')
label_1.config(font=('Comic Sans MS', 14, 'bold'), width=20 ,foreground="blue")
label_2 = tkinter.Label(master=root, text='สาขา CS')
label_2.config(font=('Comic Sans MS', 20, 'bold'), width=10 , foreground="red")
label_3 = tkinter.Label(master=root, text='สาขา DS')
label_3.config(font=('Arial', 30, 'bold'), width=10 , foreground="cyan")
label_4 = tkinter.Label(master=root, text='สาขา คหกรรม')
label_4.config(font=('Arial', 25, 'italic'), width=20 , foreground="brown")

label_1.grid(column=0, row=0)
label_2.grid(column=1, row=1)
label_3.grid(column=2, row=2)
label_4.grid(column=3, row=3)

root.mainloop()
```
Diagram flow chart:

```mermaid
graph TD;
   A -->B
    A-->C;
    B-->D;
    C-->D;
```
อย่าลืมทำตามลำดับนะครับ! :star:
<img width="981" height="331" alt="Image" src="https://github.com/user-attachments/assets/0dd55feb-bf9f-4b2c-a875-782f63ebcfa5" />

[19_2-swap-button.py]
```python
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
```
output 19-2-v1

<img width="396" height="328" alt="Image" src="https://github.com/user-attachments/assets/04836b26-686b-40e6-8729-5ac0e4094a0c" />

output-19-2-v2

<img width="399" height="290" alt="Image" src="https://github.com/user-attachments/assets/54094979-593f-4a62-85ab-33525bd86936" />

[19_3-button_add.py](https://github.com/user-attachments/files/22078598/19_3-button_add.py)

```python
import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('App ajRatiwat ex19-3')
window.config(pady=50)

class Data:
    def __init__(self):
        self.counter = 0

    def increase(self):
        self.counter += 1

    def decrease(self):
        self.counter -= 1

data = Data()
my_text = tkinter.Label(text=data.counter, font=('Comic Sans MS', 80) , foreground = 'cyan')
my_text.pack(expand=True)
my_button1 = tkinter.Button()
my_button1.config(fg="green", text="เพิ่มข้อมูล")

my_button2 = tkinter.Button()
my_button2.config(fg="red", text="ลบข้อมูล")

def click_handler1():
    data.increase()
    my_text.config(text=data.counter)
def click_handler2():
    data.decrease()
    my_text.config(text=data.counter)
    
my_button1.config(command=click_handler1)
my_button1.pack(expand=True, pady=20)

my_button2.config(command=click_handler2)
my_button2.pack(expand=True, pady=20)

window.mainloop()


```

<img width="403" height="417" alt="Image" src="https://github.com/user-attachments/assets/3413dc22-0bdc-42cb-bff0-b550bb9a70ba" />

<img width="398" height="417" alt="Image" src="https://github.com/user-attachments/assets/5e1952fe-e7c0-4839-a033-491b435affa0" />

[19_4-defualt_textInput.py](https://github.com/user-attachments/files/22078597/19_4-defualt_textInput.py)


```python
import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App 19-4.py')
window.config(pady=30)

my_title = tkinter.Label()
my_title.config(font=('Helvetica', 30, 'bold'), fg='orange')
my_title.config(text='Default Text')
my_title.pack()
sv = tkinter.StringVar()
sv.set('')
my_box = tkinter.Entry()
my_box.config(width=20, textvariable=sv)
my_box.pack(expand=True)

def callback(*args):
    my_title['text'] = sv.get()

sv.trace_add('write', callback=callback)
window.mainloop()

```

<img width="402" height="328" alt="Image" src="https://github.com/user-attachments/assets/e5a09fb6-5614-4bff-90e9-e6d048372f14" />

[19_5-buttonAdd_textbox.py](https://github.com/user-attachments/files/22078603/19_5-buttonAdd_textbox.py)

```python
import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My ajRatiwat App19-5')
window.config(padx=20, pady=20)
my_box = tkinter.Entry(width=30)

def add_handler():
    my_box.insert(tkinter.END, 'สวัสดี น.ศIT67-03!>> ')

def clear_handler():
    my_box.delete(0, tkinter.END)

add = tkinter.Button(text='Add', command=add_handler)
clear = tkinter.Button(text='Clear', command=clear_handler)
my_box.pack()
add.pack()
clear.pack()

window.mainloop()

```

<img width="494" height="413" alt="Image" src="https://github.com/user-attachments/assets/8f216a68-134e-46b0-8234-f03d33e1aaee" />

[19_6-textbox-mutipleline.py](https://github.com/user-attachments/files/22078591/19_6-textbox-mutipleline.py)

```python
import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')

multiline_box = tkinter.Text(master=window)
multiline_box.config(width=30, height=5)
multiline_box.focus()
multiline_box.insert(tkinter.END, 'อ.รติวัฒน์ บรรทัดที่ 1.')
multiline_box.insert(tkinter.INSERT, '\nผศ.ดร.ธงรบ บรรทัดที่ 2.')
multiline_box.insert(tkinter.INSERT, '\nผศ.ไพทูรย์ บรรทัดที่ 3.')
# multiline_box.tag_add('second', '4.0', '4.9')
#multiline_box.tag_config('second', background='blue', foreground='white')
multiline_box.tag_add('third', '3.0', '3.9')
multiline_box.tag_config('third', background='#000FFF', foreground='white')
multiline_box.pack(expand=True)

window.mainloop()


```

<img width="496" height="414" alt="Image" src="https://github.com/user-attachments/assets/9f6a5df5-8f3b-4a21-9b0d-2c3b9bd11b0a" />

[19_8-spinbox.py](https://github.com/user-attachments/files/22078592/19_8-spinbox.py)
```python

import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('App SprinBox by ajRatiwat')

vi = tkinter.StringVar()
vi.set('9')
label = tkinter.Label(text=vi.get())
label.config(font=('Cosmic', 30, 'bold'))
label.pack()

def update_label():
    label['text'] = vi.get()  

spin = tkinter.Spinbox(from_=1, to=10, command=update_label, textvariable=vi)
spin.pack()

window.mainloop()
```

<img width="398" height="329" alt="Image" src="https://github.com/user-attachments/assets/378f5426-0282-4bdc-9327-4a2e553fe2ba" />

[19-9]
```python
import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My Scale-number')
vi = tkinter.IntVar()
vi.set(100)
label = tkinter.Label(text=vi.get())
label.config(font=('Arial', 40, 'bold'))
label.pack()

def update_label(value):
    label['text'] = value

spin = tkinter.Scale(from_=1, to=200, command=update_label, variable=vi)
spin.pack()

window.mainloop()
```
output 19-9

<img width="395" height="331" alt="Image" src="https://github.com/user-attachments/assets/6d9d0dba-f8da-4fe7-9268-8d75a493c0e1" />

[19_11-listbox.py](https://github.com/user-attachments/files/22078599/19_11-listbox.py)
```python
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

```

<img width="397" height="323" alt="Image" src="https://github.com/user-attachments/assets/b4fd5925-5fb3-42ff-be5b-22cb748a3613" />

[19_12-scroller-Listbox.py](https://github.com/user-attachments/files/22078595/19_12-scroller-Listbox.py)
```python

```
[19_13-messagebox.py](https://github.com/user-attachments/files/22078584/19_13-messagebox.py)
```python

```
[19_10-radiobutton.py](https://github.com/user-attachments/files/22078585/19_10-radiobutton.py)
```python

```
[19_7-checkbutton.py](https://github.com/user-attachments/files/22078593/19_7-checkbutton.py)
```python
import tkinter

window = tkinter.Tk()
window.minsize(400, 300)
window.title('My App')
vi = tkinter.IntVar()
label = tkinter.Label()
label.config(text='พิซซ่า', font=('Arial', 40, 'bold'))
label.pack()

def update_label():
    if vi.get() == 1:
        label['text'] = 'พิซซ่า + เพิ่มชีส'
    else:
        label['text'] = 'พิซซ่า'

check = tkinter.Checkbutton(text='เพิ่มชีส', command=update_label, variable=vi)
check.pack()
window.mainloop()
```

<img width="395" height="328" alt="Image" src="https://github.com/user-attachments/assets/9e6a01d1-fb22-42ac-998b-60ff3e84ecb6" />

[19_9-scale-number1-100.py](https://github.com/user-attachments/files/22078602/19_9-scale-number1-100.py)
```python

```