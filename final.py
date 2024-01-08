import pygame
import sys

class TicTacToe:
    def __init__(self):
        # Constants
        self.WIDTH, self.HEIGHT = 600, 600
        self.GRID_SIZE = 3
        self.CELL_SIZE = self.WIDTH // self.GRID_SIZE
        self.BORDER_WIDTH = 6
        self.LINE_WIDTH = 10

        # Colors
        self.LIGHT_BEIGE = (232, 229, 233)
        self.GREY = (168, 174, 184)
        self.LIGHT_BLUE = (185, 203, 217)
        self.LIGHT_RED = (222, 196, 201)

        # Initialize Pygame
        pygame.init()

        # Create the game window
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic Tac Toe!!")

        self.player_one = None
        self.player_two = None

        self.initialize_players()

        self.signs = [' '] * self.GRID_SIZE ** 2

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

    def print_board(self):
        self.window.fill(self.LIGHT_BEIGE)
        
        # Draw border around the entire grid
        pygame.draw.rect(self.window, self.GREY, (0, 0, self.WIDTH, self.HEIGHT), self.BORDER_WIDTH)
        
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                pygame.draw.rect(self.window, self.GREY, (col * self.CELL_SIZE, row * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE), self.BORDER_WIDTH)

                sign = self.signs[row * self.GRID_SIZE + col]
                if sign == 'X':
                    self.draw_x(col * self.CELL_SIZE, row * self.CELL_SIZE)
                elif sign == 'O':
                    self.draw_o(col * self.CELL_SIZE + self.CELL_SIZE // 2, row * self.CELL_SIZE + self.CELL_SIZE // 2)

        pygame.display.update()

    def draw_x(self, x, y):
        pygame.draw.line(self.window, self.LIGHT_BLUE, (x + 20, y + 20), (x + self.CELL_SIZE - 20, y + self.CELL_SIZE - 20), self.LINE_WIDTH)
        pygame.draw.line(self.window, self.LIGHT_BLUE, (x + self.CELL_SIZE - 20, y + 20), (x + 20, y + self.CELL_SIZE - 20), self.LINE_WIDTH)

    def draw_o(self, x, y):
        pygame.draw.circle(self.window, self.LIGHT_RED, (x, y), self.CELL_SIZE // 2 - 20, self.LINE_WIDTH)

    def take_input(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // self.CELL_SIZE
                    row = event.pos[1] // self.CELL_SIZE

                    index = row * self.GRID_SIZE + col
                    if self.signs[index] == ' ':
                        return index

    def calculate_result(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for combo in winning_combinations:
            if self.signs[combo[0]] == self.signs[combo[1]] == self.signs[combo[2]] == 'X':
                self.print_board()
                print(f"Congrats {self.player_one}, you have won the game!!")
                pygame.quit()
                sys.exit()
            elif self.signs[combo[0]] == self.signs[combo[1]] == self.signs[combo[2]] == 'O':
                self.print_board()
                print(f"Congrats {self.player_two}, you have won the game!!")
                pygame.quit()
                sys.exit()

    def main(self):
        while True:
            self.print_board()
            if ' ' not in self.signs:
                self.print_board()
                print("This is a Tie")
                pygame.quit()
                sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if pygame.mouse.get_pressed()[0]:
                index = self.take_input()
                self.signs[index] = 'X' if len([s for s in self.signs if s == 'X']) <= len([s for s in self.signs if s == 'O']) else 'O'

                self.calculate_result()

if __name__ == "__main__":
    game = TicTacToe()
    game.main()
