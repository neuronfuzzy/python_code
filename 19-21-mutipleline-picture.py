import tkinter as tk

root = tk.Tk()
text1 = tk.Text(root, height=30, width=40)
photo = tk.PhotoImage(file='./66.gif')
text1.insert(tk.END, '\n')
text1.image_create(tk.END, image=photo)

text1.pack(side=tk.LEFT)

text2 = tk.Text(root, height=30, width=60)
scroll = tk.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color',
                    foreground='#476042',
                    font=('Comic Sans MS', 12, 'bold'))
text2.tag_bind('follow',
               '<1>',
               lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
text2.insert(tk.END,'\najรติวัฒน์ ปารีศรี\n', 'big')
quote = """
Python: INFO212 Objected Oriented Technologies:
สอนโดย อ.รติวัฒน์ ปารีศรี
สาขา เทคโนโลีสารสนเทศ
คณะวิทยาศาสตร์และเทคโนโลยี
ม.ราชภัฏพิบูลสงคราม. ต.พลายชุมพล, อ.เมือง จ.พิษณุโลก--
เทอม1/68 น.ศ IT67/3.
"""
text2.insert(tk.END, quote, 'color')
text2.insert(tk.END, 'follow-up\n', 'follow')
text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

tk.mainloop()
