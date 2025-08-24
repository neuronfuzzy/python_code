#การแก้ไขตัวแปรที่เป็น global scope และแก้ไขตัวแปรที่เป็น local ที่อยู่ใน func. หลัก (Outer function)
#เมื่อต้องการให้แก้ไขค่า Global ก็ให้ใช้ key Global แต่ถ้าฟังก์ชั่นย่อยต้อวการแก้ไขตัวแปรที่อยู่ในฟังก์ชั่นหลักก็ให้ใช้คีย์เวริด์ nonlocal
my_global = 100
def outer_func():
    my_local = 50
    def inner_func():
        nonlocal my_local
        my_local = 10
        global my_global
        my_global = 99
    inner_func()
    print(my_local)

outer_func()        # 10
print(my_global)    # 99