class Person:
    def __init__(self, name, age , id_std ,grade):
        self.name = name
        self.age = age
        self.id_std = id_std
        self.grade = grade
        
    def introduceyourself(self):
        print("ฉันชื่อ : " + self.name)
        print("อายุคุณคือ " + str(self.age))
        print("รหัส : " + str(self.id_std))
        print("เกรด :" + str(self.grade))
        # show = input("เกรดของคุณคือ :>>")

        
class Teacher(Person): #this class inherits the class above!
    def stateprofession(self):
        print("ฉันคือมนุษย์ ตัวน้อยๆ!")
        name = input("Enter your name >>> ")
        print("ชื่อเทพ ของฉันคือ :" + str(name))
#Explanation:
author = Teacher("ajรติวัฒน์",59 ,"671234568" ,"A")
author.introduceyourself()
author.stateprofession()
