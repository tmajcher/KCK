import pygame

empty = 0
friendly = {'pawn': 1, 'king': 3}
enemy = {'pawn': 2, 'king': 4}

rows = 8
columns = 8


def create_board():
    board = [[empty for column in range(columns)] for row in range(rows)]
    return board


def place_starting_pieces():
    for current_row in range(5, 8, 2):
        for current_column in range(0, 8, 2):
            board[current_row][current_column] = friendly['pawn']

    for current_row in range(6, 7):
        for current_column in range(1, 8, 2):
            board[current_row][current_column] = friendly['pawn']

    for current_row in range(0, 3, 2):
        for current_column in range(1, 8, 2):
            board[current_row][current_column] = enemy['pawn']

    for current_row in range(1, 2):
        for current_column in range(0, 7, 2):
            board[current_row][current_column] = enemy['pawn']


def is_valid_selection(board, current_player, old_x, old_y):
    board_selection = board[old_y][old_x]
    if (board_selection == friendly['pawn'] or friendly['king']):
        return True
    elif (board_selection == enemy['pawn'] or enemy['king']):
        print("Wybrales pionek przeciwnika")
        return False
    else:
        print("Nie wybrales pionka")
        return False


def is_valid_move(current_player, board, old_x, old_y, new_x, new_y):
    if (board[new_y][new_x]) != empty:
        print("Zajete miejsce")
        return False

    if (board[old_y][old_x] == 1):
        if (new_y - old_y) == -1 and (new_x - old_x) == 1:
            return True
        elif (new_y - old_y) == -1 and (new_x - old_x) == -1:
            return True


        # Do góry w prawo
        elif (new_y - old_y) == -2 and (new_x - old_x) == 2:
            if board[new_y + 1][new_x - 1] == friendly['pawn'] and friendly['king']:
                print("Chcesz zbić swojego pionka?")
                return False
            elif board[new_y + 1][new_x - 1] == enemy['pawn'] or enemy['king']:
                board[new_y + 1][new_x - 1] = empty
                return True
            else:
                return False
        # Do góry w lewo
        elif (new_y - old_y) == -2 and (new_x - old_x) == -2:
            if board[new_y + 1][new_x + 1] == friendly['pawn'] and friendly['king']:
                print("Chcesz zbić swojego pionka?")
                return False
            elif board[new_y + 1][new_x + 1] == enemy['pawn'] or enemy['king']:
                board[new_y + 1][new_x + 1] = empty
                return True
            else:
                return False

    elif board[old_y][old_x] == 2:
        if (new_y - old_y) == 1 and (new_x - old_x) == 1:
            return True
        elif (new_y - old_y) == 1 and (new_x - old_x) == -1:
            return True

        # Do dołu w prawo
        elif (new_y - old_y) == 2 and (new_x - old_x) == 2:
            if board[new_y - 1][new_x - 1] == friendly['pawn'] and friendly['king']:
                print("Chcesz zbić swojego pionka?")
                return False
            elif board[new_y - 1][new_x - 1] == enemy['pawn'] or enemy['king']:
                board[new_y - 1][new_x - 1] = empty
                return True
            else:
                return False
        # Do dołu w lewo
        elif (new_y - old_y) == 2 and (new_x - old_x) == -2:
            if board[new_y - 1][new_x + 1] == friendly['pawn'] and friendly['king']:
                print("Chcesz zbić swojego pionka?")
                return False
            elif board[new_y - 1][new_x + 1] == enemy['pawn'] or enemy['king']:
                board[new_y - 1][new_x + 1] = empty
                return True
            else:
                return False
    else:
        print("Za daleko")
        return False


def no_chips_between(board, old_x, old_y, new_x, new_y):
    board_y_coords = []
    board_x_coords = []
    if old_y < new_y:
        for row in range(old_y, new_y):
            board_y_coords.append(row)
    if old_y > new_y:
        for row in range(old_y, new_y, -1):
            board_y_coords.append(row)
    if old_x < new_x:
        for column in range(old_x, new_x):
            board_x_coords.append(column)
    if old_x > new_x:
        for column in range(old_x, new_x, -1):
            board_x_coords.append(column)

    board_coords = list(zip(board_x_coords, board_y_coords))
    board_values = [board[y][x] for x, y in board_coords]
    if len(board_values) > 2:
        if all(i == empty for i in board_values[1:-1]) is True:
            board[new_y][new_x] = board[old_y][old_x]
            board[old_y][old_x] = empty
            return True

    if len(board_values) == 2:
        if all(i == enemy['pawn'] for i in board_values[1:]) is True:
            board[new_y][new_x] = board[old_y][old_x]
            board[old_y][old_x] = empty
            return True
        elif all(i == enemy['king'] for i in board_values[1:]) is True:
            board[new_y][new_x] = board[old_y][old_x]
            board[old_y][old_x] = empty
            return True
        elif all(i == empty for i in board_values[1:]) is True:
            board[new_y][new_x] = board[old_y][old_x]
            board[old_y][old_x] = empty
            return True

    elif len(board_values) == 1:
        if all(i == empty for i in board_values[1:]) is True:
            board[new_y][new_x] = board[old_y][old_x]
            board[old_y][old_x] = empty
            return True
    else:
        print("Nie można przeskoczyc nad wiecej niz 1 pionkiem")
        return False


