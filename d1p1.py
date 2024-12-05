from utils import run_with_file, get_input_for_day


def run(lines):
    values = [int(e) for e in lines]

    total = 0
    prev = values[0]

    for e in values[1:]:
        if e > prev:
            total += 1
        prev = e

    return total


if __name__ == '__main__':
    print(run_with_file('example.txt', run))
    print(run(get_input_for_day('d1')))
