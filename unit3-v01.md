# [exam_job3.py]
example =>> Math แบบ OOP

```python
import math

class GeometryCalculator:
    """คลาสหลักสำหรับคำนวณเรขาคณิต"""
    
    # ค่าคงที่ Pi
    PI = 3.1416
    
    def __init__(self):
        """Constructor"""
        pass
    
    def get_positive_input(self, prompt):
        """รับค่าจากผู้ใช้และตรวจสอบว่าเป็นค่าบวก"""
        while True:
            try:
                value = float(input(prompt))
                if value > 0:
                    return value
                else:
                    print("กรุณาป้อนค่าที่มากกว่า 0")
            except ValueError:
                print("กรุณาป้อนตัวเลขที่ถูกต้อง")


class Sphere(GeometryCalculator):
    """คลาสสำหรับคำนวณทรงกลม"""
    
    def __init__(self, radius):
        """
        Constructor
        Parameters:
            radius (float): รัศมีของทรงกลม
        """
        super().__init__()
        self.radius = radius
    
    def calculate_volume(self):
        """
        คำนวณปริมาตรทรงกลม
        สูตร: V = (4/3) * π * r³
        Returns:
            float: ปริมาตรทรงกลม
        """
        volume = (4/3) * self.PI * (self.radius ** 3)
        return volume
    
    def calculate_surface_area(self):
        """
        คำนวณพื้นที่ผิวทรงกลม
        สูตร: A = 4 * π * r²
        Returns:
            float: พื้นที่ผิวทรงกลม
        """
        surface_area = 4 * self.PI * (self.radius ** 2)
        return surface_area
    
    def display_results(self):
        """แสดงผลลัพธ์การคำนวณ"""
        print(f"\n--- ทรงกลม ---")
        print(f"รัศมี (r) = {self.radius:.2f} หน่วย")
        print(f"ปริมาตร = {self.calculate_volume():.4f} ลูกบาศก์หน่วย")
        print(f"พื้นที่ผิว = {self.calculate_surface_area():.4f} ตารางหน่วย")


class Cylinder(GeometryCalculator):
    """คลาสสำหรับคำนวณทรงกระบอก"""
    
    def __init__(self, radius, height):
        """
        Constructor
        Parameters:
            radius (float): รัศมีของทรงกระบอก
            height (float): ความสูงของทรงกระบอก
        """
        super().__init__()
        self.radius = radius
        self.height = height
    
    def calculate_volume(self):
        """
        คำนวณปริมาตรทรงกระบอก
        สูตร: V = π * r² * h
        Returns:
            float: ปริมาตรทรงกระบอก
        """
        volume = self.PI * (self.radius ** 2) * self.height
        return volume
    
    def display_results(self):
        """แสดงผลลัพธ์การคำนวณ"""
        print(f"\n--- ทรงกระบอก ---")
        print(f"รัศมี (r) = {self.radius:.2f} หน่วย")
        print(f"ความสูง (h) = {self.height:.2f} หน่วย")
        print(f"ปริมาตร = {self.calculate_volume():.4f} ลูกบาศก์หน่วย")


class MainProgram:
    """คลาสหลักสำหรับรันโปรแกรม"""
    
    def __init__(self):
        """Constructor"""
        self.calculator = GeometryCalculator()
    
    def show_menu(self):
        """แสดงเมนูหลัก"""
        print("\n" + "="*50)
        print("โปรแกรมคำนวณเรขาคณิต 3 มิติ")
        print("="*50)
        print("1. คำนวณปริมาตรทรงกลม")
        print("2. คำนวณพื้นที่ผิวทรงกลม")
        print("3. คำนวณปริมาตรทรงกระบอก")
        print("4. ออกจากโปรแกรม")
        print("="*50)
    
    def run(self):
        """เรียกใช้งานโปรแกรมหลัก"""
        while True:
            self.show_menu()
            choice = input("เลือกเมนู (1-4): ")
            
            if choice == '1':
                # คำนวณปริมาตรทรงกลม
                r = self.calculator.get_positive_input("ป้อนรัศมีของทรงกลม (r): ")
                sphere = Sphere(r)
                print(f"\nปริมาตรทรงกลม = {sphere.calculate_volume():.4f} ลูกบาศก์หน่วย")
                
            elif choice == '2':
                # คำนวณพื้นที่ผิวทรงกลม
                r = self.calculator.get_positive_input("ป้อนรัศมีของทรงกลม (r): ")
                sphere = Sphere(r)
                print(f"\nพื้นที่ผิวทรงกลม = {sphere.calculate_surface_area():.4f} ตารางหน่วย")
                
            elif choice == '3':
                # คำนวณปริมาตรทรงกระบอก
                r = self.calculator.get_positive_input("ป้อนรัศมีของทรงกระบอก (r): ")
                h = self.calculator.get_positive_input("ป้อนความสูงของทรงกระบอก (h): ")
                cylinder = Cylinder(r, h)
                print(f"\nปริมาตรทรงกระบอก = {cylinder.calculate_volume():.4f} ลูกบาศก์หน่วย")
                
            elif choice == '4':
                print("\nขอบคุณที่ใช้งานโปรแกรม")
                break
                
            else:
                print("\nกรุณาเลือกเมนู 1-4 เท่านั้น")


# เรียกใช้งานโปรแกรม
if __name__ == "__main__":
    program = MainProgram()
    program.run()

```
output out_ex5-if-oop.py
<img width="333" height="85" alt="Image" src="" />

