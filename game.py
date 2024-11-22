from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(text: str) -> None:
    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')


def main():
    game = Board()
    game.display()

    current_player = 'X'
    running = True

    while running:

        print(f'Ход делают {current_player}')

        while True:

            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError

                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError

                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError

            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения строки и столбца заново.')
                continue

            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue

            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения строки и столбца заново.')
                continue

            except Exception as e:
                print(f'Возникла ошибка: {e}')

            else:
                break

        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()

        if game.check_win(current_player):
            winner = f'Победили {current_player}.'
            print(winner)
            save_result(winner)
            running = False
        elif game.is_board_full():
            print('Ничья!')
            save_result('Ничья!')
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
