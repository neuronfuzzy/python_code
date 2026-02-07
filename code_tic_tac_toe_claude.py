"""
8x8 Tic Tac Toe Game
เกม Tic Tac Toe ขนาด 8x8 โดยผู้เล่นต้องเรียง 5 ตัวติดกันเพื่อชนะ
ใช้ OOP และ Pygame ในการพัฒนา
"""

import pygame
import sys
from enum import Enum
from typing import Optional, List, Tuple


class Player(Enum):
    """Enum สำหรับกำหนดผู้เล่น"""
    NONE = 0
    X = 1
    O = 2


class GameState(Enum):
    """Enum สำหรับสถานะของเกม"""
    PLAYING = 1
    X_WIN = 2
    O_WIN = 3
    DRAW = 4


class Cell:
    """
    คลาสสำหรับแต่ละช่องในตาราง
    เก็บข้อมูลตำแหน่งและผู้เล่นที่ครองช่อง
    """
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.player = Player.NONE
        
    def mark(self, player: Player) -> bool:
        """ทำเครื่องหมายช่อง"""
        if self.player == Player.NONE:
            self.player = player
            return True
        return False
    
    def reset(self):
        """รีเซ็ตช่อง"""
        self.player = Player.NONE


class Board:
    """
    คลาสสำหรับจัดการตาราง 8x8
    ตรวจสอบการชนะและจัดการตำแหน่ง
    """
    def __init__(self, size: int = 8, win_length: int = 5):
        self.size = size
        self.win_length = win_length  # จำนวนที่ต้องเรียงติดกันเพื่อชนะ
        self.cells: List[List[Cell]] = []
        self.initialize_board()
        
    def initialize_board(self):
        """สร้างตารางเริ่มต้น"""
        self.cells = [[Cell(row, col) for col in range(self.size)] 
                      for row in range(self.size)]
    
    def get_cell(self, row: int, col: int) -> Optional[Cell]:
        """ดึงข้อมูลช่องจากตำแหน่ง"""
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.cells[row][col]
        return None
    
    def mark_cell(self, row: int, col: int, player: Player) -> bool:
        """ทำเครื่องหมายในช่อง"""
        cell = self.get_cell(row, col)
        if cell:
            return cell.mark(player)
        return False
    
    def check_winner(self) -> Player:
        """ตรวจสอบผู้ชนะ"""
        # ตรวจสอบแนวนอน
        for row in range(self.size):
            winner = self._check_line([(row, col) for col in range(self.size)])
            if winner != Player.NONE:
                return winner
        
        # ตรวจสอบแนวตั้ง
        for col in range(self.size):
            winner = self._check_line([(row, col) for row in range(self.size)])
            if winner != Player.NONE:
                return winner
        
        # ตรวจสอบแนวทแยงมุม (จากซ้ายบนไปขวาล่าง)
        for start_row in range(self.size - self.win_length + 1):
            for start_col in range(self.size - self.win_length + 1):
                winner = self._check_line([
                    (start_row + i, start_col + i) 
                    for i in range(self.win_length)
                ])
                if winner != Player.NONE:
                    return winner
        
        # ตรวจสอบแนวทแยงมุม (จากขวาบนไปซ้ายล่าง)
        for start_row in range(self.size - self.win_length + 1):
            for start_col in range(self.win_length - 1, self.size):
                winner = self._check_line([
                    (start_row + i, start_col - i) 
                    for i in range(self.win_length)
                ])
                if winner != Player.NONE:
                    return winner
        
        return Player.NONE
    
    def _check_line(self, positions: List[Tuple[int, int]]) -> Player:
        """ตรวจสอบแนวที่กำหนดว่ามีผู้ชนะหรือไม่"""
        for i in range(len(positions) - self.win_length + 1):
            segment = positions[i:i + self.win_length]
            first_cell = self.get_cell(segment[0][0], segment[0][1])
            
            if first_cell and first_cell.player != Player.NONE:
                if all(self.get_cell(r, c).player == first_cell.player 
                       for r, c in segment):
                    return first_cell.player
        
        return Player.NONE
    
    def is_full(self) -> bool:
        """ตรวจสอบว่าตารางเต็มหรือไม่"""
        return all(cell.player != Player.NONE 
                  for row in self.cells 
                  for cell in row)
    
    def reset(self):
        """รีเซ็ตตาราง"""
        for row in self.cells:
            for cell in row:
                cell.reset()


