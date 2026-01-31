class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.is_attacking = False

    def attack(self):
        while self.hp > 0: # ตราบใดที่ศัตรูยังไม่ตาย
            if self.is_attacking:
                print(f"{self.name} กำลังโจมตี...")
                # ตรวจสอบว่าผู้เล่นตายไหม (สมมติว่ามีเมธอด check_player_alive)
                # if not player.is_alive: break # ถ้าผู้เล่นตายให้หยุดโจมตี
            else:
                print(f"{self.name} กำลังตั้งหลัก...")
            self.hp -= 10 # ลดพลังชีวิตลง
        print(f"{self.name} ถูกกำจัดแล้ว!")

enemy = Enemy("aj@Ratiwat", 100)
enemy.is_attacking = True # ตั้งค่าให้เริ่มโจมตี
enemy.attack() # เริ่มการทำงานของเมธอด attack
