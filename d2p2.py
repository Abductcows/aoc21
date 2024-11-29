def get_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip('\n'))

    while lines and not lines[-1]:
        lines.pop()

    return lines


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


def run(filename):
    lines = get_lines(filename)

    x, y, aim = 0, 0, 0

    for line in lines:
        move = get_direction_coords(*line.split(' '), aim)
        x += move[0]
        y += move[1]
        aim = move[2]

    print(x * y)


if __name__ == '__main__':
    run('example.txt')
    run('input.txt')
