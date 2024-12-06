import re
from collections import deque
from functools import reduce

from utils import get_lines, get_input_for_day


def get_neighbors(row, col, m, n):
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [rowcol for rowcol in neighbors if 0 <= rowcol[0] < m and 0 <= rowcol[1] < n]


def get_low_points(grid):
    low_points = []
    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            val = grid[row][col]
            neighbors = get_neighbors(row, col, m, n)
            if all((val < grid[neighbor[0]][neighbor[1]] for neighbor in neighbors)):
                low_points.append((row, col))
    return low_points


def run(lines):
    grid = [list(map(int, re.findall(r'\d', line))) for line in lines]
    low_points = get_low_points(grid)
    m, n = len(grid), len(grid[0])
    basins = []
    seen = set()

    for low_point in low_points:
        seen.add(low_point)
        process_queue = deque([low_point])
        basin = []
        while process_queue:
            cur = process_queue.pop()
            basin.append(cur)
            neighbors = get_neighbors(*cur, m, n)

            for neighbor in neighbors:
                if neighbor in seen or grid[neighbor[0]][neighbor[1]] == 9 or \
                        grid[neighbor[0]][neighbor[1]] <= grid[cur[0]][cur[1]]:
                    continue
                seen.add(neighbor)
                process_queue.appendleft(neighbor)

        basins.append(basin)

    basins = sorted(basins, key=len)
    return reduce(lambda acc, v: acc * len(v), basins[-3:], 1)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d9')))
