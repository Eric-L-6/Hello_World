#Simple sudoku solver
#Written by Eric Lin www.linkedin.com/in/eric-lin-8b3b4520b
#Began 31/08/2021

import time

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
    
    def random(self):
     #in future: used to generate a new random sudoku board
     #currently: enters a premade sudoku board from internet
        self.board = [
            [0,0,0,8,0,1,0,0,0],
            [0,0,0,0,0,0,4,3,0],
            [5,0,0,0,0,0,0,0,0],
            [0,0,0,0,7,0,8,0,0],
            [0,0,0,0,0,0,1,0,0],
            [0,2,0,0,3,0,0,0,0],
            [6,0,0,0,0,0,0,7,5],
            [0,0,3,4,0,0,0,0,0],
            [0,0,0,2,0,0,6,0,0]
        ]

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

                    



if __name__ == "__main__":
    new_board = Board()
    new_board.random()
    print("Original Sudoku board")
    new_board.print_board()

    start_time = time.time()
    new_board.solve_backtrack()
    end_time = time.time()

    print("\nSolved Sudoku board")
    new_board.print_board()
    print(f"Total time elapsed: {end_time - start_time} seconds")