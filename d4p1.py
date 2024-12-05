import re

from utils import run_with_file, get_input_for_day


def count_all_in_sequence(start, offsets, number_of_steps, letters, n):
    start_1d = n * start[0] + start[1]
    step = n * offsets[0] + offsets[1]
    stop = start_1d + step * number_of_steps
    x = letters[start_1d:stop:step]
    return x.count(True)


def run(lines):
    lines = [line for line in lines if line.strip()]
    winner_sequence = [int(e) for e in lines[0].split(',')]
    lines = lines[1:]
    n = 5

    boards = []
    for board_index in range(len(lines) // 5):
        board_lines = lines[5 * board_index:5 * board_index + 5]
        board_lines_1d = [int(num) for line in board_lines for num in re.findall(r'\d+', line)]
        boards.append(board_lines_1d)
    hits = [[False] * (n * n) for _board in range(len(boards))]

    number_traversals = [
        *[((row, 0), (0, 1), n) for row in range(n)],
        *[((0, col), (1, 0), n) for col in range(n)],
    ]

    winner = -1
    winning_num = -1
    for num in winner_sequence:
        if winner >= 0:
            break
        for i in range(len(boards)):
            if num in boards[i]:
                found_index = boards[i].index(num)
                hits[i][found_index] = True
        for i in range(len(boards)):
            if winner >= 0:
                break
            for start, diffs, element_count in number_traversals:
                res = count_all_in_sequence(start, diffs, element_count, hits[i], n)
                if res == 5:
                    winner = i
                    winning_num = num
                    break

    not_found_sum = sum((boards[winner][i] for i in range(n * n) if not hits[winner][i]))

    return winning_num * not_found_sum


if __name__ == '__main__':
    print(run_with_file('example.txt', run))
    print(run(get_input_for_day('d4')))
