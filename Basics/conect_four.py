import turtle

# Board settings
ROWS = 6
COLS = 7
SIZE = 80

WIDTH = COLS * SIZE
HEIGHT = ROWS * SIZE

# Colors
BLUE = "blue"
RED = "red"
YELLOW = "yellow"
BLACK = "black"

# Game board
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
player = 1
game_over = False

# Turtle setup
screen = turtle.Screen()
screen.setup(WIDTH + 100, HEIGHT + 100)
screen.title("Connect Four")
screen.bgcolor(BLACK)
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


def draw_square(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    pen.fillcolor(color)
    pen.begin_fill()

    for _ in range(4):
        pen.forward(SIZE)
        pen.right(90)

    pen.end_fill()


def draw_circle(x, y, color):
    pen.penup()
    pen.goto(x + SIZE // 2, y - SIZE // 2 - 5)
    pen.dot(SIZE - 15, color)


def draw_board():
    pen.clear()

    start_x = -(WIDTH // 2)
    start_y = HEIGHT // 2

    for r in range(ROWS):
        for c in range(COLS):
            x = start_x + c * SIZE
            y = start_y - r * SIZE

            draw_square(x, y, BLUE)

            if board[r][c] == 1:
                draw_circle(x, y, RED)
            elif board[r][c] == 2:
                draw_circle(x, y, YELLOW)

    screen.update()


def valid(col):
    return board[0][col] == 0


def drop_piece(col, piece):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == 0:
            board[r][col] = piece
            return True
    return False


def check_win(piece):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # Diagonal down
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Diagonal up
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False


def show_winner(player):
    pen.penup()
    pen.goto(-200, 0)
    pen.color(RED if player == 1 else YELLOW)
    pen.write(
        f"Player {player} Wins!",
        font=("Arial", 35, "bold")
    )
    screen.update()


def click(x, y):
    global player, game_over

    if game_over:
        return

    start_x = -(WIDTH // 2)

    col = int((x - start_x) // SIZE)

    if 0 <= col < COLS:
        if valid(col):
            drop_piece(col, player)
            draw_board()

            if check_win(player):
                show_winner(player)
                game_over = True
                return

            player = 2 if player == 1 else 1


draw_board()

screen.onclick(click)

screen.mainloop()