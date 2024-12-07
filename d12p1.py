from collections import defaultdict

from utils import get_lines, get_input_for_day

transitions = defaultdict(set)
completed_paths = set()
cur_path = []


def delve(cur):
    if cur == 'end':
        completed_paths.add(f'{'|'.join(cur_path)}|end')
        return

    cur_path.append(cur)

    for neighbor in transitions[cur]:
        if neighbor == 'start' or neighbor.islower() and neighbor in cur_path:
            continue
        delve(neighbor)

    if cur_path:
        cur_path.pop()


def run(lines):
    global transitions, completed_paths, cur_path
    transitions, completed_paths, cur_path = defaultdict(set), set(), []

    for line in lines:
        nodes = line.split('-')
        transitions[nodes[0]].add(nodes[1])
        transitions[nodes[1]].add(nodes[0])

    delve('start')
    return len(completed_paths)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d12')))
