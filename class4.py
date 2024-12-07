import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BG_COLOR = (50, 50, 50)  # Dark gray background
LINE_COLOR = (23, 145, 135)
WIN_LINE_COLOR = (255, 0, 0)  

# Grid settings
ROWS = 3
COLS = 3
SQUARE_SIZE = WIDTH // COLS

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic-Tac-Toe')
screen.fill(BG_COLOR)

# Load images
x_image = pygame.image.load('x_image.png')
x_image = pygame.transform.scale(x_image, (SQUARE_SIZE - 40, SQUARE_SIZE - 40))
o_image = pygame.image.load('o_image.png')
o_image = pygame.transform.scale(o_image, (SQUARE_SIZE - 40, SQUARE_SIZE - 40))

# Board representation
board = [[None] * COLS for _ in range(ROWS)]

winning_line = None  # 4

######## 4
# Winning line variables
winning_line_position = None
winning_line_rotation = 0
winner_message = ""  # Message to display when the game ends
#############

# Winning line variables
winning_line_start = None
winning_line_end = None
winner_message = ""  # Message to display when the game ends

# Functions
def draw_lines():
    """Draws the grid lines."""
    for row in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * row), (WIDTH, SQUARE_SIZE * row), LINE_WIDTH)
    for col in range(1, COLS):
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * col, 0), (SQUARE_SIZE * col, HEIGHT), LINE_WIDTH)

def draw_figures():
    """Draws X and O images on the board."""
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 'X':
                screen.blit(x_image, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20))
            elif board[row][col] == 'O':
                screen.blit(o_image, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20))

def check_winner(player):
    """Checks if the player has won."""
    global winning_line_start, winning_line_end, winner_message

    # Check rows
    for row in range(ROWS):
        if all([board[row][col] == player for col in range(COLS)]):
            winning_line_start = (0, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            winning_line_end = (WIDTH, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            winner_message = f"{player} Player Wins!"
            return True

    # Check columns
    for col in range(COLS):
        if all([board[row][col] == player for row in range(ROWS)]):
            winning_line_start = (col * SQUARE_SIZE + SQUARE_SIZE // 2, 0)
            winning_line_end = (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT)
            winner_message = f"{player} Player Wins!"
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(ROWS)]):
        winning_line_start = (0, 0)
        winning_line_end = (WIDTH, HEIGHT)
        winner_message = f"{player} Player Wins!"
        return True

    if all([board[i][ROWS - i - 1] == player for i in range(ROWS)]):
        winning_line_start = (0, HEIGHT)
        winning_line_end = (WIDTH, 0)
        winner_message = f"{player} Player Wins!"
        return True

    return False

    
def draw_win_line():
    """Draws the winning line directly."""
    if winning_line_start and winning_line_end:
        pygame.draw.line(screen, WIN_LINE_COLOR, winning_line_start, winning_line_end, LINE_WIDTH)

# Game variables
game_over = False 
player = 'X' 

# Draw grid
draw_lines()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        ###### 3#######
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE
            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = player
                if check_winner(player):  # Set game variables if a player wins
                    game_over = True
                player = 'O' if player == 'X' else 'X'
        #############
    # Draw everything
    screen.fill(BG_COLOR)
    draw_lines()
    draw_figures()
    draw_win_line() # 4

    pygame.display.update()
