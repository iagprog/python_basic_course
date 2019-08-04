class Player:
    def __init__(self, name, board, board_size, player_sign):
        self.name = name
        self.board = board
        self.player_sign = player_sign
        self.board_size = board_size

    def put_sign(self, pos):
        pos[0] = int(pos[0]) - 1
        pos[1] = int(pos[1]) - 1
        for i, el in enumerate(self.board):
            if i == pos[0]:
                el[pos[1]] = self.player_sign

    def check_pos(self, pos):
        pos[0] = int(pos[0]) - 1
        pos[1] = int(pos[1]) - 1
        for i, el in enumerate(self.board):
            if i == pos[0]:
                if el[pos[1]] != '':
                    return False
        return True

    def check_win(self):
        for i, el in enumerate(self.board):                                  # проверяем строки
            if el.count(self.player_sign) == self.board_size:
                print(f"\n{self.name} - you won on the row number {i+1}!")
                return True
        for i in range(self.board_size):                                     # проверяем столбцы
            tmp_list = [el[i] for el in self.board]
            if tmp_list.count(self.player_sign) == self.board_size:
                print(f"\n{self.name} - you won on the column number {i+1}!")
                return True
        i = self.board_size                                                  # проверяем диагонали
        tmp_list = [el[j] for j, el in enumerate(self.board)]
        tmp_list2 = [el[i-j-1] for j, el in enumerate(self.board)]
        if tmp_list.count(self.player_sign) == self.board_size \
                or tmp_list2.count(self.player_sign) == self.board_size:
            print(f"\n{self.name} - you won diagonally!")
            return True
        return False


def show_board(board, board_size):
    print("\n")
    for i in range(board_size):
        print(f"  {i+1:^3}", end='')
    for i, el in enumerate(board):
        print(f"\n{'-----' * board_size}")
        for j, el2 in enumerate(el):
            if j == 0:
                print(f"{i+1}|", end='')
            print(f" {el2:<2}|", end=' ')


def empty_cells(board):
    for el in board:
        if '' in el:
            return True
    return False


def check_coordinates(player, pos, board_size):
    if len(pos) != 2:
        print("Error! You should enter 2 coordinates x and y.")
        return False
    for el in pos:
        if not el.isdigit() or int(el) > board_size:
            print(f"Error!x and y are digits <= {board_size}")
            return False
    if not player.check_pos(pos[:]):
        print("The cell is already taken.")
        return False
    return True


def enter_coordinates(name, sign, player, board_size):
    while True:
        coordinates = input(f"\n{name}, enter coordinates of your sign ('{sign}') as 'x y': ").split()
        if check_coordinates(player, coordinates, board_size):
            return coordinates


def start_game(board_size):
    board = [['']*board_size for _ in range(board_size)]
    sign = input("Player1, select you sign (X/O for example): ")
    player1 = Player('Player1', board, board_size, sign)
    sign = input("Player2, select you sign (X/O for example): ")
    player2 = Player('Player2', board, board_size, sign)
    while True:
        show_board(board, board_size)
        print("\n\nx - row, y - column")
        coordinates = enter_coordinates("Player1", player1.player_sign,
                                        player2, board_size)   # передаем объект другого игрока, чтобы
        player1.put_sign(coordinates)                          # проверить доступность координат
        show_board(board, board_size)
        if not empty_cells(board):
            print("\nDraw! There are no more empty cells.")
            break
        if player1.check_win():
            break
        coordinates = enter_coordinates("Player2", player2.player_sign,
                                        player1, board_size)
        player2.put_sign(coordinates)
        if not empty_cells(board):
            print("\nDraw! There are no more empty cells.")
            break
        show_board(board, board_size)
        if player2.check_win():
            break


print("Noughts and crosses game.")
while True:
    n = input("Enter 'n', number of cells > 2 (n * n): ")
    if n.isdigit() and int(n) > 2:
        start_game(int(n))
        break
    else:
        print("Error! You should enter one digit > 2.")
