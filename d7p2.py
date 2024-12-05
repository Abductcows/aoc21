from utils import get_lines, get_input_for_day


def run(lines):
    nums = sorted(map(int, lines[0].split(',')))
    # something close to mean?
    mean, median = sum(nums) / len(nums), nums[len(nums) // 2]
    step = 1 if mean <= median else -1

    result = 9_223_372_036_854_775_806
    for point in range(int(mean) - step, int(mean) + 10 * step, step):
        result = min(result, sum((abs(val - point) * (abs(val - point) + 1) // 2 for val in nums)))

    return result


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d7')))
