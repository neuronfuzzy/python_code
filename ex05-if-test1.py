# กำหนดจำนวนรอบเริ่มต้น
a = int(input("ป้อนจำนวนรอบ (1-10): "))
b = 1    # 
sig = "*"
# ใช้ if ซ้อนกัน 5 รอบ
if a >= 1:
    print(sig)
    if a >= 2:
        print(sig*(b+1))
        if a >= 3:
            print(sig*(b+2))
            if a >= 4:
                print(sig*(b+3))
                if a >= 5:
                    print(sig*(b+4))
                    if a >= 6:
                        print(sig*(b+5))
                        if a >= 7:
                            print(sig*(b+6))
                            if a >= 8:
                                print(sig*(b+7))
                                if a >= 9:
                                    print(sig*(b+8))
                                    if a >= 10:
                                        print(sig*(b+9))