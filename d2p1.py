from utils import get_lines, get_input_for_day



def get_direction_coords(direction, length):
    direction_map = {'forward': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    x, y = direction_map[direction]
    return x * int(length), y * int(length)


def run(lines):
    x, y = 0, 0

    for line in lines:
        move = get_direction_coords(*line.split(' '))
        x += move[0]
        y += move[1]

    return -x * y


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d2')))
