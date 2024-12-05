import re


def run_with_file(file, run_function):
    lines = get_lines(file)
    return run_function(lines)


def get_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip('\n'))

    while lines and not lines[-1]:
        lines.pop()

    return lines


def get_input_for_day(day_with_num):
    assert re.fullmatch(r'd(\d+)', day_with_num)
    lines = []
    with open('inputs.txt') as file:
        while True:
            line = file.readline()
            if not line or line.startswith(f'{day_with_num}:'):
                break
        while True:
            line = file.readline()
            if not line or re.match(r'd(\d+):', line):
                break
            lines.append(line.rstrip('\n'))

    while lines and not lines[-1]:
        lines.pop()
    while lines and not lines[0]:
        lines.remove(0)

    return lines
