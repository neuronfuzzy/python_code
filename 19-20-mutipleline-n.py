import tkinter as tk

root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=4, width=50)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """Python: INFO212 Objected Oriented Technologies:
สอนโดย อ.รติวัฒน์ ปารีศรี
สาขา เทคโนโลีสารสนเทศ
คณะวิทยาศาสตร์และเทคโนโลยี
ม.ราชภัฏพิบูลสงคราม. ต.พลายชุมพล, อ.เมือง จ.พิษณุโลก--
เทอม1/68 น.ศ IT67/3."""
T.insert(tk.END, quote)
tk.mainloop()