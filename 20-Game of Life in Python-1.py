# Requirements
from dataclasses import dataclass
import tkinter
from random import random
import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 9:
    listtype = list
else:
    from typing import List
    listtype = List

# Creating the Cells
@dataclass
class Cell:
    value: int
    marked: bool = False
    
boardtype = listtype[listtype[Cell]]

# Creating the board
board = list()
for i in range(10):
    board.append(list())
    for j in range(10):
        board[-1].append(Cell((i+j) % 2))

# Random Initializer
def random_init(board:boardtype) -> None:
    for i in range(len(board)):
        for j in range(len(board[0])):
            a = random()
            board[i][j].marked = False
            if a < 0.5:
                board[i][j].value = 0
            else:
                board[i][j].value = 1

# Updating Field
def update_field(f: tkinter.Canvas) -> None:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j].value == 1:
                field.create_rectangle(i*21, j*21, i*21 + 20,j*21 + 20, fill='chartreuse2')
            else:
                field.create_rectangle(i*21, j*21, i*21 + 20, j*21+20, fill='brown4')

# Creating the radio buttons
root = tkinter.Tk()
field = tkinter.Canvas(root, width=220,height=220)
field.pack()
next_button = tkinter.Button(root, text="Next Iteration", command=lambda : run_and_canvas(board, field))
next_button.pack()
init_button = tkinter.Button(root, text="New Initialization", command=lambda : random_init_tk(board, field))
init_button.pack()
tkinter.mainloop()

# Creating the algorithm neighbours:
if row == 0 and col == 0:
    if board[row][col+1].value == 1:
        alive_cells += 1
    if board[row+1][col+1].value == 1:
        alive_cells += 1
    if board[row+1][col].value == 1:
        alive_cells += 1
elif row == 0 and col==len(board)-1:
    if board[row][col-1].value == 1:
        alive_cells += 1
    if board[row-1][col-1].value == 1:
        alive_cells += 1
    if board[row-1][col].value == 1:
        alive_cells += 1
elif row == len(board)-1 and col==0:
    if board[row-1][col].value == 1:
        alive_cells += 1
    if board[row-1][col+1].value == 1:
        alive_cells += 1
    if board[row][col+1].value == 1:
        alive_cells += 1
elif row == len(board)-1 and col == len(board)-1:
    if board[row-1][col].value == 1:
        alive_cells += 1
    if board[row-1][col-1].value == 1:
        alive_cells += 1
    if board[row][col-1].value == 1:
        alive_cells += 1
# 

def calculate_neighbours(board: list[list[Cell]], row: int, col: int):
    neighbours = 0
    for i in range(row-1,row+2):
        for j in range(col-1, col+2):
            if i >= 0 and j >= 0 and i < len(board) and j < len(board[0]):
                neighbours += board[i][j].value 
    neighbours -= board[row][col].value 
    return neighbours