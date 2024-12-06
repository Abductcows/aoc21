import re

from utils import get_lines, get_input_for_day
from itertools import product
from collections import deque


def debug(octa):
    for row in octa:
        for e in row:
            print(e, end=' ')
        print()


def get_neighbors(row, col, m, n):
    neighbors = [(row + i, col + j) for i, j in product(range(-1, 2), repeat=2) if i != 0 or j != 0]
    return [rowcol for rowcol in neighbors if 0 <= rowcol[0] < m and 0 <= rowcol[1] < n]


def run(lines):
    total_flashes = 0
    m, n = len(lines), len(lines[0])
    octa = [list(map(int, re.findall(r'\d', line))) for line in lines]

    for _ in range(100):
        flashed = set()
        to_process = deque()

        for row, col in product(range(m), range(n)):
            octa[row][col] += 1
            if octa[row][col] > 9:
                flashed.add((row, col))
                to_process.appendleft((row, col))

        while to_process:
            cur = to_process.pop()
            total_flashes += 1
            neighbors = get_neighbors(*cur, m, n)
            for neighbor in neighbors:
                octa[neighbor[0]][neighbor[1]] += 1
                if octa[neighbor[0]][neighbor[1]] > 9 and neighbor not in flashed:
                    flashed.add(neighbor)
                    to_process.appendleft(neighbor)

        for row, col in product(range(m), range(n)):
            if octa[row][col] > 9:
                octa[row][col] = 0

    return total_flashes


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d11')))
