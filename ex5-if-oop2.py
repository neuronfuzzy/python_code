class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.is_alive = True

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
            print(f"{self.name} ถูกกำจัดแล้ว!")
        else:
            print(f"{self.name} เหลือพลังชีวิต {self.health}")

player1 = Player("Hero")
player1.take_damage(50)
player1.take_damage(60) # เงื่อนไข is_alive จะถูกเปลี่ยนเป็น False
