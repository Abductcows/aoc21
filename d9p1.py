from utils import get_lines, get_input_for_day
import re


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
    return sum((1 + grid[point[0]][point[1]] for point in low_points))


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d9')))
