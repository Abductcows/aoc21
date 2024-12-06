from utils import get_lines, get_input_for_day

closers = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}


def run(lines):
    score = 0

    for line in lines:
        symbolstack = []
        for char in line:
            if char not in scores:
                symbolstack.append(char)
            else:
                if not symbolstack or char != closers[symbolstack[-1]]:
                    score += scores[char]
                    break
                else:
                    symbolstack.pop()
    return score


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d10')))
