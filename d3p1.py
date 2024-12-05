from utils import run_with_file, get_input_for_day


def run(lines):
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
    return gamma * epsilon


if __name__ == '__main__':
    print(run_with_file('example.txt', run))
    print(run(get_input_for_day('d3')))
