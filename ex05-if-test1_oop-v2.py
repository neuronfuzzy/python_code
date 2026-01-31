# แบบที่ 2: Advanced Pattern Generator with History
class PatternGenerator:
    """คลาสสำหรับสร้างและจัดการรูปแบบต่างๆ"""
    
    def __init__(self, symbol="*", max_count=5):
        self.symbol = symbol
        self.max_count = max_count
        self._pattern_history = []
    
    def generate_ascending(self):
        """สร้างรูปแบบเพิ่มขึ้น (1, 2, 3, ...)"""
        pattern = []
        for i in range(1, self.max_count + 1):
            pattern.append(self.symbol * i)
        return pattern
    
    def generate_descending(self):
        """สร้างรูปแบบลดลง (5, 4, 3, ...)"""
        pattern = []
        for i in range(self.max_count, 0, -1):
            pattern.append(self.symbol * i)
        return pattern
    
    def generate_pyramid(self):
        """สร้างรูปแบบพีระมิด (1, 2, 3, 2, 1)"""
        ascending = self.generate_ascending()
        descending = self.generate_descending()[1:]  # ไม่เอาตัวแรก
        return ascending + descending
    
    def print_pattern(self, pattern_type="ascending"):
        """
        พิมพ์รูปแบบตามประเภทที่เลือก
        
        Args:
            pattern_type: ประเภทรูปแบบ ('ascending', 'descending', 'pyramid')
        """
        if pattern_type == "ascending":
            pattern = self.generate_ascending()
        elif pattern_type == "descending":
            pattern = self.generate_descending()
        elif pattern_type == "pyramid":
            pattern = self.generate_pyramid()
        else:
            raise ValueError(f"ไม่รู้จักประเภท: {pattern_type}")
        
        for line in pattern:
            print(line)
        
        # เก็บประวัติ
        self._pattern_history.append({
            'type': pattern_type,
            'symbol': self.symbol,
            'max_count': self.max_count
        })
    
    def get_history(self):
        """ดูประวัติการสร้างรูปแบบ"""
        return self._pattern_history
    
    def __str__(self):
        """แสดงข้อมูลของ object"""
        return f"PatternGenerator(symbol='{self.symbol}', max_count={self.max_count})"


# วิธีใช้งาน
gen = PatternGenerator(symbol="*", max_count=5)

print("=== แบบเพิ่มขึ้น ===")
gen.print_pattern("ascending")

print("\n=== แบบลดลง ===")
gen.print_pattern("descending")

print("\n=== แบบพีระมิด ===")
gen.print_pattern("pyramid")

print("\n=== ข้อมูล Object ===")
print(gen)

print("\n=== ประวัติการใช้งาน ===")
for i, record in enumerate(gen.get_history(), 1):
    print(f"{i}. {record}")
