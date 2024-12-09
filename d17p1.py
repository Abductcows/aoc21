import re
from itertools import product
from math import floor, ceil, sqrt

from utils import get_lines, get_input_for_day


def solve_quadratic(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        return tuple()
    x1 = (-b + sqrt(disc) / (2 * a))
    x2 = (-b - sqrt(disc) / (2 * a))
    return x1, x2


def try_initials(bound_l, bound_r):
    for initial in range(999, 0, -1):
        lbound_sol = [t for t in solve_quadratic(-0.5, initial + 0.5, -bound_l) if t >= 0]
        rbound_sol = [t for t in solve_quadratic(-0.5, initial + 0.5, -bound_r) if t >= 0]

        for lsol, rsol in product(lbound_sol, rbound_sol):
            lsol, rsol = sorted((lsol, rsol))
            allowed_t = range(ceil(lsol), floor(rsol) + 1)
            if allowed_t:
                return initial


def run(lines):
    x_l, x_r, y_l, y_r = list(map(int, re.findall(r'-?\d+', lines[0])))
    y0_max = try_initials(y_l, y_r)
    return int((y0_max + 0.5) ** 2) // 2


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d17')))
