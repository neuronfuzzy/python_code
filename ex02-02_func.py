import numpy as np
# โปรแกรมนี้ เขียนโดย aj@Ratiwat
pi = 3.1416

print("Hi Python")
name = input("Enter your name >>> ")
id_std = input("ใส่รหัส น.ศ : >>")
print("Hi! " + name)
print("รหัส น.ศ" , id_std)

N = np.log2(1024)
print("ค่า N =" , N)
x = 3*np.sin(np.pi/2)

print("ค่า x =" , x)

y = np.sqrt(64)
print ("ค่าของ y" , y)
# ตัวแปร pi = 3.1416 หรือ 22/7
# ตัวแปร r = รัศมี
# ตัวแปร area1 = พื้นที่วงกลม pi*r^2  
r = int(input("ใส่ค่ารัศมี : "))
print("ค่ารัศมี ",r)
area1 = pi*(np.exp(r))
print("พื้นที่สามเหลี่ยมเท่ากับ >> " , area1)