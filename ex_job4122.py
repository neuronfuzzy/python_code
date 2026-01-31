class Employee:
    """คลาสสำหรับจัดการข้อมูลพนักงานและคำนวณโบนัส"""
    
    def __init__(self, name, salary, years_of_service):
        """
        สร้างอ็อบเจ็กต์พนักงาน
        
        Parameters:
        name (str): ชื่อพนักงาน
        salary (float): เงินเดือน
        years_of_service (float): อายุการทำงาน (ปี)
        """
        self.name = name
        self.salary = salary
        self.years_of_service = years_of_service
        self.bonus_rate = 0
        self.bonus_amount = 0
        self.total_income = 0
    
    def calculate_bonus(self):
        """คำนวณโบนัสตามอายุการทำงาน"""
        if self.years_of_service < 1:
            self.bonus_rate = 0
        elif 1 <= self.years_of_service <= 3:
            self.bonus_rate = 0.03  # 3%
        else:  # มากกว่า 3 ปี
            self.bonus_rate = 0.05  # 5%
        
        self.bonus_amount = self.salary * self.bonus_rate
        self.total_income = self.salary + self.bonus_amount
    
    def display_result(self):
        """แสดงผลการคำนวณ"""
        print("\n" + "="*50)
        print(f"ชื่อพนักงาน: {self.name}")
        print(f"อายุการทำงาน: {self.years_of_service} ปี")
        print(f"เงินเดือน: {self.salary:,.2f} บาท")
        
        if self.bonus_rate == 0:
            print("สถานะ: ไม่ได้รับโบนัส (อายุงานน้อยกว่า 1 ปี)")
        else:
            print(f"อัตราโบนัส: {self.bonus_rate * 100}%")
            print(f"เงินโบนัส: {self.bonus_amount:,.2f} บาท")
            print(f"รายได้รวม: {self.total_income:,.2f} บาท")
        print("="*50)


class BonusCalculator:
    """คลาสสำหรับจัดการระบบคำนวณโบนัส"""
    
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        """เพิ่มพนักงานเข้าระบบ"""
        self.employees.append(employee)
    
    def process_all_employees(self):
        """ประมวลผลและแสดงผลพนักงานทั้งหมด"""
        for employee in self.employees:
            employee.calculate_bonus()
            employee.display_result()
    
    def get_employee_input(self):
        """รับข้อมูลพนักงานจากผู้ใช้"""
        print("\n*** โปรแกรมคำนวณโบนัสพนักงาน ***")
        
        while True:
            try:
                name = input("\nชื่อพนักงาน: ")
                salary = float(input("เงินเดือน (บาท): "))
                years = float(input("อายุการทำงาน (ปี): "))
                
                if salary < 0 or years < 0:
                    print("⚠️ กรุณากรอกค่าที่เป็นบวก")
                    continue
                
                employee = Employee(name, salary, years)
                self.add_employee(employee)
                
                continue_input = input("\nต้องการเพิ่มพนักงานคนอื่นหรือไม่? (y/n): ")
                if continue_input.lower() != 'y':
                    break
                    
            except ValueError:
                print("⚠️ กรุณากรอกตัวเลขที่ถูกต้อง")
            except KeyboardInterrupt:
                print("\n\nโปรแกรมถูกยกเลิก")
                return False
        
        return True


# โปรแกรมหลัก
if __name__ == "__main__":
    calculator = BonusCalculator()
    
    if calculator.get_employee_input():
        print("\n\n*** ผลการคำนวณโบนัส ***")
        calculator.process_all_employees()
        
        # สรุปภาพรวม
        print("\n\n*** สรุปภาพรวม ***")
        print(f"จำนวนพนักงานทั้งหมด: {len(calculator.employees)} คน")
        total_salary = sum(emp.salary for emp in calculator.employees)
        total_bonus = sum(emp.bonus_amount for emp in calculator.employees)
        print(f"เงินเดือนรวม: {total_salary:,.2f} บาท")
        print(f"โบนัสรวม: {total_bonus:,.2f} บาท")
        print(f"รายจ่ายทั้งหมด: {total_salary + total_bonus:,.2f} บาท")