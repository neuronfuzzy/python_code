# กำหนดจำนวนรอบเริ่มต้น
d = int(input("ป้อนจำนวนรอบ (1-10): "))
# d = 5    
n = d
sig = "#"
# ใช้ if ซ้อนกัน d รอบ
if d >= 1:
    print(sig*n)
    if d >= 2:
        print(sig*(n-1))
        if d >= 3:
            print(sig*(n-2))
            if d >= 4:
                print(sig*(n-3))
                if d >= 5:
                    print(sig*(n-4))
                    if d >= 6:
                        print(sig*(n-5))
                        if d >= 7:
                            print(sig*(n-6))
                            if d >= 8:
                                print(sig*(n-7))
                                if d >= 9:
                                    print(sig*(n-8))
                                    if d >= 10:
                                        print(sig*(n-9))