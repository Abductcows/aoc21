import re
from itertools import product
from math import floor, ceil, sqrt

from utils import get_lines, get_input_for_day


def solve_quadratic(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        return tuple()
    x1 = (-b + sqrt(disc)) / (2 * a)
    x2 = (-b - sqrt(disc)) / (2 * a)
    return x1, x2


def integers_between(a, b):
    a, b = sorted((a, b))
    return set(range(int(ceil(a)), int(floor(b)) + 1))


def try_initials(bound_xl, bound_xr, bound_yl, bound_yr):
    allowed_initials = []
    for x0 in range(1, bound_xr + 1):
        x_lbound_sol = solve_quadratic(-0.5, x0 + 0.5, -bound_xl)
        if not x_lbound_sol:
            continue
        x_lbound_sol = min(x_lbound_sol)
        x_rbound_sol = solve_quadratic(-0.5, x0 + 0.5, -bound_xr)
        x_rbound_sol = min(x_rbound_sol or [9999])


        for y0 in range(-bound_yl, bound_yl - 1, -1):
            y_lbound_sol = max(solve_quadratic(-0.5, y0 + 0.5, -bound_yl))
            y_rbound_sol = max(solve_quadratic(-0.5, y0 + 0.5, -bound_yr))

            allowed_t = integers_between(x_lbound_sol, x_rbound_sol) & integers_between(y_lbound_sol, y_rbound_sol)
            if allowed_t:
                allowed_initials.append((x0, y0))

    return allowed_initials


def run(lines):
    xl, xr, yl, yr = list(map(int, re.findall(r'-?\d+', lines[0])))
    allowed_both = try_initials(xl, xr, yl, yr)

    for entry in sorted(allowed_both):
        print(entry)
    return len(allowed_both)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d17')))
