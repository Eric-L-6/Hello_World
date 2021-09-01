#Simple sudoku solver
#Written by Eric Lin www.linkedin.com/in/eric-lin-8b3b4520b
#Began 31/08/2021

import time
import random

class Board():

    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def print_board(self):
        for i in range(9):

            if (i != 0 and i % 3 == 0):
                print("------+-------+------")

            for j in range(9):
                if (j != 0 and j % 3 == 0):
                    print("| ", end = '') 
                print(f"{self.board[i][j]} ", end = '')
                if j == 8:
                    print("")
    
    def check_valid(self, row, col, num):
        #valid if unique in row, column and box
        top_left = (row - row % 3, col - col % 3)
        if self.invalid_row(row, num) or self.invalid_col(col,num) or self.invalid_box(top_left,num):
            return False
        else:
            return True
    
    def invalid_box(self,top_left,num):
        #top_left input as tuple (row,col)
        row,col = top_left
        for i in range(3):
            for j in range(3):
                if self.board[row + i][col + j] == num:
                    return True
        return False

    def invalid_row(self,row,num):
        return num in self.board[row]
    
    def invalid_col(self,col,num):
        for i in range(9):
            if self.board[i][col] == num:
                return True
        return False

    #returns tuple of empty coord
    #else returns false
    def empty(self):

        for i in range (9):
            for j in range (9):
                if self.board[i][j] == 0:
                    return (i,j)
        return False

    #returns integer count of non-empty boxes
    #used for generating new sudoku box
    def count_filled(self):
        count = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    count += 1
        return count

    #returns true boolean if sudoku is not empty
    def solve_backtrack(self):
        
        if self.empty() == False:
            return True
        else:
            row,col = self.empty()
            for num in range(1,10):
                if self.check_valid(row,col,num) == True:
                    self.board[row][col] = num
                    if (self.solve_backtrack() == True):
                        return True
                    self.board[row][col] = 0
            return False

    #used to create completed random board
    def fill_random(self):

        if self.empty() == False:
            return True
        else:
            row,col = self.empty()
            for i in range(1,10):
                num = random.randint(1,9)
                if self.check_valid(row,col,num) == True:
                    self.board[row][col] = num
                    if (self.solve_backtrack() == True):
                        return True
                    self.board[row][col] = 0
            return False

#generates new sudoku game
#for now, generates pseudo sudoku board
def generate_new(new,difficulty):
    #difficulty: hard, medium, easy
    #hard: 17 clues
    #medium: 27 clues
    #easy: 37 clues

    clues = 7
    if difficulty[0].lower() == "h":
        clues += 10
    elif difficulty[0].lower() == "m":
        clues += 20
    elif difficulty[0].lower() == "e":
        clues += 30

    new.fill_random()
    while new.count_filled() > clues:
        i = random.randint(0,8)
        j = random.randint(0,8)
        new.board[i][j] = 0  




if __name__ == "__main__":
    
    while True: 
        print("Choose difficulty:")
        new = Board()
        generate_new(new,input("Hard, medium, or easy: "))
        print("\nOriginal Sudoku board")
        new.print_board()

        input("\nEnter any key to continue: ")
        start_time = time.time()
        #new_board.solve_backtrack()
        new.fill_random()
        end_time = time.time()

        print("\nSolved Sudoku board")
        new.print_board()
        print(f"Total time elapsed: {end_time - start_time} seconds")

        if input("Continue playing? y/n ")[0].lower == "y":
            continue
        else:
            print("Thanks for playing! ")
            break