Diagram flow chart:
```mermaid

```
[.py]
```python


```

```mermaid
graph TD
 
```
[.py]
```python


```
Flowchart Diagram
```mermaid
flowchart TD
    A([เริ่มต้นเรียกเมธอด attack]) --> B{hp > 0 ?}
    
    B -- ใช่ --> C{is_attacking == True ?}
    
    C -- ใช่ --> D[/แสดงผล: กำลังโจมตี.../]
    C -- ไม่ใช่ --> E[/แสดงผล: กำลังตั้งหลัก.../]
    
    D --> F[hp -= 10]
    E --> F
    
    F --> B
    
    B -- ไม่ใช่ --> G[/แสดงผล: ถูกกำจัดแล้ว!/]
    G --> H([จบการทำงาน])    
```
[.py]
```python


```
```mermaid
flowchart TD
   
```



```python

```
[exam_job412.py โจทย์ในแบบฝึกหัดที่4.12 ใน Classroom]
```python

```
```mermaid
flowchart TD
 
    
```
flow แบบ  Sequence Diagram (Mermaid Diagram)
```mermaid
sequenceDiagram
    actor User as ผู้ใช้งาน
    participant Main as Main Program
    participant HSC as HighwaySafetyChecker
    participant Method as Internal Methods
    
    User->>Main: เรียกใช้โปรแกรม
    Main->>User: ขอข้อมูล (carDensity, speed)
    User->>Main: ป้อนข้อมูล
    
    Main->>HSC: สร้าง Object<br/>HighwaySafetyChecker(carDensity, speed)
    activate HSC
    
    HSC->>HSC: เก็บค่า self.car_density<br/>และ self.speed
    HSC->>Method: เรียก _calculate_safe_speed_limit()
    activate Method
    
    alt carDensity <= 3
        Method-->>HSC: return 120
    else carDensity <= 5
        Method-->>HSC: return 90
    else carDensity > 5
        Method-->>HSC: return 60
    end
    deactivate Method
    
    HSC->>HSC: เก็บค่า self.safe_speed_limit
    HSC-->>Main: Object สร้างเสร็จ
    deactivate HSC
    
    Main->>HSC: เรียก check_safety()
    activate HSC
    
    HSC->>HSC: เปรียบเทียบ speed<br/>กับ safe_speed_limit
    
    alt speed <= safe_speed_limit
        HSC->>HSC: is_safe = True
    else speed > safe_speed_limit
        HSC->>HSC: is_safe = False
    end
    
    HSC->>Method: เรียก _generate_message(is_safe)
    activate Method
    
    alt is_safe == True
        Method-->>HSC: return "ปลอดภัย..."
    else is_safe == False
        Method-->>HSC: return "เตือน: กรุณาระวังตัว..."
    end
    deactivate Method
    
    HSC->>HSC: สร้าง result dictionary<br/>{car_density, speed, safe_speed_limit,<br/>is_safe, message}
    HSC-->>Main: return result
    deactivate HSC
    
    Main->>HSC: เรียก display_result()
    activate HSC
    HSC->>HSC: เรียก check_safety()
    HSC->>HSC: จัดรูปแบบข้อความ
    HSC->>User: แสดงผลการตรวจสอบ<br/>และข้อความเตือน
    deactivate HSC
    
    User->>Main: ตรวจสอบผลลัพธ์
    Main-->>User: สิ้นสุดการทำงาน
    
    Note over User,Method: กรณีที่ไม่ปลอดภัย<br/>ระบบจะแจ้งเตือนให้ผู้ขับระวังตัว
    
```


[ex_job4122-classroom.py :>> classroom 2-68]
```python

  
```
<img width="402" height="328" alt="Image" src="./out_ex_job4122-class2-68.jpg" />

