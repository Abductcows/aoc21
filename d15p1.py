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
    return risky_dijkstra(grid)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d15')))
