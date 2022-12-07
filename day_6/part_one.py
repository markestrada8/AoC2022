from data import buffer


def find_marker():
    current = []
    counter = 0
    for char in buffer:
        if char == '\n':
            continue
        current.append(char)
        counter += 1
        if counter > 3:
            if len(current) == len(set(current)):
                return counter
            current.pop(0)


print(find_marker())