```mermaid
flowchart TD
    Start([เริ่มต้นโปรแกรม]) --> Input1[รับข้อมูล: ชื่อพนักงาน]
    Input1 --> Input2[รับข้อมูล: เงินเดือน]
    Input2 --> Input3[รับข้อมูล: อายุการทำงาน]
    Input3 --> Validate{ข้อมูลถูกต้อง?<br/>เงินเดือน >= 0<br/>อายุงาน >= 0}
    Validate -->|ไม่| Error[แสดงข้อความ Error]
    Error --> Input1
    Validate -->|ใช่| CreateObj[สร้าง Object Employee]
    CreateObj --> CalcBonus[เรียก Method<br/>calculate_bonus]
    CalcBonus --> Check1{อายุงาน < 1 ปี?}
    Check1 -->|ใช่| Bonus0[โบนัส = 0%<br/>เงินโบนัส = 0]
    Check1 -->|ไม่| Check2{อายุงาน <= 3 ปี?}
    Check2 -->|ใช่| Bonus3[โบนัส = 3%<br/>เงินโบนัส = เงินเดือน × 0.03]
    Check2 -->|ไม่| Bonus5[โบนัส = 5%<br/>เงินโบนัส = เงินเดือน × 0.05]
    Bonus0 --> CalcTotal[คำนวณรายได้รวม<br/>total_income = salary + bonus]
    Bonus3 --> CalcTotal
    Bonus5 --> CalcTotal
    CalcTotal --> Display[แสดงผลลัพธ์:<br/>- ชื่อพนักงาน<br/>- อายุการทำงาน<br/>- เงินเดือน<br/>- เงินโบนัส<br/>- รายได้รวม]
   Display --> Continue{ต้องการเพิ่ม<br/>พนักงานอื่น?}
   Continue -->|ใช่| Input1
   Continue -->|ไม่| Summary[แสดงสรุปภาพรวม:<br/>- จำนวนพนักงาน<br/>- เงินเดือนรวม<br/>- โบนัสรวม<br/>- รายจ่ายทั้งหมด]
   Summary --> End([จบโปรแกรม])
    style Start fill:#90EE90
    style End fill:#FFB6C1
    style Check1 fill:#FFE4B5
    style Check2 fill:#FFE4B5
    style Validate fill:#FFE4B5
    style Continue fill:#FFE4B5
    style Error fill:#FF6B6B
    style Bonus0 fill:#87CEEB
    style Bonus3 fill:#87CEEB
    style Bonus5 fill:#87CEEB
```
flow Sequence Diagram ระบบการคำนวณโบนัสพนักงาน
```mermaid
sequenceDiagram
    actor User as ผู้ใช้
    participant Main as Main Program
    participant BC as BonusCalculator
    participant Emp as Employee
    
    User->>Main: เริ่มโปรแกรม
    Main->>BC: สร้าง Object BonusCalculator()
    activate BC
    
    Main->>BC: get_employee_input()
    activate BC
    
    loop สำหรับแต่ละพนักงาน
        BC->>User: ขอข้อมูล: ชื่อ, เงินเดือน, อายุงาน
        User->>BC: กรอกข้อมูล
        
        alt ข้อมูลไม่ถูกต้อง
            BC->>User: แสดง Error Message
        else ข้อมูลถูกต้อง
            BC->>Emp: สร้าง Employee(name, salary, years)
            activate Emp
            Emp-->>BC: return employee object
            BC->>BC: add_employee(employee)
            BC->>User: ถามว่าต้องการเพิ่มพนักงานอื่นหรือไม่?
            User->>BC: ตอบ (y/n)
        end
    end
    
    deactivate BC
    BC-->>Main: return True/False
    
    Main->>BC: process_all_employees()
    activate BC
    
    loop สำหรับพนักงานแต่ละคน
        BC->>Emp: calculate_bonus()
        activate Emp
        
        alt อายุงาน < 1 ปี
            Emp->>Emp: bonus_rate = 0%
        else อายุงาน 1-3 ปี
            Emp->>Emp: bonus_rate = 3%
        else อายุงาน > 3 ปี
            Emp->>Emp: bonus_rate = 5%
        end
        
        Emp->>Emp: คำนวณ bonus_amount
        Emp->>Emp: คำนวณ total_income
        deactivate Emp
        
        BC->>Emp: display_result()
        activate Emp
        Emp->>User: แสดงผลลัพธ์<br/>(ชื่อ, อายุงาน, เงินเดือน, โบนัส, รายได้รวม)
        deactivate Emp
    end
    
    deactivate BC
    
    Main->>Main: คำนวณสรุปภาพรวม
    Main->>User: แสดงสรุป<br/>(จำนวนพนักงาน, เงินเดือนรวม, โบนัสรวม)
    
    deactivate BC
    Main->>User: จบโปรแกรม
   
```


```python

    
```
<img width="402" height="328" alt="Image" src="./" />
```mermaid

    
```
```mermaid

    
```

```mermaid
graph TD
    
```