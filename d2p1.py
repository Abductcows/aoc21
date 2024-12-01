def get_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip('\n'))

    while lines and not lines[-1]:
        lines.pop()

    return lines


def get_direction_coords(direction, length):
    direction_map = {'forward': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    x, y = direction_map[direction]
    return x * int(length), y * int(length)


def run(filename):
    lines = get_lines(filename)

    x, y = 0, 0

    for line in lines:
        move = get_direction_coords(*line.split(' '))
        x += move[0]
        y += move[1]

    print(x * y)


if __name__ == '__main__':
    run('example.txt')
    run('input.txt')
