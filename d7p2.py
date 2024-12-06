from utils import get_lines, get_input_for_day


def run(lines):
    nums = list(map(int, lines[0].split(',')))
    # black magic?
    point = round(sum(nums) / len(nums) - 1/2)
    return sum((abs(val - point) * (abs(val - point) + 1) // 2 for val in nums))


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d7')))
