#pygame for creating a simple graphical interface for the Tic Tac Toe game
#sys or system-related functionality.
import pygame
import sys

#encapsulate the game logic and user interface.
class TicTacToe:

    #initializes the game by setting up constants, colors, Pygame, and creating the game window.
    def __init__(self):
        # Constants (sizeing)
        self.WIDTH, self.HEIGHT = 600, 600
        self.GRID_SIZE = 3
        self.CELL_SIZE = self.WIDTH // self.GRID_SIZE
        self.BORDER_WIDTH = 6
        self.LINE_WIDTH = 10

        # Colors
        self.LIGHT_BEIGE = (232, 229, 233) #background 
        self.GREY = (168, 174, 184) #border 
        self.LIGHT_BLUE = (185, 203, 217) #X symbol
        self.LIGHT_RED = (222, 196, 201) #O symbol

        # Initialize Pygame
        pygame.init()

        # Create the game window with the specified width and height
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic Tac Toe!!")

        #initialized by taking user input for their names.
        self.player_one = None
        self.player_two = None

        self.initialize_players()

        #is represented as a list of signs (X, O, or empty space).
        self.signs = [' '] * self.GRID_SIZE ** 2

    #prompts the users to input their names.
    def initialize_players(self):
        print("Tic Tac Toe!")
        print("Let's play!")

        while True:
            self.player_one = input("Enter player one name: ")
            if self.player_one.strip():  # Check if the input is not blank
                break
            else:
                print("Name cannot be blank. Please enter a valid name.")

        while True:
            self.player_two = input("Enter player two name: ")
            if self.player_two.strip():  # Check if the input is not blank
                break
            else:
                print("Name cannot be blank. Please enter a valid name.")

        print(f"Thank you for joining {self.player_one} and {self.player_two}")

    #draws the game board on the Pygame window using shapes and colors.
    def print_board(self):
        self.window.fill(self.LIGHT_BEIGE)
        
        # Draw border around the entire grid
        pygame.draw.rect(self.window, self.GREY, (0, 0, self.WIDTH, self.HEIGHT), self.BORDER_WIDTH)
        
        #The position and size are determined by row and col values, with the border width set by self.BORDER_WIDTH, creating a grid of cells.
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                pygame.draw.rect(self.window, self.GREY, (col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE), self.BORDER_WIDTH)

                #if the value is 'X', it calls the draw_x method to draw an 'X' symbol. If the value is 'O', it calls the draw_o method to draw an 'O' symbol. 
                sign = self.signs[row * self.GRID_SIZE + col]
                if sign == 'X':
                    self.draw_x(col * self.CELL_SIZE, row * self.CELL_SIZE)
                elif sign == 'O':
                    self.draw_o(col * self.CELL_SIZE + self.CELL_SIZE // 2, row * self.CELL_SIZE + self.CELL_SIZE // 2)

        #updates the display to reflect the changes made
        pygame.display.update()
        

    #takes x and y, which represent the starting coordinates for drawing the 'X' symbol.
    def draw_x(self, x, y):
        #pygame.draw.line to draw the first line of the 'X'
        #self.window: The Pygame window to draw on.
        #(x + 20, y + 20): Starting point of the line, offset by 20 pixels from the top-left corner of the cell.
        #(x + self.CELL_SIZE - 20, y + self.CELL_SIZE - 20): Ending point of the line, offset by 20 pixels from the bottom-right corner of the cell.
        pygame.draw.line(self.window, self.LIGHT_BLUE, (x + 20, y + 20), (x + self.CELL_SIZE - 20, y + self.CELL_SIZE - 20), self.LINE_WIDTH)
        #the difference is the starting and ending points. The starting point is now at the top-right corner, and the ending point is at the bottom-left corner.
        pygame.draw.line(self.window, self.LIGHT_BLUE, (x + self.CELL_SIZE - 20, y + 20), (x + 20, y + self.CELL_SIZE - 20), self.LINE_WIDTH)

    #x and y, which represent the center coordinates for drawing the 'O' symbol.
    #(x, y): The center coordinates of the circle, specified by the parameters of the method.
    #The circle's radius is calculated by subtracting 20 pixels from the cell size, ensuring it fits within the cell and doesn't overlap with the border.
    def draw_o(self, x, y):
        pygame.draw.circle(self.window, self.LIGHT_RED, (x, y), self.CELL_SIZE // 2 - 20, self.LINE_WIDTH)

   #doesn't take any additional parameters but belongs to the TicTacToe class.
    def take_input(self):
        #enters an infinite loop to continuously check for player input
        while True:
            #uses a for loop to iterate over the events (mouse clicks and window closure)
            for event in pygame.event.get():
                #exits the game window if the close button is clicked 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #handle the input
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #calculates the row and column based on the mouse click position
                    #determines the corresponding row and column
                    col = event.pos[0] // self.CELL_SIZE
                    row = event.pos[1] // self.CELL_SIZE

                    #calculates the linear index of the cell in the one-dimensional 
                    #calculated index is empty
                    #the player has selected a valid and empty cell
                    index = row * self.GRID_SIZE + col
                    if self.signs[index] == ' ':
                        return index

    def calculate_result(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        #iterates through each winning combination
        for combo in winning_combinations:
            #checks if the signs at the indices specified in the current winning combination are all equal to 'X'.
            if self.signs[combo[0]] == self.signs[combo[1]] == self.signs[combo[2]] == 'X':
                #prints the current board, announces the winner (player_one), and then exits the game
                self.print_board()
                print(f"Congrats {self.player_one}, you have won the game!!")
                pygame.quit()
                sys.exit()
            #checks if the signs at the indices specified in the current winning combination are all equal to 'O'.
            elif self.signs[combo[0]] == self.signs[combo[1]] == self.signs[combo[2]] == 'O':
                #prints the current board, announces the winner (player_two), and then exits the game
                self.print_board()
                print(f"Congrats {self.player_two}, you have won the game!!")
                pygame.quit()
                sys.exit()

    def main(self):
        #loop will continuously run until the user decides to exit the game
        while True:
            #display the current state of the game 
            self.print_board()
            #no more empty spaces on the board 
            #the game has ended in a tie
            #announces a tie, exits Pygame, and exits the script.
            if ' ' not in self.signs:
                self.print_board()
                print("This is a Tie")
                pygame.quit()
                sys.exit()

            #user clicking the close button on the window 
            #exits Pygame and the script.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #The player inputs using the take_input method and updates the board by placing either 'X' or 'O' in a selected cell, based on the player's fewer moves.
            if pygame.mouse.get_pressed()[0]:
                index = self.take_input()
                self.signs[index] = 'X' if len([s for s in self.signs if s == 'X']) <= len([s for s in self.signs if s == 'O']) else 'O'

                #to check if the current move has resulted in a win
                self.calculate_result()

#The script creates an instance of the TicTacToe class and initiates the main game loop, allowing reusable code by separating its main functionality from other scripts.
if __name__ == "__main__":
    game = TicTacToe()
    game.main()
