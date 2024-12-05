from utils import get_lines, get_input_for_day


def get_direction_coords(direction, length, aim):
    direction_map = {'forward': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    length = int(length)
    x_move, y_move = 0, 0

    if direction == 'forward':
        y_move = aim * length
        x_move = length
    else:
        aim += direction_map[direction][1] * length

    return x_move, y_move, aim


def run(lines):
    x, y, aim = 0, 0, 0

    for line in lines:
        move = get_direction_coords(*line.split(' '), aim)
        x += move[0]
        y += move[1]
        aim = move[2]

    return -x * y


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d2')))
