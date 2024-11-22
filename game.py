class Board:
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


# Создать игровое поле - объект класса Board.
game = Board()
# Отрисовать поле в терминале.
game.display()
# Разместить на поле символ по указанным координатам - сделать ход.
game.make_move(1, 1, 'X')
print('Ход сделан!')
# Перерисовать поле с учётом сделанного хода.
game.display()