def is_valid_king_move(current_player, board, old_x, old_y, new_x, new_y):
    if board[new_y][new_x] != 0:
        return False
    if new_y == old_y:
        return False
    if new_x == old_x:
        return False

    if new_x > old_x and new_y > old_y:
        if (new_x - old_x) != (new_y - old_y):
            return False
    if new_x < old_x and new_y < old_y:
        if (old_x - new_x) != (old_y - new_y):
            return False
    if new_x < old_x and new_y > old_y:
        if (old_x - new_x) != (new_y - old_y):
            return False
    if new_x > old_x and new_y < old_y:
        if (new_x - old_x) != (old_y - new_y):
            return False

    if board[old_y][old_x] == friendly['king']:
        try:
            if board[new_y + 1][new_x - 1] == enemy['pawn'] or enemy['king']:
                if old_x < new_x and old_y > new_y:
                    if no_chips_between(board, old_x, old_y, new_x, new_y) is True:
                        board[new_y][new_x] = friendly['king']
                        board[new_y + 1][new_x - 1] = empty
                        board_selection = empty
                        return True
        except IndexError:
            pass

        try:
            if board[new_y + 1][new_x + 1] == enemy['pawn'] or enemy['king']:
                if old_x > new_x and old_y > new_y:
                    if no_chips_between(board, old_x, old_y, new_x, new_y) is True:
                        board[new_y][new_x] = friendly['king']
                        board[new_y + 1][new_x + 1] = empty
                        board_selection = empty
                        return True
        except IndexError:
            pass

        try:
            if board[new_y - 1][new_x - 1] == enemy['pawn'] or enemy['king']:
                if no_chips_between(board, old_x, old_y, new_x, new_y) is True:
                    if old_x < new_x and old_y < new_y:
                        board[new_y][new_x] = friendly['king']
                        board[new_y - 1][new_x - 1] = empty
                        board_selection = empty
                        return True
        except IndexError:
            pass

        try:
            if board[new_y - 1][new_x + 1] == enemy['pawn'] or enemy['king']:
                if no_chips_between(board, old_x, old_y, new_x, new_y) is True:
                    if old_x > new_x and old_y < new_y:
                        board[new_y][new_x] = friendly['king']
                        board[new_y - 1][new_x + 1] = empty
                        board_selection = empty
                        return True
        except IndexError:
            pass


def check_if_double_jump_possible(board, new_x, new_y):
    if current_player == 1:
        try:
            if board[new_y - 2][new_x + 2] == empty:
                if board[new_y - 1][new_x + 1] == (enemy['pawn'] or enemy['king']):
                    print("Dodatkowe bicie 1")
                    return True

            elif board[new_y - 2][new_x - 2] == empty:
                if board[new_y - 1][new_x - 1] == (enemy['pawn'] or enemy['king']):
                    print("Dodatkowe bicie 2")
                    return True
        except IndexError:
            pass

    if current_player == 2:
        try:
            if board[new_y + 2][new_x + 2] == empty:
                if board[new_y + 1][new_x + 1] == (enemy['pawn'] or enemy['king']):
                    print("Dodatkowe bicie 3")
                    return True

            elif board[new_y + 2][new_x - 2] == empty:
                if board[new_y + 1][new_x - 1] == (enemy['pawn'] or enemy['king']):
                    print("Dodatkowe bicie 4")
                    return True
        except IndexError:
            pass

    if board[new_y][new_x] == friendly['king']:
        try:
            for i in range(8):
                if board[new_y - i][new_x + i] == (enemy['king']):
                    if board[new_y - (i + 1)][new_x + (i + 1)] == empty:
                        return True

                elif board[new_y - i][new_x - i] == (enemy['king']):
                    if board[new_y - (i + 1)][new_x - (i + 1)] == empty:
                        return True

                elif board[new_y + i][new_x + i] == (enemy['king']):
                    if board[new_y + (i + 1)][new_x + (i + 1)] == empty:
                        return True

                elif board[new_y + i][new_x - i] == (enemy['king']):
                    if board[new_y + (i + 1)][new_x - (i + 1)] == empty:
                        return True
        except IndexError:
            pass
    else:
        return False


