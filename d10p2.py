from html.parser import incomplete

from utils import get_lines, get_input_for_day

closers = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {')': 1, ']': 2, '}': 3, '>': 4}


def run(lines):
    scoreboard = []
    for line in lines:
        symbolstack = []
        valid = True
        for char in line:
            if char not in scores:
                symbolstack.append(char)
            elif char != closers[symbolstack[-1]]:
                valid = False
                break
            elif symbolstack:
                symbolstack.pop()

        if symbolstack and valid:
            local_score = 0
            for v in reversed(symbolstack):
                local_score = 5 * local_score + scores[closers[v]]
            scoreboard.append(local_score)

    return sorted(scoreboard)[len(scoreboard) // 2]


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d10')))
