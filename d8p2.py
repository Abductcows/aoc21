import re

from utils import get_lines, get_input_for_day

unique_lengths = [2, 3, 4, 7]
length_to_digit = {2: 1, 3: 7, 4: 4, 7: 8}


def get_digit(output_letters, num_sets):
    letters = set(output_letters)
    if len(letters) == 5:
        if len(letters & num_sets[4]) == 2:
            return 2
        if len(letters & num_sets[1]) == 1:
            return 5
        return 3
    if len(letters) == 6:
        if len(letters & num_sets[1]) == 1:
            return 6
        if len(letters & num_sets[4]) == 4:
            return 9
        return 0
    return length_to_digit[len(letters)]


def run(lines):
    total = 0
    for line in lines:
        digits_to_letters = [set() for _ in range(10)]
        input_values = re.findall(r'[a-z]+', line.split('|')[0])

        # get 1,4,7,8
        for val in input_values:
            if len(val) in unique_lengths:
                digits_to_letters[length_to_digit[len(val)]] = set(val)

        output_letters = re.findall(r'[a-z]+', line.split('|')[1])
        output_sum = 0
        for letter_group in output_letters:
            output_sum = 10 * output_sum + get_digit(letter_group, digits_to_letters)
        total += output_sum

    return total


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d8')))
