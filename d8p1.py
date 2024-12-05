import re
from collections import defaultdict

from utils import get_lines, get_input_for_day


def run(lines):
    occurences = defaultdict(lambda: 0)
    target_lengths = [2, 3, 4, 7]

    for line in lines:
        output_values = re.findall(r'[a-z]+', line.split('|')[1])
        for value in output_values:
            occurences[len(value)] += 1

    return sum((occurences[pattern_len] for pattern_len in occurences if pattern_len in target_lengths))


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d8')))
