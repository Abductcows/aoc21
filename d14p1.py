from utils import get_lines, get_input_for_day
import re


def run(lines):
    cur = list(lines[0])

    rules = {}
    for line in lines[2:]:
        left, right = re.findall(r'[A-Z]+', line)
        rules[left] = right

    for _ in range(10):
        next_gen = []
        for i in range(len(cur) - 1):
            next_gen.append(cur[i])
            next_gen.append(rules[''.join(cur[i:i + 2])])
        next_gen.append(cur[-1])
        cur = next_gen

    counts = {cur.count(val) for val in set(cur)}
    return max(counts) - min(counts)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d14')))
