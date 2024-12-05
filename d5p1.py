import itertools
import re
from collections import defaultdict

from utils import run_with_file, get_input_for_day


def sign(x):
    return (x > 0) - (x < 0)


def run(lines):
    line_heights = defaultdict(lambda: 0)
    for line in lines:
        x1, y1, x2, y2 = list(map(int, re.findall(r'\d+', line)))
        if x1 != x2 and y1 != y2:
            continue

        x_step = 1 if x1 <= x2 else -1
        y_step = 1 if y1 <= y2 else -1

        for x, y in itertools.product(range(x1, x2 + x_step, x_step), range(y1, y2 + y_step, y_step)):
            line_heights[(x, y)] += 1

    return len([val for val in line_heights.values() if val > 1])


if __name__ == '__main__':
    print(run_with_file('example.txt', run))
    print(run(get_input_for_day('d5')))
