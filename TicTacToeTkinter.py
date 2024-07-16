import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.buttons = []
        self.create_buttons()
    
    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font='normal 20 bold', height=3, width=6, command=lambda i=i: self.click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
    
    def click(self, index):
        if self.board[index] == " " and self.check_winner() is False:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)             # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
