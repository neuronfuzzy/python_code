import tkinter as tk

root = tk.Tk()

w = tk.Label(root, text="แดง", bg="red", fg="white")
w.pack(padx=5, pady=10, side=tk.LEFT)
w = tk.Label(root, text="เขียว", bg="green", fg="black")
w.pack(padx=5, pady=20, side=tk.LEFT)
w = tk.Label(root, text="น้ำเงิน", bg="blue", fg="white")
w.pack(padx=5, pady=20, side=tk.LEFT)
tk.mainloop()