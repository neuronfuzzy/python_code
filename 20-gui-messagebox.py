import tkinter as tk
from tkinter import messagebox as mb

def answer():
    mb.showerror("ตอบคำถาม", "เสียใจด้วย, ไม่มีคำตอบ ที่เป็นไปได้!")

def callback():
    if mb.askyesno('ตรวจสอบ', 'คุณมั่นใจนะ ว่าจะออก?'):
        mb.showwarning('ใช่', 'ยังไม่ถูก นำไปใช้งาน')
    else:
        mb.showinfo('ไม่', 'ยกเลิก การออกจากระบบ')

tk.Button(text='ออกจากระบบ', command=callback).pack(fill=tk.X)
tk.Button(text='คำตอบ', command=answer).pack(fill=tk.X)
tk.mainloop()