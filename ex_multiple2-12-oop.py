# ใช้เป็นข้อสอบ ข้อ 2 10 คะแนน 2-68 IT67-01 แบบ OOP
class MultiplicationTable:
    def __init__(self, start=2, end=12):
        self.start = start
        self.end = end
        self.current = start
        
    def is_valid_range(self):
        """ตรวจสอบว่าช่วงที่กำหนดถูกต้องหรือไม่"""
        if self.start < 2 or self.end > 12:
            return False
        if self.start > self.end:
            return False
        return True
    
    def print_header(self, num):
        """พิมพ์หัวข้อของแต่ละแม่"""
        print(f"\n{'='*40}")
        print(f"          แม่ {num} ")
        print(f"{'-'*40}")
        
    def print_one_row(self, num, multiplier):
        """พิมพ์แถวเดียว เช่น  5 x 8 = 40"""
        result = num * multiplier
        print(f"   {num:2d} x {multiplier:2d} = {result:3d}")
        
    def print_table(self, num):
        """พิมพ์ตารางของแม่สูตรคูณ 1 ตัว"""
        self.print_header(num)
        
        multiplier = 1
        while multiplier <= 12:
            self.print_one_row(num, multiplier)
            multiplier += 1
            
        print()  # เว้นบรรทัดหลังจบแต่ละแม่
    
    def show_all_tables(self):
        """แสดงแม่สูตรคูณทั้งหมดตามช่วงที่กำหนด"""
        if not self.is_valid_range():
            print("ช่วงที่ระบุไม่ถูกต้อง ต้องเป็น 2-12 เท่านั้น")
            return
            
        print("โปรแกรมแม่สูตรคูณ".center(40))
        print(f"แสดงตั้งแต่แม่ {self.start} ถึงแม่ {self.end}\n")
        
        current = self.start
        while current <= self.end:
            self.print_table(current)
            current += 1
            
        print(f"{'='*40}")
        print("     จบการแสดงแม่สูตรคูณทั้งหมด")
        print(f"{'='*40}")


# ==================== ใช้งานโปรแกรม ====================
def main():
    # สร้าง object ของคลาส MultiplicationTable
    table = MultiplicationTable(start=2, end=12)
    
    # เรียกใช้เมธอดเพื่อแสดงผลทั้งหมด
    table.show_all_tables()
    
    # ถ้าต้องการแสดงแค่บางแม่ก็ทำได้ เช่น
    # table2 = MultiplicationTable(5, 7)
    # table2.show_all_tables()


if __name__ == "__main__":
    main()
# โปรแกรมแม่สูตรคูณ 2-12 (ใช้ OOP และ if เพื่อจัดรูปแบบ)
# ใช้ OOP จริง (มี class, method แยกหน้าที่ชัดเจน)
# ใช้ while loop ตามที่ขอ
# มี if ตรวจสอบช่วงที่ถูกต้อง
# แยกหน้าที่แต่ละส่วนเป็น method (single responsibility)
# อ่านง่าย แก้ไข/ขยายต่อได้สะดวก
# สามารถปรับช่วงแม่ได้ง่าย ๆ แค่เปลี่ยนค่าใน MultiplicationTable(start=..., end=...)

# ถ้าต้องการปรับแต่ง เช่น

# อยากให้แสดงแค่ 1–10 แทน 1–12
# อยากให้มีสี (ใช้ ANSI color)
# อยากให้เลือกแสดงแม่เดียวผ่าน input