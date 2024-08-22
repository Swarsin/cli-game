#Author: Swaraj Singh

import random

class Board:
    def __init__(self, board):
        self.board = board

    #displays the board
    def print_board(self):
        print("  1 2 3 4 5 6 7 8")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Battleship:
    def __init__(self, board):
        self.board = board
    
    #creates 5 ships and places on the 
    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board
    
    #gets input from the user and validates input until valid row and column is entered
    @staticmethod #decorator which shows that this is a static method - a method that belongs to a class rather than instance of the class (object) - this allows me to use recursion to check for a valid input
    def enter(self): #enter row and column, validates using recursion
        x_row = int(input("Enter row of ship: "))
        y_column = int(input("Enter column of ship: "))
        if x_row < 0 or x_row >= 8 or y_column < 0 or y_column >= 8: #recursive case
            print("Invalid row and/or column")
            Battleship.enter(self)
        return x_row - 1, y_column - 1

    #returns how many ships were hit within the duration of the game
    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships

# checks if already guessed the square
def already_guessed():
    if user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "X":
        return True
    return False    

def Game():
    computer_board = Board([[" "] * 8 for i in range(8)])
    user_guess_board = Board([[" "] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)
    turns = 10
    while turns > 0:
        Board.print_board(user_guess_board)
        user_x_row, user_y_column = Battleship.enter(object)
        
        # checks if square has already been guessed
        while (
            user_guess_board.board[user_x_row][user_y_column] == "-"
            or user_guess_board.board[user_x_row][user_y_column] == "X"
        ):
            print("Already guessed!")
            user_x_row, user_y_column = Battleship.enter(object)
        
        #checks for hit or miss
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("Hit!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("Miss!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        
        #checks for user win or loss
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print("You hit all 5 battleships!")
            break
        else:
            turns -= 1
            print(f"You have {turns} turns remaining")
            if turns == 0:
                print("No more turns remaining")
                Board.print_board(user_guess_board)
                break

Game()

