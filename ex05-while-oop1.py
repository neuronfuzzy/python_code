class Game:
    def __init__(self):
        self.players_in_game = 0
        self.is_game_over = False

    def add_player(self):
        if not self.is_game_over:
            self.players_in_game += 1
            print(f"มีผู้เล่น {self.players_in_game} คนในเกม")
        else:
            print("เกมจบแล้ว ไม่สามารถเพิ่มผู้เล่นได้")

    def check_game_state(self):
        # สมมติว่ามีกฎว่าถ้ามีผู้เล่น 5 คน เกมจะจบ
        while self.players_in_game < 5:
            print("รอผู้เล่นเพิ่ม...")
            # ในโลกจริง อาจมีเมธอดอื่นเรียก add_player หรือรอ input
            self.players_in_game += 1 # ตัวอย่างสมมติ
        self.is_game_over = True
        print("เกมเริ่มต้นแล้ว!")

game = Game()
game.check_game_state()
# game.add_player()  # จะไม่สามารถเพิ่มผู้เล่นได้เพราะเกมจบแล้ว