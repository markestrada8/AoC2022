outcomes = {
    'A': {
        'X': 4,
        'Y': 8,
        'Z': 3},
    'B': {
        'X': 1,
        'Y': 5,
        'Z': 9},
    'C': {
        'X': 7,
        'Y': 2,
        'Z': 6
    },
}

with open('data.txt', 'r') as file:
    print(sum([outcomes[line.split()[0]][line.split()[1]]
          for line in file.readlines()]))
