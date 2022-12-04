import string
import time
start = time.time()

priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)


def find_triplicate(lines):
    for char in lines[0]:
        if char in lines[1] and char in lines[2]:
            return char


triplicates = []
total = 0

with open('data.txt', 'r') as file:
    lines = [line.strip('\n') for line in file.readlines()]
    line_triplets = []
    for i in range(3, len(lines) + 3, 3):
        line_triplets.append(lines[i-3:i])

    for line_triplet in line_triplets:
        triplicates.append(find_triplicate(line_triplet))

for char in triplicates:
    total += (priorities.index(char) + 1)

print(total)
print('Time:', time.time() - start)
