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

    bit_len = len(lines[0])
    nums = [int(line, 2) for line in lines]

    gamma = 0
    for i in range(bit_len):
        mask = 1 << i

        half_mark = mask * len(nums) // 2
        test = sum((num & mask for num in nums))

        if test > half_mark:
            gamma |= mask

    epsilon = ~gamma & ((1 << bit_len) - 1)
    print(f'{gamma=:0{bit_len}b}, {epsilon=:0{bit_len}b}')
    print(gamma * epsilon)


if __name__ == '__main__':
    run('example.txt')
    run('input.txt')