class GameRenderer:
    """
    คลาสสำหรับการแสดงผลด้วย Pygame
    รับผิดชอบการวาดตาราง, เครื่องหมาย, และข้อความ
    """
    def __init__(self, board: Board, cell_size: int = 60):
        self.board = board
        self.cell_size = cell_size
        self.width = board.size * cell_size
        self.height = board.size * cell_size + 60  # เพิ่มพื้นที่สำหรับแสดงสถานะ
        
        # สี
        self.BG_COLOR = (250, 248, 239)
        self.LINE_COLOR = (70, 70, 70)
        self.X_COLOR = (242, 85, 96)
        self.O_COLOR = (86, 174, 242)
        self.TEXT_COLOR = (50, 50, 50)
        self.BUTTON_COLOR = (100, 200, 100)
        
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tic Tac Toe 8x8')
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
    def draw(self, current_player: Player, game_state: GameState):
        """วาดหน้าจอเกมทั้งหมด"""
        self.screen.fill(self.BG_COLOR)
        self._draw_grid()
        self._draw_marks()
        self._draw_status(current_player, game_state)
        pygame.display.flip()
    
    def _draw_grid(self):
        """วาดเส้นตาราง"""
        # เส้นแนวนอน
        for i in range(self.board.size + 1):
            y = i * self.cell_size
            pygame.draw.line(self.screen, self.LINE_COLOR, 
                           (0, y), (self.width, y), 2)
        
        # เส้นแนวตั้ง
        for i in range(self.board.size + 1):
            x = i * self.cell_size
            pygame.draw.line(self.screen, self.LINE_COLOR, 
                           (x, 0), (x, self.board.size * self.cell_size), 2)
    
    def _draw_marks(self):
        """วาดเครื่องหมาย X และ O"""
        for row in range(self.board.size):
            for col in range(self.board.size):
                cell = self.board.get_cell(row, col)
                if cell.player == Player.X:
                    self._draw_x(row, col)
                elif cell.player == Player.O:
                    self._draw_o(row, col)
    
    def _draw_x(self, row: int, col: int):
        """วาดเครื่องหมาย X"""
        margin = self.cell_size // 4
        x1 = col * self.cell_size + margin
        y1 = row * self.cell_size + margin
        x2 = (col + 1) * self.cell_size - margin
        y2 = (row + 1) * self.cell_size - margin
        
        pygame.draw.line(self.screen, self.X_COLOR, (x1, y1), (x2, y2), 4)
        pygame.draw.line(self.screen, self.X_COLOR, (x2, y1), (x1, y2), 4)
    
    def _draw_o(self, row: int, col: int):
        """วาดเครื่องหมาย O"""
        center_x = col * self.cell_size + self.cell_size // 2
        center_y = row * self.cell_size + self.cell_size // 2
        radius = self.cell_size // 3
        
        pygame.draw.circle(self.screen, self.O_COLOR, 
                         (center_x, center_y), radius, 4)
    
    def _draw_status(self, current_player: Player, game_state: GameState):
        """แสดงสถานะเกมและปุ่ม"""
        status_y = self.board.size * self.cell_size + 10
        
        if game_state == GameState.PLAYING:
            text = f"ตาของผู้เล่น: {'X' if current_player == Player.X else 'O'}"
        elif game_state == GameState.X_WIN:
            text = "ผู้เล่น X ชนะ!"
        elif game_state == GameState.O_WIN:
            text = "ผู้เล่น O ชนะ!"
        else:
            text = "เสมอกัน!"
        
        text_surface = self.font.render(text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(self.width // 2, status_y + 15))
        self.screen.blit(text_surface, text_rect)
        
        # แสดงคำแนะนำ
        if game_state == GameState.PLAYING:
            hint = "(เรียง 5 ตัวติดกันเพื่อชนะ)"
            hint_surface = self.small_font.render(hint, True, self.TEXT_COLOR)
            hint_rect = hint_surface.get_rect(center=(self.width // 2, status_y + 40))
            self.screen.blit(hint_surface, hint_rect)
    
    def get_cell_from_mouse(self, pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        """แปลงตำแหน่งเมาส์เป็นตำแหน่งช่อง"""
        x, y = pos
        if y < self.board.size * self.cell_size:
            row = y // self.cell_size
            col = x // self.cell_size
            return (row, col)
        return None


class TicTacToeGame:
    """
    คลาสหลักสำหรับควบคุมเกม
    จัดการ game loop, การเล่น, และเหตุการณ์ต่างๆ
    """
    def __init__(self, board_size: int = 8, win_length: int = 5):
        self.board = Board(board_size, win_length)
        self.renderer = GameRenderer(self.board)
        self.current_player = Player.X
        self.game_state = GameState.PLAYING
        self.clock = pygame.time.Clock()
        
    def handle_click(self, pos: Tuple[int, int]):
        """จัดการการคลิกเมาส์"""
        if self.game_state != GameState.PLAYING:
            return
        
        cell_pos = self.renderer.get_cell_from_mouse(pos)
        if cell_pos:
            row, col = cell_pos
            if self.board.mark_cell(row, col, self.current_player):
                # ตรวจสอบผู้ชนะ
                winner = self.board.check_winner()
                if winner == Player.X:
                    self.game_state = GameState.X_WIN
                elif winner == Player.O:
                    self.game_state = GameState.O_WIN
                elif self.board.is_full():
                    self.game_state = GameState.DRAW
                else:
                    # สลับผู้เล่น
                    self.current_player = (Player.O if self.current_player == Player.X 
                                         else Player.X)
    
    def reset_game(self):
        """เริ่มเกมใหม่"""
        self.board.reset()
        self.current_player = Player.X
        self.game_state = GameState.PLAYING
    
    def run(self):
        """เริ่มต้น game loop"""
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # กด R เพื่อเริ่มเกมใหม่
                        self.reset_game()
                    elif event.key == pygame.K_ESCAPE:  # กด ESC เพื่อออก
                        running = False
            
            # แสดงผล
            self.renderer.draw(self.current_player, self.game_state)
            self.clock.tick(60)  # จำกัด FPS ที่ 60
        
        pygame.quit()
        sys.exit()


def main():
    """ฟังก์ชันหลักสำหรับเริ่มเกม"""
    game = TicTacToeGame(board_size=8, win_length=5)
    game.run()


if __name__ == "__main__":
    main()