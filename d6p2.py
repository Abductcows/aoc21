from utils import get_lines, get_input_for_day
from collections import defaultdict

def run(lines):
    values = map(int, lines[0].split(','))
    fish = defaultdict(lambda: 0)
    for val in values:
        fish[val] += 1

    for _ in range(256):
        zero = fish[0]
        for i in range(1, 9):
            fish[i - 1] = fish[i]
        fish[6] += zero
        fish[8] = zero

    return sum(fish.values())

if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d6')))
