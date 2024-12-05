from utils import run_with_file, get_input_for_day


def run(lines):
    nums = sorted(map(int, lines[0].split(',')))
    # pick median
    median = nums[len(nums) // 2]
    return sum((abs(val - median) for val in nums))


if __name__ == '__main__':
    print(run_with_file('example.txt', run))
    print(run(get_input_for_day('d7')))
