def get_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip('\n'))

    while lines and not lines[-1]:
        lines.pop()

    return lines


def run(filename):
    lines = get_lines(filename)

    w_len = 3
    values = [int(e) for e in lines] + [0] * w_len
    values = [sum(values[i: i + w_len]) for i in range(len(lines))]

    total = 0
    prev = values[0]

    for e in values[1:]:
        if e > prev:
            total += 1
        prev = e

    print(total)


if __name__ == '__main__':
    run('example.txt')
    run('input.txt')
