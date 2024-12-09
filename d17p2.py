import re
from math import floor, ceil, sqrt

from utils import get_lines, get_input_for_day


# https://www.desmos.com/calculator/lcnbtkgzyt

def sign(n):
    return (n > 0) - (n < 0)


def solve_quadratic(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        return tuple()
    sq = sqrt(disc)
    x1 = (-b + sq) / (2 * a)
    x2 = (-b - sq) / (2 * a)
    return tuple(sorted((x1, x2)))


def integers_between(a, b):
    sign_a, sign_b = sign(a), sign(b)
    if (sign_a, sign_b) in ((-1, 1), (1, -1)):
        return integers_between(a, 0) | integers_between(0, b)
    a, b = sorted(map(abs, (a, b)))
    return set(range(sign(a) * ceil(a), sign(a) * floor(b) + sign(a)))


def try_initials(bound_xl, bound_xr, bound_yl, bound_yr):
    allowed_initials = []
    for x0 in range(1, bound_xr + 1):
        x_lbound_sol = solve_quadratic(-0.5, x0 + 0.5, -bound_xl)
        if not x_lbound_sol:
            continue
        x_lbound_sol = min(x_lbound_sol)
        x_rbound_sol = solve_quadratic(-0.5, x0 + 0.5, -bound_xr)
        if not x_rbound_sol or min(x_rbound_sol) == (x0 + 0.5) ** 2:
            x_rbound_sol = 999
        else:
            x_rbound_sol = min(x_rbound_sol)

        for y0 in range(max(1, -bound_yr), bound_yr + sign(bound_yr), sign(bound_yr)):
            y_lbound_sol = solve_quadratic(-0.5, y0 + 0.5, -bound_yl)
            if not y_lbound_sol:
                continue
            if min(y_lbound_sol) < 0:
                y_lbound_sol = max(y_lbound_sol)
                y_rbound_sol = max(solve_quadratic(-0.5, y0 + 0.5, -bound_yr))
            else:
                pass # todo for positive y bounds. not in example or input

            allowed_t = integers_between(x_lbound_sol, x_rbound_sol)
            allowed_t &= integers_between(y_lbound_sol, y_rbound_sol)

            if allowed_t:
                allowed_initials.append((x0, y0))

    return allowed_initials


def run(lines):
    xl, xr, yl, yr = list(map(int, re.findall(r'-?\d+', lines[0])))
    yl, yr = sorted((yl, yr), key=abs)
    allowed_both = try_initials(xl, xr, yl, yr)

    return len(allowed_both)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d17')))
