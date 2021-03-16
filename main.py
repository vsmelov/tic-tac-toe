field = [[' '] * 3 for row_index in range(3)]


def check(target: str) -> bool:
    for row_index in range(3):  # check row
        if all(field[row_index][column_index] == target for column_index in range(3)):
            return True
    for column_index in range(3):  # check column
        if all(field[row_index][column_index] == target for row_index in range(3)):
            return True
    if all(field[diag_index][diag_index] == target for diag_index in range(3)):  # check diag
        return True
    if all(field[diag_index][2-diag_index] == target for diag_index in range(3)):  # check reverse diag
        return True


def print_field():
    for row in field:
        print('|' + '|'.join(row) + '|')


print_field()
current_player = 'x'

while True:
    action = input('Введите координаты игрок "{}": '.format(current_player))
    try:
        row_index, column_index = map(int, action.split(' '))
    except (ValueError, AssertionError):
        print(f'неправильный формат команды, введите ее в формате "x y", например "0 2"')
        continue
    if not (0 <= row_index < 3 and 0 <= column_index < 3):
        print('индексы должны быть от 0 до 2')
        continue
    if field[row_index][column_index] != ' ':
        print('поле уже занято символом "{}"'.format(field[row_index][column_index]))
        continue
    field[row_index][column_index] = current_player
    print_field()
    if check(current_player):
        print("Игрок {} выйграл".format(current_player))
        break
    if all(field[row_index][column_index] != ' ' for row_index in range(3) for column_index in range(3)):
        print('Ничья')
        break
    if current_player == 'x':
        current_player = 'o'
    elif current_player == 'o':
        current_player = 'x'
    else:
        raise ValueError('unknown player {}'.format(current_player))
