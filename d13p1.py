from re import findall

from utils import get_lines, get_input_for_day

import re


def run(lines):
    i = 0
    points = set()
    while lines[i]:
        x, y = list(map(int, lines[i].split(',')))
        points.add((x, y))
        i += 1

    for line in lines[i + 1: i + 2]:
        axis, val = re.findall(r'([xy])=(\d+)', line)[0]
        axis, val = 1 if axis == 'y' else 0, int(val)
        next_gen = []

        for point in points:
            if point[axis] > val:
                next_gen.append((point[0], 2 * val - point[1]) if axis == 1 else (2 * val - point[0], point[1]))
            else:
                next_gen.append(point)

        points = set(next_gen)

    grid = [['#' if (col, row) in points else '.' for col in range(41)] for row in range(7)]
    for grid_line in grid:
        print(' '.join(grid_line))
    print()
    return len(points)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d13')))
