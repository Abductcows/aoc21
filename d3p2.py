from utils import run_with_file, get_input_for_day


def get_gamma_epsilon(nbits, nums):
    gamma = 0

    for i in range(nbits):
        mask = 1 << i
        one_count = sum(1 for num in nums if num & mask)
        zero_count = len(nums) - one_count

        if one_count >= zero_count:
            gamma |= mask

    epsilon = ~gamma & ((1 << nbits) - 1)
    return gamma, epsilon


def run(lines):
    nbits = len(lines[0])
    nums_oxy = [int(e, 2) for e in lines]
    nums_co2 = nums_oxy[::]

    oxy, co2 = -1, -1
    cursor = 1 << nbits - 1

    while cursor > 0:
        if oxy < 0:
            gamma = get_gamma_epsilon(nbits, nums_oxy)[0]
            good_ones = [e for e in nums_oxy if (e ^ gamma) & cursor == 0]
            if len(good_ones) == 1:
                oxy = good_ones[0]
            nums_oxy = good_ones

        if co2 < 0:
            epsilon = get_gamma_epsilon(nbits, nums_co2)[1]
            good_ones = [e for e in nums_co2 if (e ^ epsilon) & cursor == 0]
            if len(good_ones) == 1:
                co2 = good_ones[0]
            nums_co2 = good_ones

        cursor >>= 1

    print(f'{oxy=:0{nbits}b}, {co2=:0{nbits}b}')
    return oxy * co2


if __name__ == '__main__':
    print(run_with_file('example.txt', run))
    print(run(get_input_for_day('d3')))
