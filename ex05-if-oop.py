class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def can_vote(self):
        if self.age >= 50:
            return f"{self.name} สามารถลงคะแนนได้"
        else:
            return f"{self.name} ยังไม่สามารถลงคะแนนได้"

# สร้าง Object
person1 = Person("aj@Ratiwat", 59)
person2 = Person("ผศ.ดร.ธงรบ", 48)
person3 = Person("นางสาวสุดารัตน์", 30)
person4 = Person("นายสมชาย", 50)
print(person1.can_vote()) # Output: aj@Ratiwat สามารถลงคะแนนได้
print(person2.can_vote()) # Output: ผศ.ดร.ธงรบ ยังไม่สามารถลงคะแนนได้
print(person3.can_vote()) # Output: นางสาวสุดารัตน์ ยังไม่สามารถลงคะแนนได้
print(person4.can_vote()) # Output: นายสมชาย สามารถลงคะแนนได้
