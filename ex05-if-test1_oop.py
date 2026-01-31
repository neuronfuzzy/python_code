class PatternPrinter:
    """คลาสสำหรับพิมพ์รูปแบบด้วยสัญลักษณ์"""
    
    def __init__(self, symbol="*", max_count=5):
        """
        กำหนดค่าเริ่มต้น
        
        Args:
            symbol: สัญลักษณ์ที่จะพิมพ์
            max_count: จำนวนรอบสูงสุด
        """
        self.symbol = symbol
        self.max_count = max_count
    
    def print_pattern(self):
        """พิมพ์รูปแบบตามจำนวนรอบที่กำหนด"""
        for i in range(1, self.max_count + 1):
            print(self.symbol * i)
    
    def set_symbol(self, new_symbol):
        """เปลี่ยนสัญลักษณ์"""
        self.symbol = new_symbol
    
    def set_max_count(self, new_count):
        """เปลี่ยนจำนวนรอบ"""
        self.max_count = new_count


# วิธีใช้งาน
printer = PatternPrinter(symbol="*", max_count=5)
printer.print_pattern()

print("\n--- เปลี่ยนเป็น # ---")
printer.set_symbol("#")
printer.set_max_count(5)
printer.print_pattern()