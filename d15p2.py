from utils import get_lines, get_input_for_day

import heapq


def get_neighbors(row, col, m, n):
    candidates = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    return tuple((v for v in candidates if 0 <= v[0] < m and 0 <= v[1] < n))


def risky_dijkstra(grid):
    m, n = len(grid), len(grid[0])
    visited = set()
    pq = [(0, 0, 0)]

    while True:
        risk, row, col = heapq.heappop(pq)
        if (row, col) == (m - 1, n - 1):
            return risk

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for next in get_neighbors(row, col, m, n):
            if next not in visited:
                heapq.heappush(pq, (risk + grid[next[0]][next[1]], next[0], next[1]))


def run(lines):
    grid = list(map(lambda l: [int(e) for e in l], lines))
    m, n = len(grid), len(grid[0])
    actual = [[-1] * (5 * n) for _ in range(5 * m)]

    for tile_row in range(5):
        for tile_col in range(5):
            risk_increment = tile_row + tile_col
            for row in range(m):
                for col in range(n):
                    new_value = grid[row][col] + risk_increment
                    if new_value > 9:
                        new_value -= 9
                    actual[tile_row * m + row][tile_col * n + col] = new_value

    return risky_dijkstra(actual)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d15')))
