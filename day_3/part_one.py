import string
import time
start = time.time()

priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)

total = 0
duplicates = []


def find_duplicate(lines):
    for char in lines[0]:
        if char in lines[1]:
            return char


with open('data.txt', 'r') as file:
    line_pairs = [(line.strip('\n')[:len(line)//2], line.strip('\n')
                   [len(line)//2:]) for line in file.readlines()]
    for line_pair in line_pairs:
        duplicates.append(find_duplicate(line_pair))

for char in duplicates:
    total += (priorities.index(char) + 1)

print(total)
print('Time:', time.time() - start)
