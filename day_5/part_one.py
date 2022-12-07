
rows = ['WMLF', 'BZVMF', 'HVRSLQ', 'FSVQPMTJ', 'LSW',
        'FVPMRJW', 'JQCPNRF', 'VHPSZWRB', 'BMJCGHZW']
stacks = {i + 1: [char for char in rows[i]] for i in range(len(rows))}


def handle_step(line):
    steps = [int(num) for num in line.split()[1::2]]
    for i in range(steps[0]):
        stacks[steps[2]].append(stacks[steps[1]].pop())


with open('data.txt', 'r') as file:
    for line in file.readlines():
        handle_step(line)

print(''.join([stacks[i + 1][-1] for i in range(len(stacks))]))
