from collections import defaultdict

from utils import get_lines, get_input_for_day

import re


def run(lines):
    cur = defaultdict(int)
    initial_state = lines[0].strip()
    for i in range(len(initial_state) - 1):
        cur[f'{initial_state[i]}{initial_state[i+1]}'] += 1

    rules = {}
    for line in lines[2:]:
        left, right = re.findall(r'[A-Z]+', line)
        rules[left] = right

    for _ in range(40):
        next_gen = defaultdict(int)

        for duo in cur:
            produced = rules[duo]
            count = cur[duo]
            next_gen[f'{duo[0]}{produced}'] += count
            next_gen[f'{produced}{duo[1]}'] += count

        cur = next_gen

    counts = defaultdict(int)
    for duo in cur:
        counts[duo[0]] += cur[duo]
    counts[initial_state[-1]] += 1

    return max(counts.values()) - min(counts.values())


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d14')))
