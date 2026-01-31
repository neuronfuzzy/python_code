# รับค่าจำนวนรอบจากผู้ใช้
L = int(input("กรุณาใส่จำนวนรอบ: "))

# กำหนดค่าเริ่มต้น n = L
n = L

# ใช้ while loop ตามจำนวนรอบ L
round_count = 1
while round_count <= L:
    pounds = n - (round_count - 1)
    print("#" * pounds)
    round_count += 1
