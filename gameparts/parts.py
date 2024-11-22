class Board:
    """Класс, который описывает игровое поле"""

    field_size = 3

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def make_move(self, coordinate_x: int,
                  coordinate_y: int,
                  symbol: str) -> None:
        '''Метод обрабатывающий ходы игроков'''
        self.board[coordinate_x][coordinate_y] = symbol

    def display(self):
        for row in self.board:
            print(*row, sep=' | ')
            print('-' * 10)

    def is_board_full(self):
        for i in range(self.field_size):
            if ' ' in self.board[i]:
                return False
        return True

    def check_win(self, player):
        for i in range(self.field_size):
            if (all([self.board[i][j] == player
                     for j in range(self.field_size)]) or
                all([self.board[j][i] == player
                     for j in range(self.field_size)])):
                return True

        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
