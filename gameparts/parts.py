class Board:
    """Класс, который описывает игровое поле"""

    field_size = 3

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def make_move(self, coordinate_x: int, coordinate_y: int, symbol: str) -> None:
        '''Метод обрабатывающий ходы игроков'''
        if self.board[coordinate_x][coordinate_y] == " ":
            self.board[coordinate_x][coordinate_y] = symbol
        else:
            print('Клетка уже занята!')

    def display(self):
        for row in self.board:
            print(*row, sep=' | ')
            print('-' * 10)

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
