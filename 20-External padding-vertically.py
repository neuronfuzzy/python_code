import tkinter as tk

root = tk.Tk()
w = tk.Label(root, text="พระอาทิตย์ สีแดง", bg="red", fg="white")
w.pack(fill=tk.X, pady=10)
w = tk.Label(root, text="ต้นหญ้า สีเขียว", bg="green", fg="black")
w.pack(fill= tk.X, pady=10)
w = tk.Label(root, text="ท้องฟ้า สีน้ำเงิน", bg="blue", fg="white")
w.pack(fill=tk.X, pady=10)
tk.mainloop()