def check_for_win(current_player, board):
    remaining_enemy_pieces = []
    for row in board:
        remaining_enemy_pieces.append(row.count(enemy['pawn']))
        remaining_enemy_pieces.append(row.count(enemy['king']))
    print(sum(remaining_enemy_pieces))
    if sum(remaining_enemy_pieces) == 0:
        print(f"Gracz {current_player} wygrał!")
        return True


game_over = False
board = create_board()
place_starting_pieces()

# pygame.init()

window_size = [600, 600]
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("Checkers")

clock = pygame.time.Clock()

black = (0, 0, 0)
brown = (139, 69, 19)
white = (255, 235, 205)
green = (0, 255, 0)
red = (220, 20, 60)
dark_red = (139, 0, 0)
gold = (255, 215, 0)

window_width = window_size[0]
window_height = window_size[1]
total_rows = 8
total_columns = 8
width = (window_width // total_columns)
height = (window_height // total_rows)

radius = (window_width // 20)
border = (window_width // 200)

current_player = 1
print("Kolejka czerwonych")

while not game_over:
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        mouse_matrix_pos = ((mouse_pos[0] // width), (mouse_pos[1] // height))

        if event.type == pygame.QUIT:
            game_over = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            current_pos = pygame.mouse.get_pos()
            old_x = (current_pos[0] // width)
            old_y = (current_pos[1] // height)

            previous_piece_total = sum([sum(row) for row in board])

            if is_valid_selection(board, current_player, old_x, old_y):
                pass
            else:
                continue

            while True:
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    new_pos = pygame.mouse.get_pos()
                    new_x = (new_pos[0] // width)
                    new_y = (new_pos[1] // height)

                    if board[old_y][old_x] == friendly['pawn']:
                        if is_valid_move(current_player, board, old_x, old_y, new_x, new_y):
                            board[new_y][new_x] = friendly['pawn']
                            board[old_y][old_x] = empty

                            for column in range(8):
                                if board[0][column] == 1:
                                    board[0][column] = 3
                                elif board[7][column] == 2:
                                    board[7][column] = 4

                            if (check_for_win(current_player, board)):
                                game_over = True

                            current_piece_total = sum([sum(row) for row in board])

                            if previous_piece_total > current_piece_total:
                                if check_if_double_jump_possible(board, new_x, new_y):
                                    pass
                                else:
                                    if current_player == 1:
                                        current_player = 2
                                        print("Kolejka czarnych")
                                    else:
                                        current_player = 1
                                        print("Kolejka czerwonych")
                                    friendly, enemy = enemy, friendly
                            else:
                                if current_player == 1:
                                    current_player = 2
                                    print("Kolejka czarnych")
                                else:
                                    current_player = 1
                                    print("Kolejka czerwonych")
                                friendly, enemy = enemy, friendly

                    if board[old_y][old_x] == friendly['king']:
                        if is_valid_king_move(current_player, board, old_x, old_y, new_x, new_y):

                            for column in range(8):
                                if board[0][column] == 1:
                                    board[0][column] = 3
                                elif board[7][column] == 2:
                                    board[7][column] = 4

                            if check_for_win(current_player, board):
                                game_over = True

                            current_piece_total = sum([sum(row) for row in board])

                            if previous_piece_total > current_piece_total:
                                if check_if_double_jump_possible(board, new_x, new_y):
                                    pass
                                else:
                                    if current_player == 1:
                                        current_player = 2
                                        print("Kolejka czarnych")
                                    else:
                                        current_player = 1
                                        print("Kolejka czerwonych")
                                    friendly, enemy = enemy, friendly
                            else:
                                if current_player == 1:
                                    current_player = 2
                                    print("Kolejka czarnych")
                                else:
                                    current_player = 1
                                    print("Kolejka czerwonych")
                                friendly, enemy = enemy, friendly

                    break

    for row in range(8):
        for column in range(8):
            if (row + column) % 2 == 0:
                color = white
            else:
                color = brown
            rect = pygame.draw.rect(screen, color, [width * column, height * row, width, height])
            rect_center = rect.center
            if board[row][column] == 1:
                pygame.draw.circle(screen, red, rect_center, radius)
            if board[row][column] == 2:
                pygame.draw.circle(screen, black, rect_center, radius)
            if board[row][column] == 3:
                pygame.draw.circle(screen, red, rect_center, radius)
                pygame.draw.circle(screen, gold, rect_center, radius, border)
            if board[row][column] == 4:
                pygame.draw.circle(screen, black, rect_center, radius)
                pygame.draw.circle(screen, gold, rect_center, radius, border)

    clock.tick(60)
    pygame.display.flip()
pygame.quit()
